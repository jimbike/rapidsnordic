#!/usr/bin/env python3
"""
Update all workout files to polarized training model with integrated strength/balance
and race-specific focus.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Define workout updates based on date and type
WORKOUT_UPDATES = {
    # November - Early Season Base Building (Dryland)
    "2025-11-10": {
        "title": "Zone 3 Hill Power Development",
        "zone": "3",
        "intensity": "9",
        "type": "training",
        "focus": "Power Development",
        "content": """## Zone 3 Hill Power Development

**Date:** November 10, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 9/10 (Zone 3 - High Intensity)
**Focus:** Build explosive power for season

### Pre-Practice Balance (10 min)
- Single-leg stands: 3 x 30 sec each
- Lateral hops: 3 x 10 each
- Walking lunges with rotation

### Warm-Up (20 min)
- 10 min easy run (Zone 1)
- 5 min dynamic stretching
- 3 x 30 sec progressions
- 2 min easy

### Main Workout - Zone 3 (45 min)

#### Hill Power Set
- **8 x 45 sec hill bounds** (maximum power)
  - Walk down recovery
  - Focus on explosive push-off
- **6 x 30 sec steep hill sprints** (95% effort)
  - Jog down recovery
  - Simulate ski-specific power

#### Strength Circuit (Integrated)
- 3 rounds:
  - 15 jump squats
  - 20 Russian twists
  - 15 single-leg deadlifts (each)
  - 30 sec plank hold
  - 2 min rest between rounds

### Cool Down (15 min)
- 10 min easy jog (Zone 1)
- 5 min stretching

### Key Points
- This is a HIGH intensity day - go hard!
- Full recovery between efforts
- Quality over quantity
- Follow with easy day tomorrow"""
    },
    
    "2025-11-11": {
        "title": "Zone 1 Recovery & Technique",
        "zone": "1",
        "intensity": "4",
        "type": "recovery",
        "focus": "Recovery, Balance, Technique",
        "content": """## Zone 1 Recovery & Technique

**Date:** November 11, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 4/10 (Zone 1 - Easy)
**Focus:** Recovery from yesterday's Zone 3 session

### Pre-Practice Balance (10 min)
- Balance board work: 3 x 1 min
- Single-leg reaches: 3 x 10 each
- Eyes-closed balance: 3 x 30 sec

### Warm-Up (15 min)
- 10 min very easy movement
- 5 min mobility work

### Main Workout - Zone 1 (60 min)

#### Easy Aerobic Base
- 30 min easy continuous running
  - Conversational pace
  - Nose breathing when possible
  - HR < 70% max

#### Technique Drills (No fatigue)
- 10 x 30 sec ski imitation drills
  - Focus on form
  - Full recovery between
  
#### Balance & Agility Circuit
- 3 rounds (easy pace):
  - Single-leg hops: 10 each
  - Lateral shuffles: 20 yards
  - Bear crawls: 10 yards
  - Rest as needed

### Strength Integration (15 min)
- Light bodyweight only:
  - 2 x 15 air squats (slow)
  - 2 x 10 push-ups
  - 2 x 30 sec planks
  - 2 x 10 bird dogs

### Cool Down (15 min)
- 5 min easy walk
- 10 min yoga/stretching

### Key Points
- Stay EASY - this is recovery
- Focus on movement quality
- Should feel energized after, not tired"""
    },
    
    "2025-11-12": {
        "title": "Zone 1 Aerobic Base Building",
        "zone": "1",
        "intensity": "4",
        "type": "training",
        "focus": "Aerobic Base",
        "content": """## Zone 1 Aerobic Base Building

**Date:** November 12, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 4/10 (Zone 1 - Easy)
**Focus:** Build aerobic foundation

### Balance Activation (10 min)
- Dynamic balance walks
- Single-leg stands with movement
- Proprioception drills

### Warm-Up (15 min)
- 10 min easy movement
- 5 min dynamic stretching

### Main Workout - Zone 1 (75 min)

#### Long Aerobic Development
- 45 min continuous easy running
  - Mix terrain if possible
  - Maintain conversation pace
  - HR 60-70% max

#### Technique Integration
- 15 min ski-specific movements
  - Bounding (easy effort)
  - Ski walking
  - Balance challenges

#### Hill Technique (Easy)
- 15 min gentle hill repeats
  - Focus on form, not speed
  - Walk down recovery

### Strength Circuit (15 min)
- 2 rounds:
  - 20 bodyweight squats
  - 15 lunges each leg
  - 20 core twists
  - 15 glute bridges
  - 30 sec side planks

### Cool Down (10 min)
- Easy walking and stretching

### Key Points
- Zone 1 all day - no temptation to go harder
- This builds your aerobic engine
- Quality movement patterns"""
    },
    
    "2025-11-13": {
        "title": "Zone 3 Speed Development",
        "zone": "3",
        "intensity": "9",
        "type": "training",
        "focus": "Speed & Power",
        "content": """## Zone 3 Speed Development

**Date:** November 13, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 9/10 (Zone 3 - High Intensity)
**Focus:** Develop top-end speed

### Balance Warm-Up (10 min)
- Quick balance challenges
- Agility ladder (if available)
- Dynamic movements

### Warm-Up (20 min)
- 10 min easy run
- 5 min dynamics
- 4 x 20 sec accelerations
- 2 min easy

### Main Workout - Zone 3 (50 min)

#### Speed Intervals
- **8 x 2 minutes at 90% effort**
  - 3 min recovery between
  - Focus on maintaining form at speed
  
#### Sprint Power
- **10 x 20 seconds MAX effort**
  - 90 sec full recovery
  - Explosive starts

### Integrated Strength (15 min)
- Power focus:
  - 4 x 8 jump squats
  - 4 x 6 clap push-ups
  - 4 x 10 med ball slams
  - 3 x 20 sec max plank

### Cool Down (15 min)
- 10 min easy jog
- 5 min stretching

### Key Points
- High quality, high intensity
- Full recovery is crucial
- This builds race speed
- Follow with 2 easy days"""
    },
    
    "2025-11-14": {
        "title": "Zone 1 Technical Skills & Balance",
        "zone": "1",
        "intensity": "3",
        "type": "training",
        "focus": "Technique & Recovery",
        "content": """## Zone 1 Technical Skills & Balance

**Date:** November 14, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 3/10 (Zone 1 - Recovery)
**Focus:** Technical development without fatigue

### Extended Balance Work (15 min)
- Balance board: 5 min
- Single-leg exercises: 5 min
- Partner balance challenges: 5 min

### Warm-Up (10 min)
- Very easy movement
- Joint mobility

### Main Workout - Zone 1 (60 min)

#### Technical Skill Development
- 30 min ski-specific technique work
  - Slow, controlled movements
  - Video analysis if possible
  - No fatigue accumulation

#### Easy Aerobic
- 20 min easy running
  - Recovery pace
  - Focus on breathing

#### Agility & Coordination
- 10 min low-intensity agility work
  - Cones drills (walking pace)
  - Coordination exercises

### Light Strength (15 min)
- Injury prevention focus:
  - Hip strengthening
  - Core stability
  - Ankle mobility
  - All bodyweight, controlled

### Cool Down (20 min)
- 5 min easy walk
- 15 min comprehensive stretching

### Key Points
- Maximum recovery focus
- Perfect practice makes perfect
- Preparing for weekend long session"""
    }
}

# Continue with more workout definitions...
WORKOUT_UPDATES_DECEMBER = {
    # December - On-snow technique and race prep
    "2025-12-01": {
        "title": "Zone 1 Classic Technique Focus",
        "zone": "1",
        "intensity": "4",
        "type": "training",
        "focus": "Classic Technique",
        "content": """## Zone 1 Classic Technique Focus

**Date:** December 01, 2025  
**Time:** 15:30 - 17:30  
**Location:** Mt. Itasca  
**Intensity:** 4/10 (Zone 1 - Easy)
**Focus:** Classic technique development

### Pre-Ski Balance (10 min)
- Single-leg stands on snow
- Lateral movements in boots
- Balance transfers

### Warm-Up (20 min)
- 15 min easy classic ski
- 5 min dynamic movements on skis

### Main Workout - Zone 1 (70 min)

#### Classic Technique Development
- **6 x 5 min technique segments**
  - Weight transfer focus
  - Glide optimization  
  - Timing and rhythm
  - Easy ski between

#### No-Pole Classic (Balance)
- 15 min no-pole skiing
  - Challenges balance
  - Improves weight transfer

#### Drill Work
- 10 x 30 sec specific drills
  - Full recovery
  - Quality over speed

### Strength Circuit (15 min)
Post-ski, on snow:
- 3 rounds:
  - 15 ski jumps
  - 20 core twists
  - 10 single-leg squats each
  - 30 sec plank

### Cool Down (15 min)
- 10 min easy ski
- 5 min stretching

### Key Points
- Stay in Zone 1 throughout
- Focus on perfect technique
- This is skill development"""
    },
    
    "2025-12-10": {
        "title": "Zone 3 Race Simulation",
        "zone": "3",
        "intensity": "9",
        "type": "training",
        "focus": "Race Preparation",
        "content": """## Zone 3 Race Simulation

**Date:** December 10, 2025  
**Time:** 15:30 - 17:30  
**Location:** Mt. Itasca  
**Intensity:** 9/10 (Zone 3 - High Intensity)
**Focus:** Race simulation for upcoming Proctor Invite

### Pre-Race Routine Practice (10 min)
- Dynamic warm-up sequence
- Mental preparation
- Equipment check

### Warm-Up (25 min)
- 15 min easy ski
- 5 min progressions
- 4 x 30 sec at race pace
- 1 min easy

### Main Workout - Zone 3 (50 min)

#### Race Simulation
- **2 x 15 min at race pace**
  - 5 min recovery between
  - Skate technique
  - Simulate race conditions

#### Sprint Finish Practice
- **6 x 1 min hard efforts**
  - 2 min recovery
  - Practice finishing kick

### Post-Race Routine (15 min)
- Immediate cool-down ski
- Hydration practice
- Recovery protocol

### Cool Down (20 min)
- 15 min easy ski
- 5 min stretching

### Key Points
- Treat like race day
- Full effort required
- Practice entire race routine
- Taper begins after this"""
    },
    
    "2025-12-15": {
        "title": "Zone 1 Pre-Race Activation",
        "zone": "1",
        "intensity": "3",
        "type": "training",
        "focus": "Race Preparation",
        "content": """## Zone 1 Pre-Race Activation

**Date:** December 15, 2025  
**Time:** 15:30 - 17:30  
**Location:** Mt. Itasca  
**Intensity:** 3/10 (Zone 1 - Easy)
**Focus:** Activation for tomorrow's Grand Rapids Classic race

### Warm-Up (15 min)
- 10 min very easy ski
- 5 min dynamic stretching

### Main Workout - Zone 1 with bursts (30 min)

#### Pre-Race Activation
- **3 x 1 min at race pace**
  - 3 min recovery
  - Classic technique
  - Feel fast and smooth

#### Speed Bursts
- **5 x 15 sec fast starts**
  - Full recovery
  - Neural activation only

#### Course Preview
- Ski race course if possible
- Identify key sections
- Visualize race plan

### Cool Down (15 min)
- 10 min very easy ski
- 5 min light stretching

### Race Prep Checklist
- ✅ Wax skis tonight
- ✅ Prepare race bag
- ✅ Hydration plan
- ✅ Early bedtime
- ✅ Visualize success

### Key Points
- Stay relaxed
- Don't overdo it
- Trust your training
- Get excited to race!"""
    }
}

def update_workout_file(filepath, date_str):
    """Update a single workout file with new content"""
    
    # Check which update dictionary contains this date
    if date_str in WORKOUT_UPDATES:
        update = WORKOUT_UPDATES[date_str]
    elif date_str in WORKOUT_UPDATES_DECEMBER:
        update = WORKOUT_UPDATES_DECEMBER[date_str]
    else:
        # For dates not explicitly defined, determine zone based on pattern
        update = generate_default_workout(date_str)
    
    # Read the current file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Update the frontmatter
    new_frontmatter = f"""---
title: "{update['title']}"
date: {date_str}
week: {calculate_week(date_str)}
type: "{update['type']}"
duration: "15:30 - 17:30"
location: "{get_location(date_str)}"
intensity: "{update['intensity']}"
zone: "{update['zone']}"
focus: "{update['focus']}"
---

"""
    
    # Combine with new content
    new_content = new_frontmatter + update['content']
    
    return new_content

def calculate_week(date_str):
    """Calculate training week number"""
    start_date = datetime(2025, 11, 10)
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    weeks = (current_date - start_date).days // 7 + 1
    return weeks

def get_location(date_str):
    """Determine location based on date"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    if date < datetime(2025, 11, 24):
        return "Grand Rapids HS (meet at front doors)"
    else:
        return "Mt. Itasca"

def generate_default_workout(date_str):
    """Generate a default workout based on weekly pattern"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date.weekday()  # 0 = Monday, 6 = Sunday
    
    # Default weekly pattern following polarized model
    if weekday == 0:  # Monday - Recovery
        return {
            "title": "Zone 1 Recovery & Technique",
            "zone": "1",
            "intensity": "3",
            "type": "recovery",
            "focus": "Recovery",
            "content": generate_zone1_content(date_str, "recovery")
        }
    elif weekday == 1:  # Tuesday - High Intensity
        return {
            "title": "Zone 3 Intervals",
            "zone": "3",
            "intensity": "9",
            "type": "training",
            "focus": "High Intensity",
            "content": generate_zone3_content(date_str)
        }
    elif weekday == 2:  # Wednesday - Easy Aerobic
        return {
            "title": "Zone 1 Aerobic Base",
            "zone": "1",
            "intensity": "4",
            "type": "training",
            "focus": "Aerobic Base",
            "content": generate_zone1_content(date_str, "aerobic")
        }
    elif weekday == 3:  # Thursday - Easy or Pre-race
        return {
            "title": "Zone 1 Technique & Balance",
            "zone": "1",
            "intensity": "4",
            "type": "training",
            "focus": "Technique",
            "content": generate_zone1_content(date_str, "technique")
        }
    elif weekday == 4:  # Friday - High Intensity or Pre-race
        if is_race_tomorrow(date_str):
            return {
                "title": "Zone 1 Pre-Race Activation",
                "zone": "1",
                "intensity": "3",
                "type": "training",
                "focus": "Race Preparation",
                "content": generate_prerace_content(date_str)
            }
        else:
            return {
                "title": "Zone 3 Speed Work",
                "zone": "3",
                "intensity": "9",
                "type": "training",
                "focus": "Speed Development",
                "content": generate_zone3_content(date_str)
            }
    else:  # Weekend
        return {
            "title": "Zone 1 Long Distance",
            "zone": "1",
            "intensity": "4",
            "type": "training",
            "focus": "Aerobic Endurance",
            "content": generate_zone1_content(date_str, "long")
        }

def generate_zone1_content(date_str, subtype):
    """Generate Zone 1 workout content"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    base_content = f"""## Zone 1 {subtype.title()} Session

**Date:** {date.strftime('%B %d, %Y')}  
**Time:** 15:30 - 17:30  
**Location:** {get_location(date_str)}  
**Intensity:** 3-4/10 (Zone 1 - Easy)
**Heart Rate:** 60-70% max

### Pre-Practice Balance (10 min)
- Single-leg balance work
- Dynamic balance drills
- Proprioception exercises

### Warm-Up (15 min)
- 10 min very easy movement
- 5 min dynamic stretching

### Main Workout - Zone 1 (60-75 min)
"""
    
    if subtype == "recovery":
        base_content += """
#### Recovery Focus
- 30-45 min easy continuous movement
- Conversational pace throughout
- Include technique drills (no fatigue)
- Balance and coordination work

### Strength (Optional - Very Light)
- 2 x 10 bodyweight movements
- Core stability work
- Flexibility focus"""
    
    elif subtype == "aerobic":
        base_content += """
#### Aerobic Base Building  
- 60-75 min continuous easy skiing/running
- Maintain steady Zone 1 pace
- Mix terrain for variety
- Focus on efficiency

### Strength Circuit (15 min)
- 3 rounds of bodyweight exercises
- Keep heart rate in Zone 1
- Focus on form"""
    
    elif subtype == "technique":
        base_content += """
#### Technique Development
- 45 min technique-focused work
- Break into 5-10 min segments
- Full recovery between efforts
- Film for analysis if possible

### Balance & Agility
- 15 min balance challenges
- Coordination drills
- Proprioception work"""
    
    elif subtype == "long":
        base_content += """
#### Long Aerobic Session
- 90-120 min continuous easy effort
- Build aerobic capacity
- Practice fueling strategy
- Mental training component

### Post-Workout Strength (Optional)
- Light circuit if feeling good
- Focus on injury prevention"""
    
    base_content += """

### Cool Down (15 min)
- 10 min very easy movement
- 5 min stretching

### Key Points
- Stay in Zone 1 - resist going harder
- Focus on quality movement
- This builds your aerobic base
- Recovery is where fitness happens"""
    
    return base_content

def generate_zone3_content(date_str):
    """Generate Zone 3 workout content"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Determine if on snow or dryland
    on_snow = date >= datetime(2025, 11, 24)
    
    content = f"""## Zone 3 High Intensity Training

**Date:** {date.strftime('%B %d, %Y')}  
**Time:** 15:30 - 17:30  
**Location:** {get_location(date_str)}  
**Intensity:** 9/10 (Zone 3 - High Intensity)
**Heart Rate:** >85% max

### Warm-Up (25 min)
- 15 min easy {"ski" if on_snow else "run"} (Zone 1)
- 5 min dynamic stretching
- 4 x 30 sec progressions
- 1 min easy

### Main Workout - Zone 3 (45-50 min)

#### High Intensity Intervals
- **5 x 4 minutes at 90-95% effort**
  - 3 min active recovery between
  - Maintain consistent pace
  - Focus on form under fatigue

#### Speed Development
- **8 x 30 seconds MAX effort**
  - 90 seconds full recovery
  - Explosive power focus

### Strength Integration (15 min)
- Power-focused exercises:
  - Jump squats
  - Explosive push-ups
  - Med ball work
  - Core power

### Cool Down (20 min)
- 15 min easy {"ski" if on_snow else "jog"}
- 5 min stretching

### Key Points
- This is a breakthrough session
- Quality over quantity
- Full effort required
- Need 48 hours recovery after"""
    
    return content

def generate_prerace_content(date_str):
    """Generate pre-race activation content"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    content = f"""## Pre-Race Activation

**Date:** {date.strftime('%B %d, %Y')}  
**Time:** 15:30 - 16:30 (Shortened)  
**Location:** {get_location(date_str)}  
**Intensity:** 3/10 (Zone 1 with bursts)
**Focus:** Neural activation for tomorrow's race

### Warm-Up (15 min)
- 10 min very easy ski
- 5 min dynamic movements

### Activation (20 min)
- **3 x 1 min at race pace**
  - 3 min easy recovery
- **5 x 15 sec sprints**
  - Full recovery
  - Stay loose and fast

### Cool Down (10 min)
- Easy skiing
- Light stretching

### Race Preparation
- ✅ Wax skis tonight
- ✅ Prepare all gear
- ✅ Hydration strategy
- ✅ Visualize race plan
- ✅ Early to bed

### Key Points
- Don't overdo it
- Feel fast and light
- Trust your training
- Get excited!"""
    
    return content

def is_race_tomorrow(date_str):
    """Check if there's a race the day after this date"""
    race_dates = [
        "2025-12-09", "2025-12-16", "2025-12-20",
        "2026-01-06", "2026-01-10", "2026-01-13",
        "2026-01-16", "2026-01-20", "2026-01-24",
        "2026-01-29", "2026-02-04", "2026-02-07",
        "2026-02-11", "2026-02-12"
    ]
    
    date = datetime.strptime(date_str, "%Y-%m-%d")
    tomorrow = date + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    
    return tomorrow_str in race_dates

def main():
    """Main function to update all workout files"""
    workout_dir = Path("/Users/jamesbujold/Documents/Sites/rapidsnordic/rapidsnordic-astro/src/content/workouts")
    
    # Get all workout files
    workout_files = list(workout_dir.glob("*.md"))
    
    print(f"Found {len(workout_files)} workout files to update")
    
    for filepath in workout_files:
        # Extract date from filename
        filename = filepath.name
        if match := re.match(r"(\d{4}-\d{2}-\d{2})-workout\.md", filename):
            date_str = match.group(1)
            
            print(f"Updating {filename}...")
            
            # Generate new content
            new_content = update_workout_file(filepath, date_str)
            
            # Write updated content
            with open(filepath, 'w') as f:
                f.write(new_content)
    
    print("All workouts updated successfully!")

if __name__ == "__main__":
    from datetime import timedelta
    main()