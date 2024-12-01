from aocd import get_data
import pandas as pd

def solve():
    data = get_data(day=1, year=2024).split("\n")

    df = pd.DataFrame([list(map(int, line.split())) for line in data], columns=["Col1", "Col2"])
    df["Col1"] = df["Col1"].sort_values().values
    df["Col2"] = df["Col2"].sort_values().values

    df["Distance"] = abs(df["Col1"] - df["Col2"])

    print(df["Distance"].sum())

solve()