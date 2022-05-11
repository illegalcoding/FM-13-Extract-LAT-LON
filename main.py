import re

regex = r"(?<=99)(?P<LAT>\d\d\d)(?: ?(?P<QUADRANT>\d))(?:\d(?P<LON>\d\d\d))"
fm13 = input("INPUT FM-13: ")

matches = re.finditer(regex, fm13, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    LAT = match.group("LAT")
    LON = match.group("LON")
    QUADRANT = match.group("QUADRANT")
    LAT = LAT[:2] + "." + LAT[2:]
    LON = LON[:2] + "." + LON[2:]
    if int(QUADRANT) == 1:
        quadLat = "N"
        quadLon = "E"
    elif int(QUADRANT) == 3:
        quadLat = "S"
        quadLon = "E"
    elif int(QUADRANT) == 5:
        quadLat = "S"
        quadLon = "W"
    elif int(QUADRANT) == 7:
        quadLat = "N"
        quadLon = "W"
    else:
        print("Invalid Quadrant")
        exit()
    print("LAT", LAT, quadLat)
    print("LON", LON, quadLon)
