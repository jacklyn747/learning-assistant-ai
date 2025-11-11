#!/bin/bash

# AI Learning Assistant - GitHub Push Script
#
# INSTRUCTIONS:
# 1. Create a GitHub repository at https://github.com/new
#    - Name: ai-learning-assistant
#    - Visibility: Public
#    - Don't add README, .gitignore, or license
#
# 2. Replace YOUR_USERNAME below with your actual GitHub username
# 3. Run this script: bash PUSH_TO_GITHUB.sh

# ⚠️  EDIT THIS LINE - Replace YOUR_USERNAME with your GitHub username
GITHUB_USERNAME="YOUR_USERNAME"

# Verify username is set
if [ "$GITHUB_USERNAME" = "YOUR_USERNAME" ]; then
    echo "❌ Error: Please edit this script and set your GitHub username!"
    echo "   Open PUSH_TO_GITHUB.sh and change YOUR_USERNAME to your actual username"
    exit 1
fi

echo "🚀 Pushing AI Learning Assistant to GitHub..."
echo "   Repository: https://github.com/$GITHUB_USERNAME/ai-learning-assistant"
echo ""

# Add remote repository
git remote add origin "https://github.com/$GITHUB_USERNAME/ai-learning-assistant.git"

# Rename branch to main (if not already)
git branch -M main

# Push to GitHub
echo "📤 Pushing code to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Code pushed to GitHub"
    echo ""
    echo "🌐 View your repository at:"
    echo "   https://github.com/$GITHUB_USERNAME/ai-learning-assistant"
    echo ""
    echo "📋 Next: Deploy to Streamlit Cloud"
    echo "   1. Go to: https://share.streamlit.io"
    echo "   2. Sign in with GitHub"
    echo "   3. Click 'New app'"
    echo "   4. Select your repository"
    echo ""
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo "   - Repository doesn't exist on GitHub"
    echo "   - Username is incorrect"
    echo "   - Need to authenticate (follow GitHub prompts)"
    echo ""
fi
