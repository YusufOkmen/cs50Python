import csv

femaleMember = []
maleMember = []

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\cs50Python\lecture6\filter\family.csv") as file:
    family = csv.DictReader(file)
    for member in family:
        if member["gender"] == "Female":
            femaleMember.append(member)
        elif member["gender"] == "Male":
            maleMember.append(member)
    
    print(femaleMember)
    print("\n")
    print(maleMember)