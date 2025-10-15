# Rapids Nordic Template Setup

This guide helps you quickly create announcements and workouts using Obsidian templates.

## Option 1: Using Templater Plugin (Recommended)

### Installation
1. Open Obsidian Settings → Community Plugins
2. Browse and install **Templater**
3. Enable Templater
4. Go to Templater Settings:
   - Set Template folder location to: `templates`
   - Enable "Trigger Templater on new file creation"

### Setup Hotkeys
1. Settings → Hotkeys → Search for "Templater"
2. Set these hotkeys:
   - **Create new announcement**: `Cmd+Shift+A`
   - **Create new workout**: `Cmd+Shift+W`

### Creating Templates with Variables
In Templater settings → Template Hotkeys:
- Add `announcement-template.md` → Set hotkey
- Add `workout-template.md` → Set hotkey

### Usage
1. Press hotkey (e.g., `Cmd+Shift+A` for announcement)
2. Fill in the prompted fields:
   - Title
   - Date (auto-filled with today)
   - Other fields as needed
3. File automatically saves to correct folder

## Option 2: Using QuickAdd Plugin

### Installation
1. Install **QuickAdd** plugin from Community Plugins
2. Enable QuickAdd

### Configuration
1. Go to QuickAdd Settings
2. Add new choices:

#### Announcement Macro:
- Name: "📢 New Announcement"
- Type: Template
- Template path: `templates/announcement-template.md`
- Create in: `rapidsnordic-astro/src/content/announcements`
- File name: `{{DATE:YYYY-MM-DD}}-{{VALUE:title}}.md`

#### Workout Macro:
- Name: "🏃 New Workout"  
- Type: Template
- Template path: `templates/workout-template.md`
- Create in: `rapidsnordic-astro/src/content/workouts`
- File name: `week-{{VALUE:week}}-{{VALUE:title}}.md`

3. Add to Command Palette:
   - Toggle "Add to Command Palette" for each

### Usage
1. Press `Cmd+P` to open command palette
2. Type "QuickAdd" and select your macro
3. Fill in the prompts
4. File is created and opened

## Option 3: Simple Copy & Paste

### Manual Process
1. Open template file from `templates/` folder
2. Copy all content
3. Create new file in appropriate folder:
   - Announcements: `rapidsnordic-astro/src/content/announcements/`
   - Workouts: `rapidsnordic-astro/src/content/workouts/`
4. Paste and fill in placeholders

## Template Variables Reference

### Announcement Template
- `{{title}}` - Announcement title
- `{{date}}` - Current date (YYYY-MM-DD)
- `{{time}}` - Current time

### Workout Template  
- `{{title}}` - Workout name
- `{{date}}` - Workout date
- `{{week}}` - Training week number
- `{{workout_type}}` - Type (endurance, speed, technique, strength)
- `{{duration}}` - Length of workout
- `{{intensity}}` - Intensity level (1-10)
- `{{location}}` - Where to meet

## File Naming Convention

### Announcements
Format: `YYYY-MM-DD-title.md`
Example: `2025-01-15-season-kickoff.md`

### Workouts
Format: `week-N-title.md`
Example: `week-3-interval-training.md`

## Quick Tips

1. **Batch Creation**: Create multiple workouts at once, then schedule Git commits
2. **Tags**: Use consistent tags for easy filtering
3. **Front Matter**: Always fill in the YAML front matter for proper site rendering
4. **Preview**: Check how content looks on the local Astro dev server before pushing

## Keyboard Shortcuts Summary

| Action | Shortcut | Plugin |
|--------|----------|--------|
| New Announcement | `Cmd+Shift+A` | Templater |
| New Workout | `Cmd+Shift+W` | Templater |
| Command Palette | `Cmd+P` | Built-in |
| Quick Add | `Cmd+P` → "QuickAdd" | QuickAdd |

## Troubleshooting

- **Templates not working**: Check template folder path in plugin settings
- **Files in wrong location**: Verify output folder in QuickAdd/Templater settings  
- **Variables not replacing**: Ensure using correct syntax for your plugin
- **Site not updating**: Make sure Obsidian Git is syncing

---

*Pro Tip: Pin this document in Obsidian for quick reference!*