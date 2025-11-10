# Deployment Guide: AI Learning Assistant to Streamlit Cloud

This guide walks you through deploying your AI Learning Assistant to Streamlit Cloud so you can share a public link with anyone.

## 📋 Prerequisites

Before you begin, ensure you have:
- [x] A GitHub account ([sign up here](https://github.com/join))
- [x] Git installed on your computer
- [x] Your OpenAI API key ready
- [x] A Streamlit Cloud account (free - we'll set this up)

## 🚀 Deployment Steps

### Step 1: Initialize Git Repository

First, we'll create a local Git repository for your project.

```bash
cd /Users/gingerninja/Documents/learningassistant

# Initialize git repository
git init

# Add all files (gitignore will protect sensitive data)
git add .

# Create first commit
git commit -m "Initial commit: AI Learning Assistant v2.0

- RAG-powered chatbot with LangChain and OpenAI
- 4 comprehensive knowledge base documents
- Blue & white UI theme
- Conversation export functionality
- Enhanced error handling"
```

### Step 2: Create GitHub Repository

1. **Go to GitHub**
   - Visit https://github.com
   - Log in to your account

2. **Create New Repository**
   - Click the "+" icon in top-right corner
   - Select "New repository"

3. **Repository Settings**
   - **Repository name**: `ai-learning-assistant` (or your preferred name)
   - **Description**: "AI-powered learning assistant using RAG for instructional design questions"
   - **Visibility**: Choose **Public** (required for free Streamlit Cloud)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

4. **Copy the Repository URL**
   - You'll see a URL like: `https://github.com/YOUR_USERNAME/ai-learning-assistant.git`
   - Keep this handy for the next step

### Step 3: Push Code to GitHub

```bash
# Add GitHub as remote repository
git remote add origin https://github.com/YOUR_USERNAME/ai-learning-assistant.git

# Push code to GitHub
git branch -M main
git push -u origin main
```

**Verify**: Go to your GitHub repository URL - you should see all your files except `.env` and `chroma_db/` (protected by .gitignore)

### Step 4: Sign Up for Streamlit Cloud

1. **Visit Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "Sign up" or "Continue with GitHub"

2. **Connect GitHub Account**
   - Authorize Streamlit to access your GitHub account
   - Grant permission to access your repositories

3. **Confirm Email** (if required)
   - Check your email for verification link
   - Click to verify your account

### Step 5: Deploy Your App

1. **Create New App**
   - Click "New app" button on Streamlit Cloud dashboard
   - Or go directly to: https://share.streamlit.io/deploy

2. **Configure Deployment**

   Fill in these fields:

   - **Repository**: Select `YOUR_USERNAME/ai-learning-assistant`
   - **Branch**: `main`
   - **Main file path**: `learning_assistant.py`
   - **App URL** (optional): Choose a custom subdomain like `my-learning-assistant`

3. **Advanced Settings** (Click "Advanced settings")

   - **Python version**: `3.11` (or `3.10`, `3.9`)
   - Leave other settings as default

4. **Click "Deploy"**
   - Initial deployment takes 2-5 minutes
   - You'll see a "Deploying..." status

### Step 6: Configure Secrets (API Key)

**IMPORTANT**: Do this while the app is deploying or immediately after.

1. **Open App Settings**
   - In your app's Streamlit Cloud page
   - Click the menu icon (⋮) in the bottom right
   - Select "Settings"

2. **Add Secrets**
   - Go to the "Secrets" tab
   - Paste this TOML format:

   ```toml
   OPENAI_API_KEY = "sk-proj-YOUR-ACTUAL-API-KEY-HERE"
   ```

   - **Replace** `sk-proj-YOUR-ACTUAL-API-KEY-HERE` with your real OpenAI API key
   - Click "Save"

3. **Reboot App** (if it finished deploying)
   - The app will automatically restart
   - Takes 10-30 seconds

### Step 7: Test Your Deployed App

1. **Access Your App**
   - Your app URL will be: `https://YOUR-APP-NAME.streamlit.app`
   - Or: `https://share.streamlit.io/YOUR_USERNAME/ai-learning-assistant/main/learning_assistant.py`

2. **Verify Functionality**
   - [ ] Check that the blue & white theme loads
   - [ ] Confirm "✅ API key configured" shows in sidebar
   - [ ] Click "Initialize Knowledge Base"
   - [ ] Wait for "✅ Loaded 4 documents!"
   - [ ] Ask a test question: "What is the ADDIE model?"
   - [ ] Verify response with sources appears
   - [ ] Test export functionality (TXT/JSON)

3. **Test on Different Devices**
   - Desktop browser
   - Mobile browser
   - Different browsers (Chrome, Firefox, Safari)

## 🎉 Your App is Live!

Your AI Learning Assistant is now publicly accessible at:
`https://YOUR-APP-NAME.streamlit.app`

Share this link with anyone - no account or API key required for users!

## 🔄 Updating Your Deployed App

When you make changes to your code:

```bash
# Make your changes to files
# Then commit and push:

git add .
git commit -m "Description of changes"
git push origin main
```

Streamlit Cloud will automatically detect changes and redeploy (takes 2-3 minutes).

## ⚙️ Managing Your Deployment

### View Logs
- Click "Manage app" on your app page
- View "Logs" tab to debug issues

### Monitor Usage
- Check "Analytics" for visitor statistics
- Monitor resource usage

### Sleep Mode
- Free apps sleep after 7 days of inactivity
- App "wakes up" when someone visits (takes ~30 seconds)
- Upgrade to Streamlit Cloud Pro to prevent sleeping

### Update Secrets
- Go to app Settings > Secrets
- Update OPENAI_API_KEY anytime
- Click "Save" and app will restart

## 🔒 Security Best Practices

### API Key Security
- ✅ **Never commit** `.env` file to GitHub
- ✅ **Use Streamlit secrets** for API keys
- ✅ **Monitor usage** at https://platform.openai.com/usage
- ✅ **Set spending limits** in OpenAI dashboard
- ✅ **Rotate keys** regularly

### Repository Security
- ✅ Confirm `.env` is in `.gitignore`
- ✅ Check GitHub repo doesn't contain API key
- ✅ Review commit history if you accidentally committed secrets
- ❌ Never share secrets.toml file

## 💰 Cost Considerations

### Streamlit Cloud Costs
- **Free Tier**:
  - 1 public app
  - Unlimited viewers
  - Sleep after 7 days inactivity
  - Community support
  - **Cost: $0/month**

- **Pro Tier** ($20/month):
  - 3 private apps
  - No sleep mode
  - Priority support
  - More resources

### OpenAI API Costs
Your app uses OpenAI API, costs paid by you:
- **Knowledge base initialization**: $0.05-0.10 (one-time per app reboot)
- **Per user query**: ~$0.007 (less than 1 cent)
- **100 queries**: ~$0.70
- **1,000 queries**: ~$7.00

**Important**: Since users don't need their own API key, all API costs are charged to your account.

### Cost Management Tips
1. **Set Spending Limits**
   - Go to https://platform.openai.com/account/billing/limits
   - Set monthly limit (e.g., $10, $20)
   - Get notifications at 75%, 90%

2. **Monitor Usage**
   - Check https://platform.openai.com/usage daily
   - Watch for unexpected spikes
   - Use Streamlit Analytics to track visitors

3. **Rate Limiting** (optional)
   - Add usage tracking in code
   - Limit queries per user/IP
   - Add CAPTCHA for public apps

4. **Private Deployment** (alternative)
   - Deploy as private app (requires Streamlit Pro)
   - Share only with specific users
   - Reduces public traffic

## 🐛 Troubleshooting

### App Won't Deploy

**Error: "Could not find requirements.txt"**
- Solution: Ensure requirements.txt is in root directory
- Check capitalization

**Error: "Module not found"**
- Solution: Verify all packages in requirements.txt
- Check Python version compatibility

**Error: "Port already in use"**
- Solution: Streamlit Cloud manages ports automatically
- Check there's no hardcoded port in code

### API Key Issues

**Error: "OpenAI API key not configured"**
- Solution: Check Secrets configuration
- Ensure format is: `OPENAI_API_KEY = "sk-..."`
- No quotes around key value in TOML
- Reboot app after adding secrets

**Error: "Invalid API key"**
- Solution: Verify key is correct
- Check for extra spaces or line breaks
- Generate new key if needed

### Knowledge Base Not Loading

**Error: "No documents found"**
- Solution: Verify knowledge_base/ folder exists in repo
- Check .gitignore isn't excluding knowledge_base/
- Verify .txt files are present

**Slow Loading**
- Solution: First load creates embeddings (30-60 seconds)
- Subsequent loads faster with cache
- This is normal behavior

### App is Sleeping

**Issue**: "This app is sleeping..."
- Solution: App sleeps after 7 days inactivity (free tier)
- Click to wake it up (takes 30 seconds)
- Upgrade to Pro to prevent sleeping

## 📞 Support

### Streamlit Cloud Support
- Documentation: https://docs.streamlit.io/streamlit-community-cloud
- Community forum: https://discuss.streamlit.io
- Status page: https://streamlitstatus.com

### GitHub Support
- GitHub Docs: https://docs.github.com
- GitHub Community: https://github.community

### OpenAI Support
- API Docs: https://platform.openai.com/docs
- Community: https://community.openai.com
- Status: https://status.openai.com

## 🎯 Next Steps

After successful deployment:

1. **Share Your Link**
   - Post on social media
   - Share with colleagues
   - Add to your portfolio
   - Include in email signature

2. **Customize Further**
   - Add your branding
   - Customize knowledge base
   - Add analytics
   - Implement user feedback

3. **Monitor Performance**
   - Check logs regularly
   - Monitor API usage
   - Review user analytics
   - Optimize based on usage patterns

4. **Iterate and Improve**
   - Add new documents
   - Improve UI/UX
   - Optimize performance
   - Fix reported issues

## 🏆 Congratulations!

You've successfully deployed your AI Learning Assistant to the cloud!

Your app is now accessible to anyone in the world at:
`https://YOUR-APP-NAME.streamlit.app`

Happy sharing! 🎉
