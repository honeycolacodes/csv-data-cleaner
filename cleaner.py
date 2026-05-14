import csv
import os

def clean_csv(input_file, output_file):
    rows = []
    seen = set()
    
    # Read the CSV file
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        for row in reader:
            # Strip whitespace from all values
            cleaned_row = {k: v.strip() for k, v in row.items()}
            
            # Skip completely empty rows
            if all(v == "" for v in cleaned_row.values()):
                continue
            
            # Skip duplicate rows
            row_tuple = tuple(cleaned_row.values())
            if row_tuple in seen:
                continue
            seen.add(row_tuple)
            
            # Replace empty cells with "N/A"
            cleaned_row = {k: v if v != "" else "N/A" for k, v in cleaned_row.items()}
            
            rows.append(cleaned_row)
    
    # Write the cleaned data to a new file
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Done! Cleaned {len(rows)} rows.")
    print(f"Saved to: {output_file}")

# Change these to your file paths
input_file = "messy_data.csv"
output_file = "cleaned_data.csv"

clean_csv(input_file, output_file)
