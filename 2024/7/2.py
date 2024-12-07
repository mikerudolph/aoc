from aocd import get_data
import pandas as pd
import itertools

data = get_data(day=7, year=2024).split("\n")

records = []
for row in data:
    target, nums = row.split(":")
    target = int(target.strip())
    nums = list(map(int, nums.strip().split()))
    records.append({"target": target, "nums": nums})

df = pd.DataFrame(records)

def evaluate(nums, ops):
    result = nums[0]
    for op, val in zip(ops, nums[1:]):
        if op == "+":
            result = result + val
        elif op == "*":
            result = result * val
        else:
            result = int(str(result) + str(val))
    return result

def solve(target, nums):
    for combo in itertools.product(["+", "*", "||"], repeat=len(nums)-1):
        val = evaluate(nums, combo)
        if val == target:
            return True
    return False

df["valid"] = df.apply(lambda row: solve(row["target"], row["nums"]), axis=1)

print(df.loc[df["valid"], 'target'].sum())