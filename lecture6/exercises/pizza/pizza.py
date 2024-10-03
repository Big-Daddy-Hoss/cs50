import csv
from tabulate import tabulate

menu = []

with open("sicilian.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append({"Sicilian Pizza": row["Sicilian Pizza"], 
                     "Small": row["Small"],
                     "Large": row["Large"]})

print(tabulate(menu, headers="keys", tablefmt="fancy_grid"))