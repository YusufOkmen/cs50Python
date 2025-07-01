import csv 

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\cs50Python\lecture6\csvFile\students.csv") as file:
    fileReader = csv.DictReader(file)

    # Analys subjects and their favourite count
    mathCounter, engCounter, peCounter, bioCounter = 0, 0, 0, 0

    for student in fileReader:
        if student["Favourite Subject"] == "Math":
            mathCounter += 1
        elif student["Favourite Subject"] == "English":
            engCounter += 1
        elif student["Favourite Subject"] == "P.E":
            peCounter += 1
        elif student["Favourite Subject"] == "Biology":
            bioCounter += 1

    print(f"Math: {mathCounter}")
    print(f"English: {engCounter}")
    print(f"P.E: {peCounter}")
    print(f"Biology: {bioCounter}")