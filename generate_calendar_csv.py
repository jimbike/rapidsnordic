#!/usr/bin/env python3
"""
Generate Google Calendar CSV import file for Rapids Nordic 2025-2026 Season
Includes all practices, races, and waxing sessions with color coding
"""

import csv
from datetime import datetime, timedelta
import os

def parse_date(date_str):
    """Parse date from various formats"""
    for fmt in ["%Y-%m-%d", "%m/%d/%y", "%m/%d/%Y", "%Y/%m/%d"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date: {date_str}")

def create_calendar_csv():
    """Create a CSV file for Google Calendar import"""
    
    # Read the original schedule
    input_csv = "/Users/jamesbujold/Downloads/GRHS_Nordic_2025_Season_Schedule_OFFICIAL.csv"
    output_csv = "/Users/jamesbujold/Documents/Sites/rapidsnordic/rapids_nordic_2025_2026_calendar.csv"
    
    # Base URL for the website
    base_url = "https://rapidsnordic.com"
    
    # Google Calendar CSV headers
    headers = [
        "Subject",
        "Start Date",
        "Start Time", 
        "End Date",
        "End Time",
        "All Day Event",
        "Description",
        "Location",
        "Private"
    ]
    
    calendar_events = []
    
    # Parse the original CSV
    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file)
        events = [row for row in reader if row['Subject']]
    
    # Process each event
    for event in events:
        event_date = parse_date(event['Start Date'])
        
        if event['Subject'] == 'Practice':
            # Create practice event with workout link
            date_str = event_date.strftime("%Y-%m-%d")
            workout_url = f"{base_url}/workouts/{date_str}-workout/"
            
            # Determine workout type from description
            if "Dryland" in event.get('Description', ''):
                workout_type = "🏃 Dryland Training"
                color_note = "[Orange Event]"
            elif "transition" in event.get('Description', ''):
                workout_type = "⛷️ Technique Focus"
                color_note = "[Light Blue Event]"
            elif "Taper" in event.get('Description', ''):
                workout_type = "🎯 Taper Training"
                color_note = "[Yellow Event]"
            else:
                workout_type = "⛷️ On-Snow Training"
                color_note = "[Blue Event]"
            
            description = f"{workout_type}\n{event.get('Description', '')}\n\nView Workout Plan: {workout_url}\n\n{color_note}"
            
            calendar_events.append({
                "Subject": f"Practice: {workout_type}",
                "Start Date": event_date.strftime("%m/%d/%Y"),
                "Start Time": event.get('Start Time', '3:30 PM'),
                "End Date": event_date.strftime("%m/%d/%Y"),
                "End Time": event.get('End Time', '5:30 PM'),
                "All Day Event": "False",
                "Description": description,
                "Location": event.get('Location', 'Mt. Itasca'),
                "Private": "False"
            })
            
        else:  # Race events
            # Add the race event
            race_type = "Skate" if "Skate" in event.get('Description', '') else "Classic"
            if "Sprint" in event.get('Description', ''):
                race_type = f"{race_type} Sprint"
            elif "Pursuit" in event.get('Description', ''):
                race_type = "Pursuit"
            
            description = f"🏁 RACE DAY - {race_type}\n{event.get('Description', '')}\n\n[Red Event - RACE]"
            
            calendar_events.append({
                "Subject": f"RACE: {event['Subject']} ({race_type})",
                "Start Date": event_date.strftime("%m/%d/%Y"),
                "Start Time": event.get('Start Time', '11:00 AM'),
                "End Date": event_date.strftime("%m/%d/%Y"),
                "End Time": event.get('End Time', '2:00 PM'),
                "All Day Event": "False",
                "Description": description,
                "Location": event.get('Location', 'TBD'),
                "Private": "False"
            })
            
            # Add waxing session the day before
            wax_date = event_date - timedelta(days=1)
            wax_date_str = wax_date.strftime("%Y-%m-%d")
            announcement_url = f"{base_url}/announcements/{wax_date_str}-wax-session/"
            
            wax_description = f"🎿 SKI WAXING SESSION\nPrepare skis for {event['Subject']}\nRace Type: {race_type}\n\nVolunteers Needed!\nDetails: {announcement_url}\n\n[Green Event - WAXING]"
            
            calendar_events.append({
                "Subject": f"WAX SESSION: {event['Subject']}",
                "Start Date": wax_date.strftime("%m/%d/%Y"),
                "Start Time": "5:00 PM",
                "End Date": wax_date.strftime("%m/%d/%Y"),
                "End Time": "7:00 PM",
                "All Day Event": "False",
                "Description": wax_description,
                "Location": "GRHS Wax Room",
                "Private": "False"
            })
    
    # Add missing practice days manually
    # November 11 practice
    calendar_events.append({
        "Subject": "Practice: 🏃 Dryland Training",
        "Start Date": "11/11/2025",
        "Start Time": "3:30 PM",
        "End Date": "11/11/2025",
        "End Time": "5:30 PM",
        "All Day Event": "False",
        "Description": "🏃 Dryland Training\nBase Building - Hill Repeats\n\nView Workout Plan: https://rapidsnordic.com/workouts/2025-11-11-workout/\n\n[Orange Event]",
        "Location": "Grand Rapids HS (meet at front doors)",
        "Private": "False"
    })
    
    # January 19 (MLK Day) practice
    calendar_events.append({
        "Subject": "Practice: ⛷️ MLK Day Distance Ski",
        "Start Date": "01/19/2026",
        "Start Time": "3:30 PM",
        "End Date": "01/19/2026",
        "End Time": "5:30 PM",
        "All Day Event": "False",
        "Description": "⛷️ On-Snow Training\nMLK Day Distance Ski - Optional\n\nView Workout Plan: https://rapidsnordic.com/workouts/2026-01-19-workout/\n\n[Blue Event]",
        "Location": "Mt. Itasca",
        "Private": "False"
    })
    
    # Add special events
    # Season Kickoff Meeting
    calendar_events.append({
        "Subject": "📋 Mandatory Parent/Athlete Meeting",
        "Start Date": "11/06/2025",
        "Start Time": "6:00 PM",
        "End Date": "11/06/2025",
        "End Time": "7:30 PM",
        "All Day Event": "False",
        "Description": "Season kickoff meeting\nEquipment overview\nRegistration help\nMeet the coaches\n\n[Purple Event]",
        "Location": "GRHS Cafeteria",
        "Private": "False"
    })
    
    # Holiday Break Optional Practices
    holiday_dates = ["12/27/2025", "12/28/2025", "01/03/2026", "01/04/2026"]
    for date_str in holiday_dates:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        calendar_events.append({
            "Subject": "⛷️ Optional Holiday Practice",
            "Start Date": date_str,
            "Start Time": "10:00 AM",
            "End Date": date_str,
            "End Time": "12:00 PM",
            "All Day Event": "False",
            "Description": "Optional practice during break\nCheck with coach for details\n\n[Light Gray Event]",
            "Location": "Mt. Itasca",
            "Private": "False"
        })
    
    # Sort events by date
    calendar_events.sort(key=lambda x: datetime.strptime(x["Start Date"], "%m/%d/%Y"))
    
    # Write CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(calendar_events)
    
    print(f"Calendar CSV created: {output_csv}")
    print(f"Total events: {len(calendar_events)}")
    print(f"  - Practices: {len([e for e in calendar_events if 'Practice' in e['Subject']])}")
    print(f"  - Races: {len([e for e in calendar_events if 'RACE' in e['Subject']])}")
    print(f"  - Wax Sessions: {len([e for e in calendar_events if 'WAX' in e['Subject']])}")
    print(f"  - Other: {len([e for e in calendar_events if 'Practice' not in e['Subject'] and 'RACE' not in e['Subject'] and 'WAX' not in e['Subject']])}")
    
    # Create color coding guide
    color_guide = """
    
COLOR CODING GUIDE FOR GOOGLE CALENDAR:
=========================================
After importing, set colors for events containing these keywords:

1. RACE (Red) - Competition days
2. WAX (Green) - Waxing sessions  
3. Dryland (Orange) - Dryland training
4. Technique (Light Blue) - Technique focus days
5. On-Snow (Blue) - Regular snow training
6. Taper (Yellow) - Taper phase training
7. Optional (Gray) - Optional/holiday practices
8. Meeting (Purple) - Team meetings

To set colors in Google Calendar:
1. After import, click on an event
2. Click the color palette icon
3. Choose the appropriate color
4. Optional: Click "Save for all events in series" if recurring
    """
    
    print(color_guide)
    
    # Save color guide to file
    with open("/Users/jamesbujold/Documents/Sites/rapidsnordic/calendar_color_guide.txt", "w") as f:
        f.write(color_guide)
    
    return output_csv

if __name__ == "__main__":
    csv_file = create_calendar_csv()
    print(f"\n✅ Calendar CSV ready for import: {csv_file}")
    print("\nTo import into Google Calendar:")
    print("1. Open Google Calendar")
    print("2. Click the gear icon → Settings")
    print("3. Click 'Import & Export' in the left sidebar")
    print("4. Click 'Select file from your computer'")
    print("5. Choose the CSV file")
    print("6. Select the Rapids Nordic calendar")
    print("7. Click 'Import'")