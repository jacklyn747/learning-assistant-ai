import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load environment variables
# Support both local .env file and Streamlit Cloud secrets
load_dotenv()

# Function to get API key from either .env or Streamlit secrets
def get_api_key():
    """Get OpenAI API key from environment or Streamlit secrets"""
    # Try Streamlit secrets first (for cloud deployment)
    if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
        return st.secrets['OPENAI_API_KEY']
    # Fall back to environment variable (for local development)
    return os.getenv("OPENAI_API_KEY")

# Set the API key for OpenAI
api_key = get_api_key()
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# Page configuration
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for blue and white theme
st.markdown("""
    <style>
    /* Main color scheme: Blue and White */
    .main {
        padding: 2rem;
        background-color: #ffffff;
    }

    /* Chat message styling */
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        background-color: #f8f9ff !important;
        border: 1px solid #e3e8ff;
    }

    /* User message styling */
    .stChatMessage[data-testid="user-message"] {
        background-color: #e3f2fd !important;
        border-left: 4px solid #2196F3;
    }

    /* Assistant message styling */
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #ffffff !important;
        border-left: 4px solid #1565C0;
    }

    /* Source box styling */
    .source-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        border-left: 4px solid #0288D1;
    }

    /* Header colors */
    h1 {
        color: #1565C0;
        font-weight: 700;
    }

    h2, h3 {
        color: #1976D2;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f0f7ff;
    }

    /* Button styling */
    .stButton > button {
        background-color: #2196F3;
        color: white;
        border: none;
        border-radius: 0.5rem;
        font-weight: 500;
        transition: all 0.3s;
    }

    .stButton > button:hover {
        background-color: #1976D2;
        box-shadow: 0 4px 8px rgba(33, 150, 243, 0.3);
    }

    /* Input field styling */
    .stTextInput > div > div > input {
        border-color: #2196F3;
    }

    /* Metric styling */
    [data-testid="stMetricValue"] {
        color: #1565C0;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #e3f2fd;
        border-radius: 0.5rem;
        color: #1565C0;
    }

    /* Success message */
    .stSuccess {
        background-color: #e8f5e9;
        color: #2e7d32;
    }

    /* Info message */
    .stInfo {
        background-color: #e3f2fd;
        color: #1565C0;
    }

    /* Divider */
    hr {
        border-color: #bbdefb;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

@st.cache_resource
def load_documents():
    """Load documents from the knowledge_base folder with improved error handling"""
    try:
        # Check if directory exists
        if not os.path.exists('knowledge_base/'):
            st.error("❌ Knowledge base folder not found!")
            st.info("Please create a 'knowledge_base' folder and add .txt documents.")
            return []

        # Load documents
        loader = DirectoryLoader(
            'knowledge_base/',
            glob="**/*.txt",
            loader_cls=TextLoader,
            show_progress=False,
            use_multithreading=True
        )
        documents = loader.load()

        # Validate documents loaded
        if not documents:
            st.warning("⚠️ No documents found in knowledge_base folder!")
            st.info("Please add .txt files to the knowledge_base folder.")
            return []

        # Log success
        st.info(f"📚 Successfully loaded {len(documents)} document(s)")
        return documents

    except PermissionError:
        st.error("❌ Permission denied: Cannot access knowledge_base folder")
        return []
    except UnicodeDecodeError as e:
        st.error(f"❌ Encoding error in one of the documents: {str(e)}")
        st.info("Ensure all text files are UTF-8 encoded")
        return []
    except Exception as e:
        st.error(f"❌ Unexpected error loading documents: {str(e)}")
        st.info("Please check the application logs for more details")
        return []

@st.cache_resource
def create_vectorstore(_documents):
    """Create vector store from documents with improved error handling"""
    try:
        if not _documents:
            st.error("❌ No documents provided to create vector store")
            return None

        # Split documents into chunks
        st.info("🔄 Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(_documents)

        if not chunks:
            st.error("❌ No text chunks created from documents")
            return None

        st.info(f"✅ Created {len(chunks)} text chunks")

        # Create embeddings
        st.info("🔄 Creating embeddings with OpenAI...")
        try:
            embeddings = OpenAIEmbeddings()
        except Exception as e:
            st.error(f"❌ Failed to initialize OpenAI embeddings: {str(e)}")
            st.info("Please check your OPENAI_API_KEY in the .env file")
            return None

        # Create vector store
        st.info("🔄 Building vector database...")
        try:
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                persist_directory="./chroma_db"
            )
            st.success("✅ Vector store created successfully!")
            return vectorstore
        except Exception as e:
            st.error(f"❌ Failed to create vector store: {str(e)}")
            return None

    except ImportError as e:
        st.error(f"❌ Missing required package: {str(e)}")
        st.info("Please ensure all dependencies are installed")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error creating vector store: {str(e)}")
        return None

def initialize_conversation(vectorstore):
    """Initialize the conversational retrieval chain"""
    try:
        # Create custom prompt template
        prompt_template = """You are an AI Learning Assistant specialized in instructional design, eLearning, and learning theories.
Use the following context to answer the question. If you don't know the answer based on the context, say so clearly.
Always provide detailed, educational responses.

Context: {context}

Question: {question}

Answer:"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        # Initialize memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

        # Create LLM
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )

        # Create conversational chain
        conversation = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": PROMPT}
        )

        return conversation
    except Exception as e:
        st.error(f"Error initializing conversation: {str(e)}")
        return None

def format_sources(source_documents):
    """Format source documents for display"""
    sources = []
    for i, doc in enumerate(source_documents, 1):
        source_name = os.path.basename(doc.metadata.get('source', 'Unknown'))
        content_preview = doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
        sources.append(f"**Source {i}: {source_name}**\n\n{content_preview}")
    return "\n\n---\n\n".join(sources)

def export_conversation_json():
    """Export conversation history as JSON"""
    try:
        export_data = {
            "export_date": datetime.now().isoformat(),
            "total_messages": len(st.session_state.messages),
            "conversation": st.session_state.messages
        }
        return json.dumps(export_data, indent=2)
    except Exception as e:
        st.error(f"Error exporting to JSON: {str(e)}")
        return None

def export_conversation_txt():
    """Export conversation history as plain text"""
    try:
        lines = [
            "AI Learning Assistant - Conversation Export",
            f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Messages: {len(st.session_state.messages)}",
            "=" * 80,
            ""
        ]

        for i, msg in enumerate(st.session_state.messages, 1):
            role = "You" if msg["role"] == "user" else "Assistant"
            lines.append(f"Message {i} - {role}:")
            lines.append("-" * 40)
            lines.append(msg["content"])

            if "sources" in msg:
                lines.append("\nSources:")
                lines.append(msg["sources"])

            lines.append("\n" + "=" * 80 + "\n")

        return "\n".join(lines)
    except Exception as e:
        st.error(f"Error exporting to text: {str(e)}")
        return None

def main():
    # Header
    st.title("🎓 AI Learning Assistant")
    st.markdown("### Your intelligent guide to instructional design and eLearning")

    # Sidebar
    with st.sidebar:
        st.header("📚 About")
        st.markdown("""
        This AI-powered learning assistant uses Retrieval-Augmented Generation (RAG)
        to answer questions about:
        - Instructional Design (ADDIE model)
        - eLearning Best Practices
        - Learning Theories
        - Narrative Learning Design
        """)

        st.divider()

        # Check API key
        api_key = get_api_key()
        if not api_key or api_key == "your_openai_api_key_here":
            st.error("⚠️ OpenAI API key not configured!")
            if hasattr(st, 'secrets'):
                st.info("Please configure OPENAI_API_KEY in Streamlit Cloud secrets")
            else:
                st.info("Please add your API key to the .env file")
            st.stop()
        else:
            st.success("✅ API key configured")

        # Initialize button
        if st.button("🔄 Initialize Knowledge Base", use_container_width=True):
            with st.spinner("Loading documents and creating vector store..."):
                documents = load_documents()
                if documents:
                    st.session_state.vectorstore = create_vectorstore(documents)
                    if st.session_state.vectorstore:
                        st.session_state.conversation = initialize_conversation(st.session_state.vectorstore)
                        st.success(f"✅ Loaded {len(documents)} documents!")
                else:
                    st.error("No documents found in knowledge_base folder")

        st.divider()

        # Clear conversation button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            if st.session_state.vectorstore:
                st.session_state.conversation = initialize_conversation(st.session_state.vectorstore)
            st.rerun()

        st.divider()

        # Export conversation
        st.markdown("**💾 Export Conversation**")
        if len(st.session_state.messages) > 0:
            col1, col2 = st.columns(2)

            with col1:
                txt_export = export_conversation_txt()
                if txt_export:
                    st.download_button(
                        label="📄 TXT",
                        data=txt_export,
                        file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

            with col2:
                json_export = export_conversation_json()
                if json_export:
                    st.download_button(
                        label="📋 JSON",
                        data=json_export,
                        file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json",
                        use_container_width=True
                    )
        else:
            st.info("Start a conversation to enable export")

        st.divider()
        st.markdown("**📊 Statistics**")
        st.metric("Messages", len(st.session_state.messages))

    # Main chat interface
    if st.session_state.conversation is None:
        st.info("👆 Click 'Initialize Knowledge Base' in the sidebar to get started!")
        st.markdown("""
        ### How to use:
        1. Click the **Initialize Knowledge Base** button in the sidebar
        2. Wait for the documents to load
        3. Start asking questions about instructional design, eLearning, or learning theories!

        ### Example questions:
        - What is the ADDIE model?
        - What are best practices for eLearning design?
        - Explain constructivism in learning theory
        - How do adults learn differently?
        """)
    else:
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "sources" in message:
                    with st.expander("📄 View Sources"):
                        st.markdown(message["sources"])

        # Chat input
        if prompt := st.chat_input("Ask a question about learning and instructional design..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        # Validate conversation is initialized
                        if not st.session_state.conversation:
                            error_msg = "❌ Conversation not initialized. Please initialize the knowledge base first."
                            st.error(error_msg)
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": error_msg
                            })
                            return

                        # Generate response
                        response = st.session_state.conversation({
                            "question": prompt
                        })

                        answer = response.get("answer", "No answer generated")
                        source_documents = response.get("source_documents", [])

                        # Display answer
                        st.markdown(answer)

                        # Display sources
                        if source_documents:
                            sources_text = format_sources(source_documents)
                            with st.expander("📄 View Sources"):
                                st.markdown(sources_text)

                            # Add to messages with sources
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": answer,
                                "sources": sources_text
                            })
                        else:
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": answer
                            })

                    except KeyError as e:
                        error_msg = f"❌ Response format error: Missing key {str(e)}"
                        st.error(error_msg)
                        st.info("The AI model returned an unexpected response format")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })
                    except Exception as e:
                        error_msg = f"❌ Error generating response: {str(e)}"
                        st.error(error_msg)

                        # Provide helpful hints based on error type
                        error_str = str(e).lower()
                        if "api key" in error_str or "authentication" in error_str:
                            st.info("💡 Check your OpenAI API key in the .env file")
                        elif "rate limit" in error_str:
                            st.info("💡 You've hit the OpenAI rate limit. Please wait a moment and try again.")
                        elif "timeout" in error_str:
                            st.info("💡 The request timed out. Please try again.")
                        else:
                            st.info("💡 Please try rephrasing your question or check the application logs")

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })

if __name__ == "__main__":
    main()
