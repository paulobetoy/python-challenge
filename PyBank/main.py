import os, csv
csv_path = os.path.join("../Resources","budget_data.csv")
with open (csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
csv_header =next(csvfile)
print(f"Header: {csv_header}")
counter = 0
for row in csvreader:
    fiber_grams 