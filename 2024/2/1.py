from aocd import get_data
import pandas as pd

data = get_data(day=2, year=2024).split("\n")
df = pd.DataFrame([list(map(int, line.split())) for line in data])

def is_safe(row):
    differences = row.diff().dropna()

    increasing = (differences > 0).all()
    decreasing = (differences < 0).all()

    conditions_met = ((differences.abs() >= 1) & (differences.abs() <= 3)).all()

    return (increasing or decreasing) and conditions_met

results = df.apply(is_safe, axis=1)

print(results.sum())