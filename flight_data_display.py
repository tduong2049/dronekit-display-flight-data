
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

drone_address = "/dev/ttyS0"

# Create a drone object after connecting to the address of the drone
print "Connecting to drone on: " + drone_address
drone = connect(drone_address, baud = 921600 wait_ready = True)

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

outputFile = open("output.txt", "w+")
print "\nWriting ouput to 'output.txt'"
print "Press [CTRL + C] to stop recording data and end flight."

# Loop for displaying the drone's lat, long, alt, pitch, yaw, and roll
# can be broken when user presses CTRL + C
try:
    while True:
        outputFile.write("\nLatitude: \t" + str(drone.location.global_relative_frame.lat))
        outputFile.write("\nLongitude: \t" + str(drone.location.global_relative_frame.lon))
        outputFile.write("\nAltitude: \t" + str(drone.location.global_relative_frame.alt))
        outputFile.write("\nPitch: \t\t" + str(drone.attitude.pitch))
        outputFile.write("\nYaw: \t\t" + str(drone.attitude.yaw))
        outputFile.write("\nRoll: \t\t" + str(drone.attitude.roll))
        outputFile.write("\n________________________________________")
        
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

print("Completed")