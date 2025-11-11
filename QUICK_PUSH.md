# Quick Push to GitHub

## Step 1: Create Repository on GitHub

**Open this link:** https://github.com/new

Fill in:
- Repository name: `learning-assistant-ai`
- Description: `AI-powered learning assistant using RAG`
- Visibility: **Public** ✓
- DO NOT check: README, .gitignore, or license

Click **"Create repository"**

---

## Step 2: Push Your Code

After creating the repository, run these commands (replace `YOUR_USERNAME` with your actual GitHub username):

```bash
# Add the GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/learning-assistant-ai.git

# Ensure you're on the main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## What Happens Next

After pushing:
1. GitHub may ask you to authenticate (follow the prompts)
2. All your code will be uploaded to GitHub
3. You'll get a confirmation message
4. Your repository will be live at: `https://github.com/YOUR_USERNAME/learning-assistant-ai`

---

## Quick Copy-Paste Version

If your GitHub username is (for example) `johndoe`, run:

```bash
git remote add origin https://github.com/johndoe/learning-assistant-ai.git
git branch -M main
git push -u origin main
```

Just replace `johndoe` with your actual username!
