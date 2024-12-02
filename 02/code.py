import pandas as pd

# read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# iterate over each line
data = []
for line in lines:
    # split the line by whitespace, but keep the original structure
    parts = line.strip().split()
    data.append(parts)

# create a DataFrame
df = pd.DataFrame(data)

# if you need to convert to numeric where possible:
df = df.apply(pd.to_numeric, errors='coerce')

# remove NaN values from each row, keeping only non-NaN values
rows = [[value for value in row if not pd.isna(value)]
        for _, row in df.iterrows()]

# check if row is increasing or decreasing
for row in rows:
    for i in range(len(row)-1):
        current_value = row[i]
        next_value = row[i + 1]

        if current_value < next_value and next_value - current_value >= 3:
            print(f"{current_value} is less that {next_value} with less or exact 3")
