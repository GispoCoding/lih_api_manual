# Location API Business Manual - Development Setup

This repository contains the source code for the Location API Business Manual website, built with MkDocs and the Material theme.

## Prerequisites

- **Python 3.8+** (recommended: Python 3.10 or newer)
- **Git** for version control

## Development Environment Setup

We **strongly recommend** using a Python virtual environment to avoid conflicts with system packages and ensure consistent dependencies across all team members.

### Option 1: Using Python venv (Recommended)

#### Linux/macOS
```bash
# Clone the repository
git clone <repository-url>
cd lih_api_manual

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Windows (PowerShell)
```powershell
# Clone the repository
git clone <repository-url>
cd lih_api_manual

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### Windows (Command Prompt)
```cmd
# Clone the repository
git clone <repository-url>
cd lih_api_manual

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```
## Quick Start

After setting up your virtual environment:

```bash
# Serve the site locally (with auto-reload)
mkdocs serve

# Open your browser to http://127.0.0.1:8000
```

## Building and Deployment

```bash
# Build static site
mkdocs build

# Deploy to GitHub Pages (requires proper repository setup)
mkdocs gh-deploy
```

## Project Structure

```
lih_api_manual/
├── docs/                   # Documentation source files
│   ├── index.md           # Homepage
│   ├── strategy/          # API Strategy section
│   ├── legal/             # Legal frameworks
│   ├── compliance/        # Security & compliance
│   ├── advanced/          # Advanced technologies
│   ├── lifecycle/         # API lifecycle management
│   ├── build/             # Technical implementation
│   ├── usecases/          # Market examples
│   ├── stylesheets/       # Custom CSS
│   │   └── extra.css     # Site customizations
│   └── glossary.md        # Glossary & resources
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Contributing

1. **Always use the virtual environment** when working on this project
2. **Activate your environment** before running any MkDocs commands
3. **Test locally** with `mkdocs serve` before committing changes
4. **Update requirements.txt** if you add new dependencies

### Adding New Content

1. Create or edit Markdown files in the `docs/` directory
2. Update navigation in `mkdocs.yml` if adding new pages
3. Test with `mkdocs serve`
4. Commit and push changes

### Custom Styling

- Edit `docs/stylesheets/extra.css` for custom styling
- The CSS is automatically included via `mkdocs.yml` configuration

## Troubleshooting

### Virtual Environment Issues

**Problem**: `source venv/bin/activate` not working on Windows
**Solution**: Use the Windows-specific activation script (see setup instructions above)

**Problem**: Permission denied on venv activation
**Solution**: On Windows PowerShell, you might need to run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem**: Python command not found
**Solution**: 
- Linux/Mac: Try `python3` instead of `python`
- Windows: Ensure Python is in your PATH, or use Python Launcher: `py -m venv venv`

### MkDocs Issues

**Problem**: `mkdocs: command not found`
**Solution**: Ensure your virtual environment is activated and requirements are installed

**Problem**: Site not updating when editing files
**Solution**: Check that `mkdocs serve` is running and refresh your browser

**Problem**: Theme not loading properly
**Solution**: Verify `mkdocs-material` is installed: `pip list | grep mkdocs-material`

## Team Workflows

### Daily Development
```bash
# Start of day
cd lih_api_manual
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Work on content...
mkdocs serve  # Keep this running while editing

# End of day - deactivate environment
deactivate
```

### Before Committing
```bash
# Test build
mkdocs build

# Check for any errors
# Commit if everything looks good
git add .
git commit -m "Your descriptive commit message"
git push
```

## Deployment to GitHub Pages

### Quick Deployment (fist time)
```bash
# Automated deployment script
./deploy.sh
```

### Manual Steps
1. **Update repository URLs** in `mkdocs.yml`
2. **Create GitHub repository** and add as remote
3. **Deploy**: `mkdocs gh-deploy` (manual) or push to trigger GitHub Actions

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for detailed instructions.

