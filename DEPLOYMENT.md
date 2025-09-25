# GitHub Pages Deployment Guide

This guide will help you deploy the Location API Business Manual to GitHub Pages for free hosting.

## Prerequisites

- GitHub account
- Git configured with your GitHub credentials
- Repository pushed to GitHub

## Method 1: Automatic Deployment with GitHub Actions (Recommended)

### Step 1: Update mkdocs.yml with your repository details

Before pushing, update these placeholders in `mkdocs.yml`:

```yaml
site_url: https://YOUR-GITHUB-USERNAME.github.io/YOUR-REPO-NAME/
repo_name: 'YOUR-GITHUB-USERNAME/YOUR-REPO-NAME'
repo_url: https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME
```

### Step 2: Create GitHub Actions Workflow

Create `.github/workflows/ci.yml` in your repository:

```yaml
name: ci
on:
  push:
    branches:
      - master
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

### Step 3: Push to GitHub

1. Add and commit all files
2. Push to GitHub
3. GitHub Actions will automatically build and deploy

### Step 4: Configure GitHub Pages Settings

1. Go to your repository on GitHub
2. Settings → Pages
3. Source should be set to "Deploy from a branch"
4. Branch should be "gh-pages"
5. Folder should be "/ (root)"

## Method 2: Manual Deployment with MkDocs

### Prerequisites
- MkDocs installed locally
- Repository cloned and configured

### Steps

1. **Update repository URLs in mkdocs.yml**
2. **Build and deploy:**
   ```bash
   source venv/bin/activate
   mkdocs gh-deploy
   ```

This command will:
- Build your site
- Create/update the `gh-pages` branch
- Push the built site to GitHub

### Verification

After deployment, your site will be available at:
`https://YOUR-GITHUB-USERNAME.github.io/YOUR-REPO-NAME/`

## Method 3: Custom Domain (Optional)

If you have a custom domain:

1. Add a `CNAME` file in the `docs/` directory with your domain
2. Update `site_url` in `mkdocs.yml`
3. Configure your DNS to point to GitHub Pages

## Troubleshooting

### Common Issues

**Issue**: 404 error on GitHub Pages
**Solution**: Check that `gh-pages` branch exists and Pages is configured correctly

**Issue**: CSS/styling not loading
**Solution**: Verify `site_url` in `mkdocs.yml` matches your GitHub Pages URL exactly

**Issue**: Build fails in GitHub Actions
**Solution**: Check the Actions tab for detailed error messages

**Issue**: Changes not appearing
**Solution**: 
- GitHub Pages can take a few minutes to update
- Clear browser cache
- Check that you pushed to the correct branch

### Manual Troubleshooting Steps

1. **Check GitHub Actions logs** (if using Method 1)
2. **Verify gh-pages branch exists** and contains built HTML files
3. **Confirm Pages settings** in repository settings
4. **Test local build** with `mkdocs build` to ensure no errors

## Security Notes

- The `.github/workflows/ci.yml` file needs `contents: write` permission
- GitHub Actions will automatically create the `gh-pages` branch
- The workflow runs on every push to `main` or `master`

## Updating the Site

### With GitHub Actions (Method 1)
Simply push changes to your main branch - GitHub Actions handles the rest.

### Manual Updates (Method 2)
```bash
# Make your changes
git add .
git commit -m "Update content"
git push origin main

# Deploy updated site
source venv/bin/activate
mkdocs gh-deploy
```

## Best Practices

1. **Always test locally** before deploying: `mkdocs serve`
2. **Use descriptive commit messages** for easy tracking
3. **Review changes** in your local development server first
4. **Keep dependencies updated** in `requirements.txt`
5. **Monitor GitHub Actions** for successful deployments

## Performance Tips

- GitHub Actions caches dependencies for faster builds
- MkDocs Material includes search optimization
- Static site generation ensures fast loading
- GitHub's CDN provides global performance