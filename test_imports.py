#!/usr/bin/env python3
"""Test script to verify all imports work correctly"""

import sys

def test_imports():
    """Test that all required modules can be imported"""
    try:
        print("Testing imports...")

        import streamlit
        print("✓ streamlit")

        import dotenv
        print("✓ python-dotenv")

        from langchain.text_splitter import RecursiveCharacterTextSplitter
        print("✓ langchain text_splitter")

        from langchain_community.document_loaders import DirectoryLoader, TextLoader
        print("✓ langchain_community document_loaders")

        from langchain_openai import OpenAIEmbeddings, ChatOpenAI
        print("✓ langchain_openai")

        from langchain_community.vectorstores import Chroma
        print("✓ langchain_community vectorstores")

        from langchain.chains import ConversationalRetrievalChain
        print("✓ langchain chains")

        from langchain.memory import ConversationBufferMemory
        print("✓ langchain memory")

        from langchain.prompts import PromptTemplate
        print("✓ langchain prompts")

        import chromadb
        print("✓ chromadb")

        import openai
        print("✓ openai")

        import tiktoken
        print("✓ tiktoken")

        print("\n✅ All imports successful!")
        return True

    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        return False

def check_project_structure():
    """Verify project structure"""
    import os

    print("\nChecking project structure...")

    files = [
        'learning_assistant.py',
        'requirements.txt',
        '.env',
        'README.md',
        'knowledge_base/',
        'knowledge_base/instructional_design.txt',
        'knowledge_base/elearning_best_practices.txt',
        'knowledge_base/learning_theories.txt'
    ]

    all_exist = True
    for file in files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False

    return all_exist

if __name__ == "__main__":
    imports_ok = test_imports()
    structure_ok = check_project_structure()

    if imports_ok and structure_ok:
        print("\n🎉 All tests passed! The project is ready to run.")
        print("\nNext steps:")
        print("1. Edit .env file and add your OpenAI API key")
        print("2. Run: streamlit run learning_assistant.py")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        sys.exit(1)
