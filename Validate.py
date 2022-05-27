import csv
from Applicant import Applicant

applicantList = []
newApps = []

def importTable():
    with open("YPM101Interview.csv", "r") as file:
        data = csv.reader(file, delimiter=",")
        for row in data:
            applicantList.append(row)
        """
        applicantList
        [
        row1 => [person1,person2,person3],
        row2 => [pos1,pos2,pos3],
        row3 => [pos1,pos2,pos3],
        row4 => [pos1,pos2,pos3],
        ...
        ]

        name = myName
        positions = [RG, GS, ...]

        apps(name, positions)
        """

    for i in range(len(applicantList[0])):
        name = applicantList[0][i]
        positions = []
        for j in range(1, len(applicantList)):
            positions.append(applicantList[j][i])
        newApps.append(Applicant(name, positions))
    for app in newApps:
        print(f"name='{app.name}' positions={app.positions}")

if __name__ == "__main__":
    importTable()
