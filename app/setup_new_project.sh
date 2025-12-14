#!/bin/bash
# Script to help set up a new project from this template
# Usage: ./setup_new_project.sh <project-name>

set -e

PROJECT_NAME="${1:-my-ai-project}"

if [ -z "$1" ]; then
    echo "Usage: $0 <project-name>"
    echo "Example: $0 sentiment-analysis"
    exit 1
fi

echo "🚀 Setting up new project: $PROJECT_NAME"
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Must run this script from the app/ directory"
    exit 1
fi

# Update app.py with project name
echo "📝 Updating app.py..."
sed -i.bak "s/AI Up-Skilling Flask App/$PROJECT_NAME/g" app.py
sed -i.bak "s/Welcome to AI Up-Skilling Flask App/Welcome to $PROJECT_NAME/g" app.py
rm -f app.py.bak

# Update README.md
echo "📝 Updating README.md..."
sed -i.bak "s/AI Up-Skilling Flask Application/$PROJECT_NAME/g" README.md
sed -i.bak "s/for AI\/ML upskilling programs/for $PROJECT_NAME/g" README.md
rm -f README.md.bak

# Create .env from example if it doesn't exist
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo "📝 Creating .env from .env.example..."
    cp .env.example .env
    echo "⚠️  Remember to update .env with your actual values!"
fi

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: $PROJECT_NAME setup from template"
    echo "⚠️  Remember to add your remote: git remote add origin <your-repo-url>"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Review and update README.md with project-specific details"
echo "  2. Update requirements.txt with your needed libraries"
echo "  3. Edit .env with your configuration (if needed)"
echo "  4. Run 'make install' to set up the environment"
echo "  5. Run 'make run' to test the application"
echo ""
echo "For more information, see TEMPLATE_USAGE.md"

