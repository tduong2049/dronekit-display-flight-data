
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

fileName = raw_input("Enter the file name to store flight data on: ")
outputFile = open(fileName, "w+")
print "\nWriting ouput to " + fileName + "\n"

drone_address = "/dev/ttyS0"

# Create a drone object after connecting to the address of the drone
print "Connecting to drone on: " + drone_address
drone = connect(drone_address, baud = 921600, wait_ready = True)

'''
# Sets the drone to GUIDED mode
print "\nSetting drone to GUIDED mode now..."
drone.mode = VehicleMode("GUIDED")
print "Drone is in GUIDED mode."

# Arm the drone
print"\nDrone is armable and is arming now..."
drone.armed = True
time.sleep(2)

# If the drone does not successfully arm,
# attempt to arm it again.
while not drone.armed:
    print("--Drone is still arming...")
    drone.armed = True
    time.sleep(2)
print("\nDrone is armed!")

# Set a target altitude for drone to take off and elevate to.
targetAltitude = 10.0
print "\nTarget altitude of " + str(targetAltitude) + "m has been set."
drone.simple_takeoff(targetAltitude)
'''

print "\nConnected to the drone on: " + drone_address
print "Press [CTRL + C] to stop recording data and end flight.\n"
iteration = 1
totalIteration = 1000

# For each iteration, write the drone's current latitude, longitude,
# altitude, pitch, yaw, and roll to the file at a frequency of 400Hz
# (Pixhawk's update rate)
try:
    while iteration <= totalIteration:
        if iteration == 1:
            outputFile.write(str(drone.location.global_relative_frame.lat) + ', ')
        else:
            outputFile.write('\n' + str(drone.location.global_relative_frame.lat) + ', ')

        outputFile.write(str(drone.location.global_relative_frame.lon) + ', ')
        outputFile.write(str(drone.location.global_relative_frame.alt) + ', ')
        outputFile.write(str(drone.attitude.pitch) + ', ')
        outputFile.write(str(drone.attitude.yaw) + ', ')
        outputFile.write(str(drone.attitude.roll))

        print "Completed Iteration: " + str(iteration)
        iteration += 1

        time.sleep(0.0025)
        
        '''
        print "\nLatitude: " + str(drone.location.global_relative_frame.lat)
        print "Longitude: " + str(drone.location.global_relative_frame.lon)
        print "Altitude: " + str(drone.location.global_relative_frame.alt)
        print "Pitch: " + str(drone.attitude.pitch)
        print "Yaw: " + str(drone.attitude.yaw)
        print "Roll: " + str(drone.attitude.roll)
        print "________________________________________"
        '''
except KeyboardInterrupt:
    pass


outputFile.close()

# Close vehicle object before exiting script
drone.close()

print("Completed data gathering.")