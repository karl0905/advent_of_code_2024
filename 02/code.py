import pandas as pd

# read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

data = []
# iterate over each line and split the line by whitespace
for line in lines:
    parts = line.strip().split()
    data.append(parts)

# create a DataFrame
df = pd.DataFrame(data)
df = df.apply(pd.to_numeric, errors='coerce')

# remove NaN values from each row
rows = [[value for value in row if not pd.isna(value)]
        for _, row in df.iterrows()]

safe_reports = 0
# check if row is increasing or decreasing
for row in rows:
    MIN_DIFF = 1
    MAX_DIFF = 3

    if row[0] < row[1]:
        levels = "increasing"

    elif row[0] > row[1]:
        levels = "decreasing"
    else:
        continue

    is_safe = True

    for i in range(len(row)-1):
        current_value = row[i]
        next_value = row[i + 1]
        difference = abs(current_value - next_value)

        if (levels == "increasing" and
                current_value < next_value and
                MIN_DIFF <= difference <= MAX_DIFF):
            continue
        elif (levels == "decreasing" and
                current_value > next_value and
                MIN_DIFF <= difference <= MAX_DIFF):
            continue
        else:
            is_safe = False
            break

    if is_safe:
        safe_reports += 1

print(f"{safe_reports}")
