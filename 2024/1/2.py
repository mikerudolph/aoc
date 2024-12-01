from aocd import get_data
import pandas as pd

def solve():
    data = get_data(day=1, year=2024).split("\n")

    df = pd.DataFrame([list(map(int, line.split())) for line in data], columns=["Col1", "Col2"])
    df["Col1"] = df["Col1"].sort_values().values
    df["Col2"] = df["Col2"].sort_values().values

    col2_counts = df["Col2"].value_counts().to_dict()

    df["Similarity"] = df["Col1"].apply(lambda x: x * col2_counts.get(x, 0))

    print(df["Similarity"].sum())

solve()