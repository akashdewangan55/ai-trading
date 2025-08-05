import csv
from config import DATA_FILE
from pathlib import Path

def log_trade(pred_color, pred_number):
    Path(DATA_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['-', '-', '-', pred_color, pred_number, '-'])

def get_stats():
    try:
        with open(DATA_FILE, 'r') as file:
            lines = list(csv.reader(file))[1:]  # Skip header
            total = len(lines)
            reds = sum(1 for row in lines if 'Red' in row[3])
            greens = sum(1 for row in lines if 'Green' in row[3])
            violets = sum(1 for row in lines if 'Violet' in row[3])
            return (f"Total Predictions: {total}\n"
                    f"🔴 Red: {reds}\n🟢 Green: {greens}\n🟪 Violet: {violets}")
    except FileNotFoundError:
        return "No predictions logged yet."