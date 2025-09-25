#!/bin/bash

# GitHub Pages Deployment Script for Location API Business Manual

echo "🚀 GitHub Pages Deployment Script"
echo "=================================="

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Virtual environment not detected."
    echo "Activating virtual environment..."
    if [[ -f "venv/bin/activate" ]]; then
        source venv/bin/activate
        echo "✓ Virtual environment activated"
    else
        echo "❌ Virtual environment not found. Run setup first!"
        exit 1
    fi
else
    echo "✓ Virtual environment already active"
fi

# Check if repository info is updated
if grep -q "YOUR-GITHUB" mkdocs.yml; then
    echo ""
    echo "⚠️  IMPORTANT: Update your repository information!"
    echo "Edit mkdocs.yml and replace:"
    echo "  - YOUR-GITHUB-USERNAME with your actual GitHub username"
    echo "  - YOUR-REPO-NAME with your actual repository name"
    echo ""
    read -p "Have you updated the repository URLs? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Please update mkdocs.yml first, then run this script again."
        exit 1
    fi
fi

# Test local build
echo ""
echo "🔧 Testing local build..."
if mkdocs build --quiet; then
    echo "✓ Local build successful"
else
    echo "❌ Local build failed. Fix errors before deploying."
    exit 1
fi

# Choose deployment method
echo ""
echo "Select deployment method:"
echo "1) Automatic (GitHub Actions) - Recommended"
echo "2) Manual (Direct deployment)"
read -p "Choice (1 or 2): " -n 1 -r
echo

case $REPLY in
    1)
        echo ""
        echo "📋 GitHub Actions Deployment Steps:"
        echo "1. Commit and push your changes to GitHub"
        echo "2. GitHub Actions will automatically deploy"
        echo "3. Check the Actions tab for progress"
        echo ""
        
        # Check if there are uncommitted changes
        if [[ -n $(git status --porcelain) ]]; then
            echo "📝 Uncommitted changes detected. Committing..."
            git add .
            git commit -m "Initial commit: Location API Business Manual with GitHub Actions deployment"
            echo "✓ Changes committed"
        else
            echo "✓ No uncommitted changes"
        fi
        
        echo ""
        echo "Next steps:"
        echo "1. Create repository on GitHub"
        echo "2. Run: git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git"
        echo "3. Run: git push -u origin main"
        echo "4. Enable GitHub Pages in repository settings (Source: gh-pages branch)"
        echo ""
        echo "Your site will be available at:"
        echo "https://YOUR-USERNAME.github.io/YOUR-REPO/"
        ;;
    2)
        echo ""
        echo "🔄 Manual deployment using mkdocs gh-deploy..."
        
        # Check if remote origin exists
        if git remote get-url origin >/dev/null 2>&1; then
            echo "✓ Git remote origin configured"
            
            # Deploy
            if mkdocs gh-deploy; then
                echo ""
                echo "🎉 Deployment successful!"
                echo ""
                echo "Your site should be available at:"
                REPO_URL=$(git remote get-url origin)
                USERNAME=$(echo $REPO_URL | sed 's/.*github.com[:\/]\([^\/]*\).*/\1/')
                REPONAME=$(echo $REPO_URL | sed 's/.*\/\([^\/]*\)\.git/\1/' | sed 's/.*\/\([^\/]*\)$/\1/')
                echo "https://$USERNAME.github.io/$REPONAME/"
                echo ""
                echo "Note: It may take a few minutes for GitHub Pages to update."
            else
                echo "❌ Deployment failed. Check the error messages above."
                exit 1
            fi
        else
            echo "❌ No git remote origin configured."
            echo "Please add your GitHub repository as origin first:"
            echo "git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git"
            exit 1
        fi
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "📚 For more information, see DEPLOYMENT.md"