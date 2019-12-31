from numpy import histogram
import matplotlib.pyplot as plt

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
    latitude.append(float(lat))
    longitude.append(float(lon))
    altitude.append(float(alt))
    pitch.append(float(pit))
    yaw.append(float(y))
    roll.append(float(r))

latFigure = plt.figure()
latAxis = latFigure.add_subplot(111)
latAxis.hist(latitude, 100)
latAxis.set_title("Latitude")

longFigure = plt.figure()
longAxis = longFigure.add_subplot(111)
longAxis.hist(longitude, 100)
longAxis.set_title("Longitude")

altFigure = plt.figure()
altAxis = altFigure.add_subplot(111)
altAxis.hist(altitude, 100)
altAxis.set_title("Altitude")

pitchFigure = plt.figure()
pitchAxis = pitchFigure.add_subplot(111)
pitchAxis.hist(pitch, 100)
pitchAxis.set_title("Pitch")

yawFigure = plt.figure()
yawAxis = yawFigure.add_subplot(111)
yawAxis.hist(yaw, 100)
yawAxis.set_title("Yaw")

rollFigure = plt.figure()
rollAxis = rollFigure.add_subplot(111)
rollAxis.hist(roll, 100)
rollAxis.set_title("Roll")

plt.show()