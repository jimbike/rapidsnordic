#!/usr/bin/env python3
import csv
from datetime import datetime, timedelta

# Read the calendar CSV
with open('/Users/jamesbujold/Documents/Sites/rapidsnordic/rapids_nordic_2025_2026_calendar.csv', 'r') as f:
    reader = csv.DictReader(f)
    events = list(reader)

# Extract practice dates (ignore races, waxing, meetings)
practice_dates = set()
for event in events:
    if 'Practice' in event['Subject']:
        date_str = event['Start Date']
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        practice_dates.add(date_obj.date())

# Define season date range (Nov 10, 2025 to Feb 10, 2026)
start_date = datetime(2025, 11, 10).date()
end_date = datetime(2026, 2, 10).date()

# Find all weekdays (Mon-Fri) that should have practice
missing_dates = []
current_date = start_date

while current_date <= end_date:
    # Check if it's a weekday (0-4 = Mon-Fri)
    if current_date.weekday() <= 4:  # Monday to Friday
        # Skip Thanksgiving week (Nov 27-28) and Winter break (Dec 25, Jan 1)
        if not (
            (current_date.month == 11 and current_date.day in [27, 28]) or  # Thanksgiving
            (current_date.month == 12 and current_date.day == 25) or  # Christmas
            (current_date.month == 1 and current_date.day == 1)  # New Year's
        ):
            if current_date not in practice_dates:
                missing_dates.append(current_date)
    
    current_date += timedelta(days=1)

# Create CSV with missing practice days
output_file = '/Users/jamesbujold/Documents/Sites/rapidsnordic/missing_practice_days.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Description', 'Location', 'Private']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for date in sorted(missing_dates):
        # Determine practice type based on date
        if date < datetime(2025, 11, 24).date():
            desc = "Dryland: running, bounding drills, core strength"
            location = "Grand Rapids HS (meet at front doors)"
        elif date < datetime(2025, 12, 8).date():
            desc = "On-snow transition: technique focus, easy ski"
            location = "Mt. Itasca"
        else:
            desc = "On-snow training: intervals and technique"
            location = "Mt. Itasca"
        
        writer.writerow({
            'Subject': 'Practice',
            'Start Date': date.strftime('%m/%d/%Y'),
            'Start Time': '15:30',
            'End Date': date.strftime('%m/%d/%Y'),
            'End Time': '17:30',
            'Description': desc,
            'Location': location,
            'Private': 'False'
        })

print(f"Found {len(missing_dates)} missing practice days")
print("\nMissing dates:")
for date in sorted(missing_dates):
    print(f"  {date.strftime('%A, %B %d, %Y')}")
print(f"\nCSV saved to: {output_file}")