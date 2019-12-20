while True:
    try:
        fileName = raw_input("Enter the file name to be read: ")
        inputFile = open(fileName, 'r')
    except IOError:
        print "File '" + fileName + "' not found."
    else:
        break

latitude = []
longitude = []
altitude = []
pitch = []
yaw = []
roll = []

for line in inputFile:
    lat, lon, alt, pit, y, r = line.strip().split(", ")
    latitude.append(lat)
    longitude.append(lon)
    altitude.append(alt)
    pitch.append(pit)
    yaw.append(y)
    roll.append(r)

print latitude
print longitude
print altitude
print pitch
print yaw
print roll