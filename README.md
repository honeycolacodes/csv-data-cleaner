# 🧹 CSV Data Cleaner

A Python script that automatically cleans messy spreadsheet data.

## What it does
- Removes duplicate rows
- Strips extra whitespace from all cells
- Replaces empty cells with "N/A"
- Skips completely blank rows
- Saves the cleaned data to a new file (original is never touched)

## How to use
1. Clone this repo
2. Place your CSV file in the same folder as `cleaner.py`
3. Open `cleaner.py` and update these two lines:
4. Run: `python cleaner.py`

## Example output
```
Done! Cleaned 142 rows.
Saved to: cleaned_data.csv
```

## Tech used
- Python 3
- `csv` (built-in library, no install needed)
