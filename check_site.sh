#!/bin/bash

# Check if GitHub Pages site is live
SITE_URL="https://gispocoding.github.io/lih_api_manual/"

echo "🔍 Checking if GitHub Pages site is live..."
echo "URL: $SITE_URL"
echo ""

for i in {1..10}; do
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL")
    
    if [ "$HTTP_CODE" = "200" ]; then
        echo "✅ Site is LIVE! ($HTTP_CODE)"
        echo "🌐 Your Location API Business Manual is available at:"
        echo "   $SITE_URL"
        echo ""
        echo "🎉 Success! The site is now publicly accessible."
        break
    else
        echo "⏳ Attempt $i/10: Site not ready yet ($HTTP_CODE)"
        if [ $i -lt 10 ]; then
            echo "   Waiting 30 seconds before next check..."
            sleep 30
        fi
    fi
done

if [ "$HTTP_CODE" != "200" ]; then
    echo ""
    echo "⚠️  Site is not accessible yet. This is normal and can take up to 10 minutes."
    echo "   1. Make sure you enabled GitHub Pages in repository settings"
    echo "   2. Check: https://github.com/GispoCoding/lih_api_manual/settings/pages"
    echo "   3. Verify source is set to 'gh-pages' branch"
    echo ""
    echo "   You can manually check: $SITE_URL"
fi