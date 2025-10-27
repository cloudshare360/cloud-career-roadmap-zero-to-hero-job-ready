#!/bin/bash

# Cloud Career Roadmap Setup Script
# This script sets up the environment for conversation analysis

echo "🚀 Setting up Cloud Career Roadmap Analysis Environment..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3."
    exit 1
fi

echo "✅ Python 3 found"

# Make the analysis script executable
chmod +x conversations/analyze_conversations.py

echo "✅ Made analysis script executable"

# Check current directory structure
echo "📁 Current project structure:"
find . -type f -name "*.md" -o -name "*.py" | head -10

echo ""
echo "🎯 Next Steps:"
echo "1. Follow the instructions in conversations/EXTRACTION_GUIDE.md"
echo "2. Extract your AI conversations from Qwen chat"
echo "3. Save them using the template in conversations/conversation_template.md"
echo "4. Run: cd conversations && python3 analyze_conversations.py"
echo "5. Review your personalized roadmap!"

echo ""
echo "📝 Quick Start:"
echo "   cd conversations"
echo "   cp conversation_template.md conversation_01_your_topic.md"
echo "   # Edit the file with your conversation content"
echo "   python3 analyze_conversations.py"

echo ""
echo "✨ Setup complete! Ready to analyze your AI conversations."