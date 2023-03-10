import re
from fpdf import FPDF

def syllabus_input():
    subject = input("Enter the name of syllabus file: ")
    syllabus = open(subject, "r")
    syllabus = syllabus.read()
    syllabus = syllabus.split("\n")
    return syllabus

def segregatting_units(syllabus):
    units = []
    for i in range(len(syllabus)):
        if "Unit-I" in syllabus[i] or "Unit 1" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-II" in syllabus[i] or "Unit 2" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-III" in syllabus[i] or "Unit 3" in syllabus[i]:
            units.append(syllabus[i])
        elif "Unit-IV" in syllabus[i] or "Unit 4" in syllabus[i]:
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

def encode(unit_wise_syllabus):
    """This function encodes the syllabus to ignore the UnicodeEncodeError: 'latin-1' codec can't encode characters in position 334-335: ordinal not in range(256) error"""
    for i in unit_wise_syllabus:
        for j in range(len(unit_wise_syllabus[i])):
            for k in range(len(unit_wise_syllabus[i][j])):
                try:
                    unit_wise_syllabus[i][j][k] = unit_wise_syllabus[i][j][k].encode("latin-1", "ignore").decode("latin-1")
                except UnicodeEncodeError:
                    print(unit_wise_syllabus[i][j][k])
                    unit_wise_syllabus[i][j][k] = unit_wise_syllabus[i][j][k].encode("utf-8", "ignore").decode("utf-8")
    return unit_wise_syllabus

def pdf_print(unit_wise_syllabus, name = "syllabus.pdf"):    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    for i in unit_wise_syllabus:
        pdf.cell(200, 10, txt=i, ln=1, align="C")
        for j in unit_wise_syllabus[i]:
            for k in j:
                if k != "" :
                    pdf.cell(200, 10, txt=f"\t* {k}", ln=1, align="L")
    pdf.output(name)


def main():
    syllabus = syllabus_input()
    print(syllabus)
    units = segregatting_units(syllabus)
    unit_wise_syllabus = syllabus_unit_wise(units, syllabus)
    unit_wise_syllabus = processing_syllabus(unit_wise_syllabus)
    unit_wise_syllabus = encode(unit_wise_syllabus)
    output = input("Enter the name of output file: ")
    pdf_print(unit_wise_syllabus, output)

if __name__ == "__main__":
    main()
