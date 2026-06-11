import time
import tracemalloc

import pandas as pd

FILE = "data.csv"


def main():
    tracemalloc.start()
    t0 = time.perf_counter()

    df = pd.read_csv(FILE)

    pd.set_option("display.float_format", "{:,.2f}".format)

    # Aggregation task: sum of amount grouped by category
    result = df.groupby("category")["amount"].sum()

    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()

    print("Result:")
    print(result.to_string())
    print(f"\nWall time : {elapsed:.2f}s")
    print(f"Peak memory: {peak / 1024 / 1024:.1f} MB")

    tracemalloc.stop()


if __name__ == "__main__":
    main()
