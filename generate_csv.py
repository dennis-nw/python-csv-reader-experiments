import csv
import random
import time
from datetime import datetime, timedelta

ROWS = 5_000_000
OUTPUT_FILE = "data.csv"
CATEGORIES = ["food", "transport", "utilities", "entertainment"]

START_DATE = datetime(2020, 1, 1)
END_DATE = datetime(2025, 12, 31)


def get_random_date():
    delta = END_DATE - START_DATE
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return START_DATE + timedelta(seconds=random_seconds)


def main():
    t0 = time.time()

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "timestamp", "amount", "category"])
        for i in range(1, ROWS + 1):
            writer.writerow(
                [
                    i,
                    get_random_date(),
                    round(random.uniform(1, 1000), 2),
                    random.choice(CATEGORIES),
                ]
            )

            if i % 100_000 == 0:
                print(f"Written {i} rows")

    elapsed = time.time() - t0
    print(f"Done in {elapsed:.1f}s → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
