#!/usr/bin/env python3
"""
Create workouts for missing practice days
"""

import os
from datetime import datetime

WORKOUT_DIR = "/Users/jamesbujold/Documents/Sites/rapidsnordic/rapidsnordic-astro/src/content/workouts"

# Missing workout 1: November 11, 2025 (Dryland - Week 1)
workout1 = """---
title: "Base Building - Hill Repeats"
date: 2025-11-11
week: 1
type: "training"
duration: "15:30 - 17:30"
location: "Grand Rapids HS (meet at front doors)"
intensity: "6"
---

## Base Building - Hill Repeats

**Date:** November 11, 2025  
**Time:** 15:30 - 17:30  
**Location:** Grand Rapids HS (meet at front doors)  
**Intensity:** 6/10

### Warm-Up (15-20 min)
- 10 min easy jog
- Dynamic stretching (leg swings, high knees, butt kicks)
- 5 min progressive run

### Main Workout
#### Hill Workout
- 6 x 90 sec hill runs (80% effort)
- Jog down recovery between reps
- Focus on powerful arm drive and high knee lift

#### Strength Circuit (2 rounds)
- 20 squat jumps
- 30 sec plank
- 15 burpees
- 20 walking lunges (each leg)
- 30 Russian twists
- 1 min rest between rounds

### Cool Down (10-15 min)
- 10 min easy jog
- Static stretching (15 min)
- Foam rolling

### Notes
- First week of training! Focus on good form over speed
- Stay hydrated
- Bring layers for changing weather

### Equipment Needed
- Water bottle
- Running shoes
- Appropriate training clothes for weather

---
*Remember: Listen to your body. Quality training beats quantity every time.*"""

# Missing workout 2: January 19, 2026 (MLK Day - Competition phase - Week 10)
workout2 = """---
title: "MLK Day Distance Ski"
date: 2026-01-19
week: 10
type: "training"
duration: "15:30 - 17:30"
location: "Mt. Itasca"
intensity: "6"
---

## MLK Day Distance Ski

**Date:** January 19, 2026  
**Time:** 15:30 - 17:30  
**Location:** Mt. Itasca  
**Intensity:** 6/10

### Warm-Up (15-20 min)
- 20 min easy ski
- 4 x 20 sec accelerations
- Dynamic stretching on skis

### Main Workout
#### Distance Work
- 45-60 min continuous ski at moderate pace
- Include varied terrain
- Focus on efficient technique throughout
- Heart rate zone 2-3 (conversational pace)

#### Technique Check
- 5 x 2 min technique-focused intervals
- Alternate classic and skate if conditions allow
- 1 min recovery between

### Cool Down (10-15 min)
- 15 min easy ski
- Light stretching

### Notes
- MLK Day practice - optional for those who can attend
- Focus on building aerobic base mid-season
- Great day for longer distance work

### Equipment Needed
- Skis and poles
- Water bottle
- Appropriate ski clothing
- Wax for conditions

---
*Remember: Listen to your body. Quality training beats quantity every time.*"""

# Create the workout files
with open(os.path.join(WORKOUT_DIR, "2025-11-11-workout.md"), "w") as f:
    f.write(workout1)
    print("Created workout: 2025-11-11-workout.md")

with open(os.path.join(WORKOUT_DIR, "2026-01-19-workout.md"), "w") as f:
    f.write(workout2)
    print("Created workout: 2026-01-19-workout.md")

print("\n✅ Missing workouts created successfully!")