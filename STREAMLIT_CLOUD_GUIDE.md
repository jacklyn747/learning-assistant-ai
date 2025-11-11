# Streamlit Cloud Deployment Guide - Step by Step

This is your visual walkthrough for deploying to Streamlit Cloud after pushing to GitHub.

## 📋 Prerequisites Checklist

Before starting, ensure you have:
- [x] Code pushed to GitHub
- [x] GitHub repository is PUBLIC
- [ ] Your OpenAI API key ready (you'll need this!)

---

## 🚀 Part 1: Sign Up for Streamlit Cloud

### Step 1: Visit Streamlit Cloud

Go to: **https://share.streamlit.io**

### Step 2: Sign Up with GitHub

You'll see a landing page with options:

```
┌─────────────────────────────────────┐
│    Welcome to Streamlit Cloud!     │
│                                      │
│  [Continue with GitHub]  ← Click    │
│  [Continue with Google]             │
│  [Sign in with email]               │
└─────────────────────────────────────┘
```

**Click "Continue with GitHub"**

### Step 3: Authorize Streamlit

GitHub will ask for permissions:

```
┌───────────────────────────────────────┐
│ Streamlit wants to:                  │
│ ✓ Read your profile                  │
│ ✓ Access your repositories           │
│ ✓ Read repository metadata           │
│                                       │
│  [Authorize streamlit]  ← Click      │
│  [Cancel]                            │
└───────────────────────────────────────┘
```

**Click "Authorize streamlit"**

### Step 4: Complete Registration

- You may need to verify your email
- Check your inbox and click the verification link
- Return to https://share.streamlit.io

---

## 🎯 Part 2: Deploy Your App

### Step 1: Access the Dashboard

After logging in, you'll see your Streamlit Cloud dashboard:

```
┌─────────────────────────────────────────┐
│  Streamlit Cloud                        │
│  ────────────────                       │
│                                          │
│  Your apps         [New app +]  ← Click │
│  ──────────                             │
│  No apps yet                            │
│                                          │
└─────────────────────────────────────────┘
```

**Click "New app"** button (top right)

### Step 2: Configure Deployment

You'll see a deployment form:

```
┌─────────────────────────────────────────────┐
│  Deploy an app                              │
│  ──────────────                             │
│                                              │
│  Repository *                               │
│  [YOUR_USERNAME/ai-learning-assistant ▼]    │
│                                              │
│  Branch *                                   │
│  [main ▼]                                   │
│                                              │
│  Main file path *                           │
│  [learning_assistant.py]                    │
│                                              │
│  App URL (optional)                         │
│  [my-learning-assistant]                    │
│  .streamlit.app                             │
│                                              │
│  ▼ Advanced settings                        │
│                                              │
│  [Deploy!]                                  │
└─────────────────────────────────────────────┘
```

**Fill in:**
- **Repository**: Select `YOUR_USERNAME/ai-learning-assistant`
- **Branch**: `main`
- **Main file path**: `learning_assistant.py`
- **App URL**: Choose something memorable (e.g., `my-learning-assistant`)

### Step 3: Advanced Settings (Optional)

Click "▼ Advanced settings" if you want to customize:

```
┌─────────────────────────────────────────┐
│  Python version:  [3.11 ▼]             │
│  Secrets:         [Add secrets]         │
└─────────────────────────────────────────┘
```

- **Python version**: 3.11 (recommended) or 3.10
- **Secrets**: We'll add this after deployment

### Step 4: Deploy!

**Click the "Deploy!" button**

You'll see a deployment screen:

```
┌─────────────────────────────────────────┐
│  🚀 Deploying your app...               │
│                                          │
│  ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ 50%             │
│                                          │
│  Installing dependencies...             │
│  - Installing streamlit==1.31.0         │
│  - Installing langchain==0.1.9          │
│  - Installing chromadb==0.4.22          │
│  ...                                    │
│                                          │
│  This usually takes 2-5 minutes         │
└─────────────────────────────────────────┘
```

**Wait for deployment** (2-5 minutes)

---

## 🔑 Part 3: Add API Key Secret

**CRITICAL STEP** - Your app won't work without this!

### Step 1: Access App Settings

While the app is deploying (or after), you'll see your app page.

Look for the **hamburger menu (⋮)** in the bottom right corner:

```
                                    ┌──────────────┐
                                    │ ⋮ Settings   │
                                    │   Reboot app │
                                    │   Delete app │
                                    │   Manage     │
                                    └──────────────┘
```

**Click the menu icon (⋮)**
**Select "Settings"**

### Step 2: Navigate to Secrets

You'll see the Settings panel:

```
┌─────────────────────────────────────────┐
│  Settings                               │
│  ────────                               │
│  │ General                              │
│  │ Sharing                              │
│  │ Resources                            │
│  │ Secrets      ← Click this           │
│  │ Domains                              │
└─────────────────────────────────────────┘
```

**Click on "Secrets"** tab

### Step 3: Add Your OpenAI API Key

You'll see a text editor:

```
┌─────────────────────────────────────────────────┐
│  Secrets                                        │
│  ────────                                       │
│  Secrets are encrypted and only available      │
│  to your app. Use TOML format.                 │
│                                                  │
│  ┌────────────────────────────────────────┐   │
│  │ # Paste your secrets here in TOML     │   │
│  │ # format (key = "value")               │   │
│  │                                         │   │
│  │ OPENAI_API_KEY = "sk-proj-..."        │   │
│  │                                         │   │
│  │                                         │   │
│  └────────────────────────────────────────┘   │
│                                                  │
│  [Save]                                         │
└─────────────────────────────────────────────────┘
```

**Paste exactly this (with YOUR actual API key):**

```toml
OPENAI_API_KEY = "sk-proj-YOUR-ACTUAL-API-KEY-HERE"
```

### Important Notes:

- Use TOML format: `KEY = "value"`
- Include the quotes around the API key
- No extra spaces or line breaks
- The key name must be exactly `OPENAI_API_KEY`

### Step 4: Save Secrets

**Click the "Save" button**

The app will automatically restart (takes 10-30 seconds)

---

## ✅ Part 4: Verify Deployment

### Step 1: Wait for App to Load

After saving secrets, the app will reload:

```
┌─────────────────────────────────────────┐
│  Your app is running!                   │
│  ────────────────────                   │
│  🌐 https://my-learning-assistant.      │
│     streamlit.app                       │
│                                          │
│  [Open app]                             │
└─────────────────────────────────────────┘
```

**Click "Open app"** or visit your URL

### Step 2: Check API Key Status

In the sidebar, you should see:

```
┌─────────────────────────┐
│ 📚 About                │
│                          │
│ ✅ API key configured   │ ← Look for this!
│                          │
│ [🔄 Initialize          │
│  Knowledge Base]         │
└─────────────────────────┘
```

✅ **SUCCESS**: If you see "✅ API key configured"

❌ **ERROR**: If you see "⚠️ OpenAI API key not configured"
   - Go back to Settings > Secrets
   - Check the format is correct
   - Make sure you clicked "Save"
   - Try rebooting the app

### Step 3: Initialize Knowledge Base

1. **Click "🔄 Initialize Knowledge Base"**
2. Wait 30-60 seconds
3. You should see: **"✅ Loaded 4 documents!"**

### Step 4: Test the App

Ask a test question:

```
Type: "What is the ADDIE model?"
Press Enter
```

You should get:
- A detailed response about the ADDIE model
- Source citations you can expand

---

## 🎉 Success! Your App is Live

Your AI Learning Assistant is now publicly accessible at:

```
https://your-app-name.streamlit.app
```

Share this link with anyone - they can use it without:
- Installing anything
- Having an API key
- Creating an account

---

## 📊 Managing Your App

### View Logs

To debug issues:

1. Go to your app on Streamlit Cloud
2. Click menu (⋮) > "Manage"
3. Click "Logs" tab
4. See real-time application logs

### Monitor Usage

1. Go to "Analytics" tab
2. See visitor count, usage patterns
3. Monitor resource consumption

### Reboot App

If something goes wrong:

1. Click menu (⋮)
2. Select "Reboot app"
3. Wait 30 seconds for restart

### Update Code

When you make changes:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Streamlit Cloud auto-detects changes and redeploys (2-3 minutes)

---

## 🔒 Security Reminders

✅ **Do:**
- Keep your API key secret
- Monitor OpenAI usage: https://platform.openai.com/usage
- Set spending limits in OpenAI dashboard
- Only share your app URL (not GitHub repo with secrets)

❌ **Don't:**
- Commit `.env` file to GitHub (already protected)
- Share your API key
- Forget to monitor costs
- Leave unlimited spending

---

## 💰 Cost Tracking

### Streamlit Cloud
- Free tier: $0/month
- 1 public app included
- Unlimited viewers

### OpenAI API
Your costs (charged per usage):
- Knowledge base init: ~$0.05 per deploy
- Per user query: ~$0.007 (< 1 cent)
- 100 queries: ~$0.70
- 1000 queries: ~$7.00

### Set Spending Limits

**IMPORTANT**: Do this before making your app public!

1. Go to: https://platform.openai.com/account/billing/limits
2. Set monthly limit (e.g., $10, $20, $50)
3. Set email notifications at 75%, 90%, 100%

---

## 🐛 Troubleshooting

### "App is sleeping"

**Cause**: Free apps sleep after 7 days of inactivity

**Solution**:
- Click "Wake up" button (takes 30 seconds)
- Or upgrade to Streamlit Pro ($20/month) to prevent sleeping

### "Invalid API key"

**Cause**: Wrong API key format or expired key

**Solution**:
1. Check format in Secrets: `OPENAI_API_KEY = "sk-..."`
2. Verify key at: https://platform.openai.com/api-keys
3. Generate new key if needed
4. Update in Streamlit Cloud secrets

### "No documents found"

**Cause**: Knowledge base folder missing or empty

**Solution**:
1. Check GitHub repo has `knowledge_base/` folder
2. Verify 4 `.txt` files are present
3. Check `.gitignore` isn't excluding them
4. Reboot app

### "Module not found"

**Cause**: Missing dependency or wrong Python version

**Solution**:
1. Check `requirements.txt` is in repo root
2. Verify all packages listed
3. Try changing Python version in Settings
4. Check deployment logs for specific error

---

## 📞 Get Help

- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Community Forum**: https://discuss.streamlit.io
- **Status Page**: https://streamlitstatus.com

---

## 🎯 What's Next?

After successful deployment:

1. **Share Your Link**
   - Social media
   - Professional networks
   - Portfolio

2. **Customize**
   - Add more documents
   - Customize branding
   - Add analytics

3. **Monitor**
   - Check logs daily
   - Review usage patterns
   - Monitor API costs

4. **Iterate**
   - Get user feedback
   - Fix issues
   - Add features

---

## Congratulations! 🎉

Your AI Learning Assistant is now live and accessible to the world!

**Your App URL:**
`https://your-app-name.streamlit.app`

Happy sharing! 🚀
