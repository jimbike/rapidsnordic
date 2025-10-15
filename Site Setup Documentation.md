# Rapids Nordic Site Setup Documentation

## Overview
This Obsidian vault serves as the content management system for the Rapids Nordic website, automatically deployed via GitHub and Netlify.

## Tech Stack

### Content Management
- **Obsidian**: Local markdown editor and vault manager
- **Obsidian Git Plugin**: Automated sync between vault and GitHub

### Version Control
- **GitHub Repository**: [github.com/jimbike/rapidsnordic](https://github.com/jimbike/rapidsnordic)
- **Branch**: main
- **Auto-sync**: Every 10 minutes via Obsidian Git plugin

### Site Framework
- **Astro**: Static site generator
- **Location**: `/rapidsnordic-astro` directory
- **Build Command**: `npm run build`
- **Output Directory**: `rapidsnordic-astro/dist`

### Hosting & Deployment
- **Platform**: [Netlify](https://app.netlify.com)
- **Authentication**: GitHub OAuth (using jimbike account)
- **Deployment**: Automatic on push to main branch
- **Build Settings**:
  - Base directory: `rapidsnordic-astro`
  - Build command: `npm run build`
  - Publish directory: `rapidsnordic-astro/dist`

## Workflow

### Content Updates
1. Edit markdown files in Obsidian
2. Obsidian Git plugin auto-commits and pushes changes
3. GitHub receives the update
4. Netlify detects change and rebuilds site
5. Site is live within ~1-2 minutes

### Manual Sync (if needed)
- **Commit & Push**: `Cmd+P` → "Obsidian Git: Commit all changes"
- **Pull Updates**: `Cmd+P` → "Obsidian Git: Pull"

## Directory Structure

```
/rapidsnordic/
├── Welcome.md                          # Vault home
├── Site Setup Documentation.md         # This file
├── .gitignore                          # Git ignore rules
├── rapidsnordic-astro/                # Astro site
│   ├── src/
│   │   ├── content/                   # Site content
│   │   │   ├── announcements/         # Team announcements
│   │   │   └── workouts/              # Workout plans
│   │   ├── pages/                     # Site pages
│   │   ├── layouts/                   # Page layouts
│   │   └── styles/                    # CSS styles
│   ├── public/                        # Static assets
│   │   ├── images/                    # Site images
│   │   └── qr/                        # QR codes
│   ├── package.json                   # Node dependencies
│   ├── astro.config.mjs              # Astro config
│   └── netlify.toml                   # Netlify config
└── .git/                              # Git repository

```

## Key Links

### Live Site
- **URL**: [To be provided after Netlify deployment]
- **Custom Domain**: (Can be added in Netlify settings)

### Admin & Management
- **GitHub Repo**: [github.com/jimbike/rapidsnordic](https://github.com/jimbike/rapidsnordic)
- **Netlify Dashboard**: [app.netlify.com](https://app.netlify.com)
- **Obsidian**: Local application

## Adding Content

### New Announcement
1. Create markdown file in `rapidsnordic-astro/src/content/announcements/`
2. Include frontmatter:
   ```yaml
   ---
   title: "Your Title"
   date: 2024-01-15
   ---
   ```
3. Write content in markdown

### New Workout
1. Create markdown file in `rapidsnordic-astro/src/content/workouts/`
2. Include frontmatter:
   ```yaml
   ---
   title: "Workout Name"
   date: 2024-01-15
   week: 1
   ---
   ```
3. Write workout details in markdown

## Troubleshooting

### Sync Issues
- Check Obsidian Git plugin status (bottom right corner)
- Manual sync: `Cmd+P` → "Obsidian Git: Commit all changes"
- Verify GitHub connection: `git status` in terminal

### Build Failures
- Check Netlify dashboard for error logs
- Ensure all markdown files have valid frontmatter
- Verify no broken image links

### Plugin Not Working
1. Settings → Community Plugins → Obsidian Git
2. Ensure "Enable" is toggled on
3. Check plugin settings for proper intervals
4. Restart Obsidian if needed

## Maintenance

### Regular Tasks
- Monitor Netlify build minutes (300/month free tier)
- Check GitHub repo size (should stay under 1GB)
- Review and clean old content periodically

### Backups
- GitHub serves as primary backup
- Consider local Time Machine/backup for vault
- Export critical content periodically

---

*Last Updated: 2024-10-15*
*Documentation created during initial setup*