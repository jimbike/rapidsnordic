#!/usr/bin/env python3
import csv
from datetime import datetime

# Read original schedule to check for races
original_csv = '/Users/jamesbujold/Downloads/GRHS_Nordic_2025_Season_Schedule_OFFICIAL.csv'
with open(original_csv, 'r') as f:
    reader = csv.DictReader(f)
    original_events = list(reader)

# Get race dates
race_dates = set()
for event in original_events:
    if event['Subject'] and event['Subject'] != 'Practice':
        # Parse date
        date_str = event['Start Date']
        for fmt in ["%m/%d/%y", "%m/%d/%Y"]:
            try:
                date_obj = datetime.strptime(date_str, fmt)
                race_dates.add(date_obj.date())
                break
            except:
                continue

# Read missing dates from our CSV
with open('/Users/jamesbujold/Documents/Sites/rapidsnordic/missing_practice_days.csv', 'r') as f:
    reader = csv.DictReader(f)
    missing_events = list(reader)

# Filter out race days
true_missing = []
for event in missing_events:
    date_obj = datetime.strptime(event['Start Date'], '%m/%d/%Y').date()
    if date_obj not in race_dates:
        true_missing.append(event)
        print(f"Missing practice: {date_obj.strftime('%A, %B %d, %Y')}")

# Write the actual missing practice days CSV
output_file = '/Users/jamesbujold/Documents/Sites/rapidsnordic/actual_missing_practices.csv'
with open(output_file, 'w', newline='') as csvfile:
    if true_missing:
        fieldnames = true_missing[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(true_missing)

print(f"\nFound {len(true_missing)} actual missing practice days (not race days)")
print(f"CSV saved to: {output_file}")