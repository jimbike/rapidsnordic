# Auto Build Setup for Rapids Nordic

## Overview
This setup provides automated daily builds to refresh content and ensure the site always displays current information.

## Components

### 1. GitHub Action - Daily Scheduled Build
**File**: `.github/workflows/daily-build.yml`

- **Schedule**: Runs daily at 6:00 AM UTC (11:00 PM PST / 12:00 AM MST)
- **Purpose**: Ensures date-based content stays fresh and any scheduled content becomes visible
- **Manual Trigger**: Can be triggered manually from GitHub Actions tab

### 2. Manual Build Script
**File**: `trigger-build.sh`

Run a manual build anytime:
```bash
./trigger-build.sh
```

## How It Works

1. **Daily Automatic Builds**
   - GitHub Action runs on schedule
   - Sends POST request to Netlify build hook
   - Site rebuilds with fresh content
   - Any date-based logic (like "upcoming" vs "past" events) updates

2. **Manual Builds**
   - Run the shell script when immediate update needed
   - Useful after major content changes
   - No need to wait for daily schedule

## Setup Instructions

### Enable GitHub Actions
1. Push these files to your GitHub repository
2. Go to repository Settings → Actions → General
3. Ensure Actions are enabled

### Verify Build Hook
The Netlify build hook URL is:
```
https://api.netlify.com/build_hooks/692311909b99cadcfd8082bd
```

This triggers builds when called.

## Benefits

- **Fresh Content**: Date-sensitive content automatically updates
- **No Manual Intervention**: Builds happen automatically overnight
- **Workout Visibility**: Past workouts marked as "completed" automatically
- **Announcement Timing**: Time-based announcements appear when scheduled

## Monitoring

- **GitHub Actions**: Check runs at github.com/jimbike/rapidsnordic/actions
- **Netlify Dashboard**: Monitor builds at app.netlify.com
- **Build Status**: Each build logs timestamp for tracking

## Customization

### Change Schedule Time
Edit the cron expression in `.github/workflows/daily-build.yml`:
```yaml
- cron: '0 6 * * *'  # Current: 6:00 AM UTC daily
```

Cron format: `minute hour day month weekday`

### Common Schedule Examples
- `0 12 * * *` - Noon UTC daily
- `0 6 * * 1-5` - Weekdays only at 6 AM UTC  
- `0 6,18 * * *` - Twice daily at 6 AM and 6 PM UTC

## Troubleshooting

### Builds Not Triggering
1. Check GitHub Actions are enabled
2. Verify webhook URL is correct
3. Check Netlify build minutes haven't exceeded limit

### Manual Test
Test the webhook manually:
```bash
curl -X POST https://api.netlify.com/build_hooks/692311909b99cadcfd8082bd
```

Should return empty response with 200 status code.

---

*Setup completed: November 2025*