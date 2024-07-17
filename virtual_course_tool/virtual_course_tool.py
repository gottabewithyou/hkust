import json
import requests
import pdfplumber
import re
from io import BytesIO

# Open and load the JSON file
with open("virtual_course.json") as file:
    raw_data = json.load(file)

data = raw_data["commonJsonList"]

SciMajors = {"DASC": "Data Analytics in Science",
             "CHEM": "Chemistry",
             "BCB": "Biochemistry and Cell Biology",
             "BIOT": "Biotechnology",
             "MATH": "Mathematics",
             "OST": "Ocean Science and Technology",
             "PHYS": "Physics"
}
EngMajors = {"BIEN": "Bioengineering",
             "CENG": "Chemical Engineering",
             "CEEV": "Chemical and Environmental Engineering",
             "SUSEE": "Sustainable Energy Engineering",
             "CIVL": "Civil Engineering",
             "CIEV": "Civil and Environmental Engineering",
             "CPEG": "Computer Engineering",
             "COMP": "Computer Science",
             "COSC": "Computer Science",
             "ELEC": "Electronic Engineering",
             "DA": "Decision Analytics",
             "IEEM": "Industrial Engineering and Engineering Management",
             "AE": "Aerospace Engineering",
             "MECH": "Mechanical Engineering"
}
BusiMajors = {"GBM": "General Business Management",
              "GBUS": "Global Business",
              "ACCT": "Professional Accounting",
              "ECON": "Economics",
              "ECOF": "Economics and Finance",
              "FINA": "Finance",
              "QFIN": "Quantitative Finance",
              "IS": "Information Systems",
              "OM": "Operations Management",
              "MGMT": "Management",
              "MARK": "Marketing"
}
HumaMajors = {"GCS": "Global China Studies",
              "QSA": "Quantitative Social Analysis"
}
AISMajors = {"EVMT": "Environmental Management and Technology",
             "IIM": "Individualized Interdisciplinary Major",
             "ISDN": "Integrative Systems and Design"
}
JoinedSchoolMajors = {"BIBU": "Biotechnology and Business",
                      "DSCT": "Data Science and Technology",
                      "MAEC": "Mathematics and Economics",
                      "RMBI": "Risk Management and Business Intelligence",
                      "SGFN": "Sustainable and Green Finance"
}

SciMinors = {"CHEM": "Chemistry",
             "BIOT": "Biotechnology",
             "ACTM": "Actuarial Mathematics",
             "MATH": "Mathematics",
             "ENVS": "Environmental Science",
             "ASCO": "Astrophysics and Cosmology",
             "PHYS": "Physics"
}
EngMinors = {"BIEN": "Bioengineering",
             "SC": "Smart City",
             "BDT": "Big Data Technology",
             "IT": "Information Technology", 
             "ROBO": "Robotics",
             "SUSEE": "Sustainable Energy Engineering",
             "AERO": "Aeronautical Engineering"
}
BusiMinors = {"BUS": "Business",
}
HumaMinors = {"CS": "China Studies",
              "HUMA": "Humanities",
              "SOSC": "Social Science"              
}
AISMinors = {"SUST": "Sustainability",
             "DESN": "Design"
}
JoinedSchoolMinors = {"ENTR": "Entrepreneurship",
                      "PBS": "Psychological and Behavioral Science"
}

AISExtm = {"AI": "Artificial Intelligence",
           "DMCA": "Digital Media and Creative Arts"
}

CommonCore = {"A": "Arts",
              "H": "Humanities",
              "SA": "Social Analytics",
              "S": "Science",
              "T": "Technology"
}

Type = {"Major": "Major",
        "Minor": "Minor",
        "Extm": "Extended Major",
        "CC": "Common Core"
}

def fetch_major():
    print("\nScience Majors:")
    for code, title in SciMajors.items():
        print(f"\t{code}: {title}")

    print("\nEngineering Majors:")
    for code, title in EngMajors.items():
        print(f"\t{code}: {title}")

    print("\nBusiness Majors:")
    for code, title in BusiMajors.items():
        print(f"\t{code}: {title}")

    print("\nHumanities Majors:")
    for code, title in HumaMajors.items():
        print(f"\t{code}: {title}")

    print("\nInterdisciplinary Majors:")
    for code, title in AISMajors.items():
        print(f"\t{code}: {title}")

    print("\nJoined School Majors:")
    for code, title in JoinedSchoolMajors.items():
        print(f"\t{code}: {title}")

def fetch_minor():
    print("\nScience Minors:")
    for code, title in SciMinors.items():
        print(f"\t{code}: {title}")

    print("\nEngineering Minors:")
    for code, title in EngMinors.items():
        print(f"\t{code}: {title}")

    print("\nBusiness Minors:")
    for code, title in BusiMinors.items():
        print(f"\t{code}: {title}")

    print("\nHumanities Minors:")
    for code, title in HumaMinors.items():
        print(f"\t{code}: {title}")

    print("\nInterdisciplinary Minors:")
    for code, title in AISMinors.items():
        print(f"\t{code}: {title}")

    print("\nJoined School Minors:")
    for code, title in JoinedSchoolMinors.items():
        print(f"\t{code}: {title}")

def fetch_extm():
    print("\nInterdisciplinary Extended Majors:")
    for code, title in AISExtm.items():
        print(f"\t{code}: {title}")

def fetch_cc():
    print("\nCommon Core:")
    for code, title in CommonCore.items():
        print(f"\t{code}: {title}")

for code, title in Type.items():
    print(f"\t{code}: {title}")

type_input = input("What type of programme do you want to search? ")

year = 24
match type_input.lower():
    case "major":
        fetch_major()
        input = input("Which major do you want to search? ")
        url = f"https://ugadmin.hkust.edu.hk/prog_crs/ug/20{year}{year+1}/pdf/{year}-{year+1}{input.lower()}.pdf"
    case "minor":
        fetch_minor()
        input = input("Which minor do you want to search? ")
        url = f"https://ugadmin.hkust.edu.hk/prog_crs/ug/20{year}{year+1}/pdf/minor-{input.lower()}.pdf"
    case "extm":
        fetch_extm()
        input = input("Which extended major do you want to search? ")
        url = f"https://ugadmin.hkust.edu.hk/prog_crs/ug/20{year}{year+1}/pdf/{year}-{year+1}extm-{input.lower()}.pdf"
    case "cc":
        fetch_cc()
        input = input("Which area of common core do you want to search? ")
        url = f"https://uce.ust.hk/web/resources/Course_List_30-credit_{input.upper()}.pdf"

# Fetch the document content
response = requests.get(url)

subj_in = []
code_in = []

with pdfplumber.open(BytesIO(response.content)) as pdf:
    total_pages = len(pdf.pages)
    text = ""

    for i in range(0, total_pages):
        page_obj = pdf.pages[i]
        text += page_obj.extract_text()

    pattern = r"([A-Z]+) (\d{4})"
    matches = re.findall(pattern, text)

    # Loop through all courses in the PDF
    for match in matches:
        if len(match[0]) == 4 and len(match[1]) == 4:
            if not (match[0] in subj_in and match[1] in code_in):
                subj_in.append(match[0])
                code_in.append(match[1])

sorted_data = sorted(data, key=lambda x: x["extOrgFormalDescr"])
uni_list = []
matched_courses = []

def append_course(item):
    # Check if the mapping's approved and it's a virtual course
    if item["apprvStatusCde"] == "APPROVED" and "virtual" in item["extOrgFormalDescr"].lower():
        course_str = f"\t{tr_course['incrseCde']} - {tr_course['incrseTitleTxt']}   to   {eqv_course['subject']}{eqv_course['catalogNbr']} - {eqv_course['crseTitle']}"
        # Handle stupid duplicated, identical mappings
        if course_str not in matched_courses:
            matched_courses.append(course_str)
            # To print the university name 1 time even if there're multiple courses
            if item["extOrgFormalDescr"] not in uni_list:
                uni_list.append(item["extOrgFormalDescr"])
                print(item["extOrgFormalDescr"])
            print(course_str)

for item in sorted_data:
    for tr_course in item["inCrseList"]:
        for eqv_course in item["hkustEqvCrseList"]:
            # If the codes in PDF matches the equivalent course code
            match input.upper():
                case "A":
                    if ((eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in)) or eqv_course["crseTitle"] == "Common Core Broadening Group in Arts":
                        append_course(item)
                case "H":
                    if ((eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in)) or eqv_course["crseTitle"] == "Common Core Broadening Group in Humanities":
                        append_course(item)
                case "S":
                    if ((eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in)) or eqv_course["crseTitle"] == "Common Core Broadening Group in Science":
                        append_course(item)
                case "SA":
                    if ((eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in)) or eqv_course["crseTitle"] == "Common Core Broadening Group in Social Analytics":
                        append_course(item)
                case "T":
                    if ((eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in)) or eqv_course["crseTitle"] == "Common Core Broadening Group in Technology":
                        append_course(item)
                case _: # Not CC
                    if (eqv_course["subject"], eqv_course["catalogNbr"]) in zip(subj_in, code_in):
                        append_course(item)