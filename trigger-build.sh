#!/bin/bash

# Manual Netlify Build Trigger Script
# Usage: ./trigger-build.sh

WEBHOOK_URL="https://api.netlify.com/build_hooks/692311909b99cadcfd8082bd"

echo "🚀 Triggering Netlify build..."

response=$(curl -X POST -d '{}' -w "\n%{http_code}" "$WEBHOOK_URL" 2>/dev/null)
http_code=$(echo "$response" | tail -n1)

if [ "$http_code" = "200" ]; then
    echo "✅ Build triggered successfully!"
    echo "📅 Triggered at: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "🔗 Check build status at: https://app.netlify.com"
else
    echo "❌ Failed to trigger build (HTTP $http_code)"
    exit 1
fi