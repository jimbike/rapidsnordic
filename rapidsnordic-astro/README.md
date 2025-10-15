# GRHS Nordic Team Site (Astro)

A fast, good-looking team site with Markdown content and a Google Calendar embed.

## Prereqs
- Node 18+
- (Optional) Obsidian Git to sync your vault to this folder

## Setup
```bash
cd rapidsnordic-astro
npm install
npm run dev
```
Visit http://localhost:4321

## Content Editing
- Announcements: `src/content/announcements/*.md`
- Workouts: `src/content/workouts/*.md`
- Registration page: `src/pages/registration.astro` (uses QR in `/public/qr/registration.png`)
- Calendar page: set your Google Calendar ID in `src/pages/calendar.astro`

## Deploy
- Netlify: connect repo, build with `npm run build`, publish `dist/`
- Vercel: "Import Project" → framework: Astro

## Replace Branding
- Update `/public/images/logo.svg`
- Tweak colors in `src/styles/global.css`
