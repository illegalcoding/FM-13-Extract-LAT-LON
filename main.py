import re
import math

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

    latDeg = math.floor(float(LAT))
    latMin = float(float('0.' + LAT.split('.')[1]) * 60)
    if(latMin.is_integer() == False):
        latSec = float(float('0.' + str(latMin).split('.')[1]) * 60)
    else:
        latSec = 00.0
    lonDeg = math.floor(float(LON))
    lonMin = float(float('0.' + LON.split('.')[1]) * 60)
    if(lonMin.is_integer() == False):
        lonSec = float(float('0.' + str(lonMin).split('.')[1]) * 60)
    else:
        lonSec = 00.0
    if(latMin.is_integer() == True):
        latMin = int(latMin)
    if(lonMin.is_integer() == True):
        lonMin = int(lonMin)
    url = "https://www.google.com/maps/place/" + str(latDeg) + '°' + str(latMin) + "'" + str(latSec) + '"' + str(quadLat) + '+' + str(lonDeg) + '°' + str(lonMin) + "'" + str(lonSec) + '"' + str(quadLon)
    print("Google maps URL: " + url)
# 43 Degrees
# 180 minutes
# 0 Seconds