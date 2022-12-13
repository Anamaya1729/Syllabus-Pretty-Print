import re

def syllabus_input():
    # subject = input("Enter the name of syllabus file: ")
    # syllabus = open(subject, "r")
    syllabus = open("web_mining.txt", "r")
    syllabus = syllabus.read()
    syllabus = syllabus.split("\n")
    return syllabus

def segregatting_units(syllabus):
    units = []
    for i in range(len(syllabus)):
        if "Unit-I" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-II" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-III" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-IV" in syllabus[i]:
            units.append(syllabus[i])
    return units

def syllabus_unit_wise(units, syllabus):
    unit_wise_syllabus = {}
    for i in range(len(units)):
        if i == len(units)-1:
            unit_wise_syllabus[units[i]] = syllabus[syllabus.index(units[i])+1:]
        else:   
            unit_wise_syllabus[units[i]] = syllabus[syllabus.index(units[i])+1:syllabus.index(units[i+1])]

    return unit_wise_syllabus

def processing_syllabus(unit_wise_syllabus):
    for i in unit_wise_syllabus.keys():
        for j in range(len(unit_wise_syllabus[i])):
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO1]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO2]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO3]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO4]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO5]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("[CO2", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("CO3]", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].replace("\n", "")
            unit_wise_syllabus[i][j] = unit_wise_syllabus[i][j].strip()
            unit_wise_syllabus[i][j] = re.split(r'[,.]', unit_wise_syllabus[i][j])
    return unit_wise_syllabus

def pretty_print(unit_wise_syllabus):
    for i in unit_wise_syllabus:
        print(i)
        for j in unit_wise_syllabus[i]:
            for k in j:
                if k != "" :
                    print(f"\t* {k}", end="\n")

def main():
    syllabus = syllabus_input()
    # print(syllabus)
    units = segregatting_units(syllabus)
    unit_wise_syllabus = syllabus_unit_wise(units, syllabus)
    unit_wise_syllabus = processing_syllabus(unit_wise_syllabus)
    pretty_print(unit_wise_syllabus)

if __name__ == "__main__":
    main()