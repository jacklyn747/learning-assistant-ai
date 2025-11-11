#!/bin/bash

# GitHub Repository Setup Script
# This script will help you push to GitHub after creating the repository

echo "🚀 AI Learning Assistant - GitHub Setup"
echo "========================================"
echo ""

# Repository details
REPO_NAME="learning-assistant-ai"
GITHUB_USERNAME=""

echo "📝 Step 1: We need your GitHub username"
echo "----------------------------------------"
read -p "Enter your GitHub username: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Error: GitHub username is required"
    exit 1
fi

REPO_URL="https://github.com/$GITHUB_USERNAME/$REPO_NAME"

echo ""
echo "✅ Configuration:"
echo "   Repository name: $REPO_NAME"
echo "   Your username: $GITHUB_USERNAME"
echo "   Repository URL: $REPO_URL"
echo ""

# Check if remote already exists
if git remote get-url origin &> /dev/null; then
    echo "⚠️  Git remote 'origin' already exists. Removing it..."
    git remote remove origin
fi

# Instructions for creating repository
echo "📋 MANUAL STEP REQUIRED:"
echo "========================"
echo ""
echo "1. Open this URL in your browser:"
echo "   👉 https://github.com/new"
echo ""
echo "2. Fill in the form:"
echo "   - Repository name: $REPO_NAME"
echo "   - Description: AI-powered learning assistant using RAG"
echo "   - Visibility: ⚪ Public"
echo "   - ❌ DO NOT check: Add README, .gitignore, or license"
echo ""
echo "3. Click 'Create repository'"
echo ""
read -p "Press ENTER after you've created the repository on GitHub... " -r

echo ""
echo "📤 Pushing code to GitHub..."
echo "----------------------------"

# Add remote
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

# Ensure on main branch
git branch -M main

# Push to GitHub
echo "Pushing to: $REPO_URL"
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Your code is now on GitHub!"
    echo "========================================"
    echo ""
    echo "🌐 View your repository:"
    echo "   $REPO_URL"
    echo ""
    echo "📋 Next Steps:"
    echo "   1. Go to: https://share.streamlit.io"
    echo "   2. Sign in with GitHub"
    echo "   3. Click 'New app'"
    echo "   4. Select repository: $GITHUB_USERNAME/$REPO_NAME"
    echo "   5. Branch: main"
    echo "   6. Main file: learning_assistant.py"
    echo "   7. Deploy!"
    echo ""
else
    echo ""
    echo "❌ Push failed!"
    echo "=============="
    echo ""
    echo "Common issues:"
    echo "  - Repository doesn't exist yet (create it at https://github.com/new)"
    echo "  - Username is incorrect"
    echo "  - Need to authenticate (GitHub will prompt)"
    echo ""
    echo "Try running this script again after fixing the issue."
    exit 1
fi
