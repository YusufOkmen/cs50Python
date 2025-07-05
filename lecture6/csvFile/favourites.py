import csv 

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\cs50Python\lecture6\csvFile\students.csv") as file:
    fileReader = csv.DictReader(file)
    counts = {}

    for student in fileReader:
        favourite = student["Favourite Subject"]
        if favourite in counts:
            counts[favourite] += 1
        else:
            counts[favourite] = 1

# Show favourited subject by highest to lowest.
fSubject = input("Enter a subject ")
print(f"{fSubject}: {counts[fSubject]}")