#!/usr/bin/env python3
"""
Generate workout markdown files for Rapids Nordic 2025 Season
Based on periodized training plan with race prep and recovery
"""

import csv
import os
from datetime import datetime, timedelta
from pathlib import Path

# Base directory for workouts
WORKOUT_DIR = "/Users/jamesbujold/Documents/Sites/rapidsnordic/rapidsnordic-astro/src/content/workouts"
ANNOUNCEMENT_DIR = "/Users/jamesbujold/Documents/Sites/rapidsnordic/rapidsnordic-astro/src/content/announcements"

# Training phases with specific workout types
TRAINING_PHASES = {
    "base": {
        "name": "Base Building Phase",
        "focus": "Aerobic capacity, technique foundation, strength",
        "intensity_range": "3-6",
    },
    "transition": {
        "name": "Snow Transition Phase", 
        "focus": "Technique refinement, snow feel, easy volume",
        "intensity_range": "4-7",
    },
    "race_prep": {
        "name": "Race Preparation Phase",
        "focus": "Race pace intervals, speed work, tactics",
        "intensity_range": "6-9",
    },
    "competition": {
        "name": "Competition Phase",
        "focus": "Race sharpening, recovery, peak performance",
        "intensity_range": "5-8",
    },
    "taper": {
        "name": "Taper Phase",
        "focus": "Recovery, race-specific speed, mental prep",
        "intensity_range": "4-7",
    }
}

def parse_csv(file_path):
    """Parse the season schedule CSV"""
    events = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Subject']:  # Skip empty rows
                events.append(row)
    return events

def determine_phase(date_str):
    """Determine training phase based on date"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Define phase dates
    if date < datetime(2025, 11, 24):
        return "base"
    elif date < datetime(2025, 12, 8):
        return "transition"
    elif date < datetime(2026, 1, 7):
        return "race_prep"
    elif date < datetime(2026, 1, 26):
        return "competition"
    else:
        return "taper"

def get_days_until_race(date_str, events):
    """Calculate days until next race"""
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    for event in events:
        if 'Race Day' in event.get('Description', '') or event['Subject'] not in ['Practice']:
            event_date = datetime.strptime(event['Start Date'], "%Y-%m-%d")
            if event_date > current_date:
                return (event_date - current_date).days, event['Subject']
    return None, None

def generate_dryland_workout(date, location, phase, days_to_race, week_num):
    """Generate dryland workout based on phase and proximity to race"""
    workouts = {
        1: {
            "title": "Aerobic Base Building",
            "warmup": "- 10 min easy jog\n- Dynamic stretching (leg swings, high knees, butt kicks)\n- 5 min progressive run",
            "main": """#### Circuit A (3 rounds, 90 sec rest between)
- 30 sec bounding uphill
- 20 burpees
- 40 sec plank
- 15 box jumps
- 30 sec mountain climbers

#### Circuit B (3 rounds, 2 min rest between)
- 400m tempo run (85% effort)
- 20 push-ups
- 30 walking lunges (each leg)
- 20 V-sits""",
            "cooldown": "- 10 min easy jog\n- Static stretching (15 min)\n- Foam rolling",
            "intensity": "6"
        },
        2: {
            "title": "Hill Power Development",
            "warmup": "- 15 min easy run with 4x30sec pickups\n- Dynamic mobility routine\n- Hill bounding prep drills",
            "main": """#### Hill Workout
- 8 x 45 sec hill bounds (focus on power and form)
- Walk down recovery between reps
- 4 x 30 sec steep hill sprints (90% effort)
- Easy jog down recovery

#### Strength Circuit
- 3 x 15 squat jumps
- 3 x 20 Russian twists
- 3 x 15 single-leg deadlifts (each)
- 3 x 30 sec side plank (each side)""",
            "cooldown": "- 10 min easy run\n- Stretch and core stability work",
            "intensity": "7"
        },
        3: {
            "title": "Tempo and Technique",
            "warmup": "- 10 min easy run\n- Ski imitation drills (5 min)\n- 4 x 100m strides",
            "main": """#### Tempo Work
- 3 x 8 min tempo run (threshold pace)
- 3 min easy jog recovery
- Focus on maintaining form when tired

#### Technique Drills
- 20 x diagonal stride imitation (no poles)
- 20 x double pole imitation
- 20 x skate push-off (each leg)""",
            "cooldown": "- 10 min easy jog\n- Full body stretching routine",
            "intensity": "7"
        }
    }
    
    # Select workout based on week pattern
    workout_type = week_num % 3 + 1
    return workouts[workout_type]

def generate_snow_workout(date, location, phase, days_to_race, week_num, technique_focus):
    """Generate on-snow workout based on phase and race proximity"""
    
    # Determine if recovery is needed (day after race or 2 days before)
    if days_to_race == 2:
        return {
            "title": "Pre-Race Opener",
            "warmup": "- 20 min easy ski\n- 4 x 30 sec race pace accelerations",
            "main": """#### Race Prep
- 3 x 3 min at race pace
- 3 min easy ski recovery
- 4 x 30 sec sprint efforts (simulate race finish)
- Easy ski recovery

#### Technique Check
- Review race technique focus points
- Practice transitions (if skate race)""",
            "cooldown": "- 15 min easy ski\n- Light stretching",
            "intensity": "6",
            "notes": "Keep volume low, focus on feeling sharp"
        }
    elif days_to_race == 1:
        return {
            "title": "Race Day Prep",
            "warmup": "- 15 min easy ski\n- Dynamic stretching",
            "main": """#### Pre-Race Activation
- 3 x 1 min race pace efforts
- 2 min recovery
- 4 x 15 sec sprints
- Full recovery between

#### Course Preview
- Ski race course if available
- Review hills and technical sections""",
            "cooldown": "- 10 min easy ski\n- Hydrate and rest",
            "intensity": "5",
            "notes": "Race tomorrow! Stay relaxed, visualize success"
        }
    
    # Regular training workouts by phase
    if phase == "transition":
        return {
            "title": f"Technique Focus - {technique_focus}",
            "warmup": "- 20 min easy ski\n- Balance and agility drills on skis",
            "main": f"""#### Technique Development
- 6 x 5 min {technique_focus} technique focus
- Emphasis on:
  - Weight transfer
  - Glide optimization
  - Timing and rhythm
- Easy ski between sets

#### Drill Work
- 10 x 30 sec specific technique drill
- Full recovery between""",
            "cooldown": "- 15 min easy ski\n- Review video if available",
            "intensity": "5"
        }
    elif phase == "race_prep":
        interval_workouts = {
            1: {
                "title": "VO2 Max Intervals",
                "main": """#### Interval Set
- 5 x 4 min at VO2 max pace (90% effort)
- 3 min easy ski recovery
- Focus on maintaining technique under fatigue

#### Speed Work
- 6 x 30 sec all-out sprints
- Full recovery between""",
                "intensity": "8"
            },
            2: {
                "title": "Threshold Training",
                "main": """#### Threshold Work
- 3 x 10 min at threshold pace (85% effort)
- 3 min recovery
- Maintain consistent pace throughout

#### Tempo Finish
- 15 min continuous tempo ski
- Focus on efficiency""",
                "intensity": "7"
            },
            3: {
                "title": "Race Simulation",
                "main": """#### Race Simulation
- 2 x 15 min at race pace
- 5 min recovery
- Simulate race conditions and tactics

#### Sprint Finish Practice
- 5 x 1 min hard efforts
- 2 min recovery""",
                "intensity": "8"
            }
        }
        workout_num = week_num % 3 + 1
        base = interval_workouts[workout_num]
        base["warmup"] = "- 25 min progressive warm-up\n- Include 4 x 30 sec pickups"
        base["cooldown"] = "- 20 min easy ski\n- Stretching and recovery"
        return base
    else:  # competition/taper
        return {
            "title": "Competition Maintenance",
            "warmup": "- 20 min easy ski\n- 4 x 20 sec accelerations",
            "main": """#### Quality Work
- 4 x 5 min at slightly under race pace
- 3 min recovery
- Stay smooth and controlled

#### Speed Touch
- 5 x 45 sec race pace efforts
- Full recovery""",
            "cooldown": "- 15 min easy ski\n- Focus on recovery",
            "intensity": "6"
        }

def generate_holiday_workout(date):
    """Special workout recommendations for holiday periods"""
    return {
        "title": "Holiday Training - Maintain Fitness",
        "warmup": "- 15 min easy activity of choice\n- Dynamic stretching",
        "main": """#### Option A - Ski if Available
- 60-90 min easy to moderate ski
- Include 5 x 2 min tempo efforts

#### Option B - Cross Training
- 45 min run or bike
- 20 min strength circuit:
  - Push-ups
  - Squats
  - Core work
  - Pull-ups if available

#### Option C - Active Recovery
- 30 min easy activity
- Yoga or extensive stretching
- Foam rolling""",
        "cooldown": "- Easy cool down\n- Enjoy time with family!",
        "intensity": "5",
        "notes": "Maintain fitness but don't stress about missing a workout. Family time is important too!"
    }

def create_workout_markdown(event, workout_data, week_num):
    """Create a markdown file for a workout"""
    date = event['Start Date']
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    
    # Create filename
    filename = f"{date}-workout.md"
    filepath = os.path.join(WORKOUT_DIR, filename)
    
    # Generate markdown content
    content = f"""---
title: "{workout_data['title']}"
date: {date}
week: {week_num}
type: "training"
duration: "{event.get('Start Time', '')} - {event.get('End Time', '')}"
location: "{event.get('Location', '')}"
intensity: "{workout_data.get('intensity', '5')}"
---

## {workout_data['title']}

**Date:** {date_obj.strftime('%B %d, %Y')}  
**Time:** {event.get('Start Time', '')} - {event.get('End Time', '')}  
**Location:** {event.get('Location', '')}  
**Intensity:** {workout_data.get('intensity', '5')}/10

### Warm-Up (15-20 min)
{workout_data.get('warmup', '')}

### Main Workout
{workout_data.get('main', '')}

### Cool Down (10-15 min)
{workout_data.get('cooldown', '')}

### Notes
{workout_data.get('notes', '''- Hydrate well before, during, and after practice
- Bring appropriate clothing layers
- Focus on quality over quantity''')}

### Equipment Needed
{workout_data.get('equipment', '- Water bottle\n- Appropriate training clothes\n- Running shoes or ski equipment as needed')}

---
*Remember: Listen to your body. Quality training beats quantity every time.*"""
    
    return filepath, content

def create_waxing_announcement(race_event):
    """Create waxing session announcement before races"""
    race_date = datetime.strptime(race_event['Start Date'], "%Y-%m-%d")
    wax_date = race_date - timedelta(days=1)
    
    race_type = "Skate" if "Skate" in race_event.get('Description', '') else "Classic"
    
    filename = f"{wax_date.strftime('%Y-%m-%d')}-wax-session.md"
    filepath = os.path.join(ANNOUNCEMENT_DIR, filename)
    
    content = f"""---
title: "Wax Session for {race_event['Subject']}"
date: {wax_date.strftime('%Y-%m-%d')}
author: "Coach"
tags: [waxing, race-prep, volunteer]
---

## Ski Waxing Session - {race_event['Subject']}

**When:** {wax_date.strftime('%B %d')} (day before race)  
**Time:** 5:00 PM - 7:00 PM  
**Location:** GRHS Wax Room  
**Race:** {race_event['Subject']} ({race_type})

### Parent Volunteers Needed!

We need parent volunteers to help prepare skis for tomorrow's race at {race_event.get('Location', 'TBD')}.

### What to Bring
- Skis that need waxing (labeled with athlete's name)
- Any personal wax you prefer
- Helping hands!

### Wax Plan
- **Race Type:** {race_type}
- **Expected Conditions:** Will be determined based on weather forecast
- **Wax Selection:** Will be announced morning of wax session

### Drop-Off Option
If you can't attend the wax session, you can drop off skis by 4:30 PM and pick them up by 7:30 PM.

### Questions?
Contact Coach at coach@rapidsnordic.com

---
*Thank you to all our parent volunteers who help make race day successful!*"""
    
    return filepath, content

def main():
    """Generate all workout and waxing files"""
    # Parse CSV
    csv_path = "/Users/jamesbujold/Downloads/GRHS_Nordic_2025_Season_Schedule_OFFICIAL.csv"
    events = parse_csv(csv_path)
    
    # Create directories if they don't exist
    Path(WORKOUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(ANNOUNCEMENT_DIR).mkdir(parents=True, exist_ok=True)
    
    # Track week numbers
    start_date = datetime(2025, 11, 10)
    
    # Process each event
    for event in events:
        if not event['Subject']:
            continue
            
        event_date = datetime.strptime(event['Start Date'], "%Y-%m-%d")
        week_num = ((event_date - start_date).days // 7) + 1
        
        if event['Subject'] == 'Practice':
            # Determine training phase
            phase = determine_phase(event['Start Date'])
            days_to_race, next_race = get_days_until_race(event['Start Date'], events)
            
            # Check if it's a holiday
            if event_date.month == 12 and event_date.day in [24, 25, 26, 31]:
                workout_data = generate_holiday_workout(event['Start Date'])
            # Dryland vs on-snow
            elif "Dryland" in event.get('Description', ''):
                workout_data = generate_dryland_workout(
                    event['Start Date'], 
                    event.get('Location', ''),
                    phase,
                    days_to_race,
                    week_num
                )
            else:  # On-snow
                technique = "Classic" if week_num % 2 == 0 else "Skate"
                workout_data = generate_snow_workout(
                    event['Start Date'],
                    event.get('Location', ''),
                    phase,
                    days_to_race,
                    week_num,
                    technique
                )
            
            # Create workout file
            filepath, content = create_workout_markdown(event, workout_data, week_num)
            print(f"Creating workout: {filepath}")
            with open(filepath, 'w') as f:
                f.write(content)
                
        elif 'Race Day' in event.get('Description', '') or event['Subject'] not in ['Practice']:
            # Create waxing announcement for races
            filepath, content = create_waxing_announcement(event)
            print(f"Creating wax session: {filepath}")
            with open(filepath, 'w') as f:
                f.write(content)
    
    print(f"\nGenerated {len([e for e in events if e['Subject'] == 'Practice'])} workout files")
    print(f"Generated {len([e for e in events if 'Race Day' in e.get('Description', '')])} waxing announcements")

if __name__ == "__main__":
    main()