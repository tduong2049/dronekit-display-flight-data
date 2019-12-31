import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

xs = []
ys = []
zs = []

for i in range(len(pitch)):
    xs.append(np.cos(pitch[i]) * np.cos(yaw[i]))
    ys.append(np.cos(pitch[i]) * np.sin(yaw[i]))
    zs.append(np.sin(pitch[i]))

ax.scatter(xs, ys, zs, c = "r", marker = ".")
ax.set_xlabel("cos(pitch) * cos(yaw)")
ax.set_ylabel("cos(pitch) * sin(yaw)")
ax.set_zlabel("sin(pitch)")

ax.set_xlim(-0.7, 0)
ax.set_ylim(0, 0.8)
ax.set_zlim(0, 0.01)

plt.show()