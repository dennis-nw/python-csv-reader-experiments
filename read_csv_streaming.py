import csv
import time
import tracemalloc
from collections import defaultdict

FILE = "data.csv"


def main():
    t0 = time.perf_counter()

    tracemalloc.start()

    totals = defaultdict(float)

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totals[row["category"]] += float(row["amount"])

    elapsed = time.perf_counter() - t0

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Result:")
    for category, total in sorted(totals.items()):
        print(f"  {category}: {total:,.2f}")
    print(f"\nWall time : {elapsed:.2f}s")
    print(f"Peak memory: {peak / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    print("Starting streaming apprach with native CSV...")
    main()
