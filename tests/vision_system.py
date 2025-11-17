from enes100 import enes100
from time import sleep

TEAM_NAME = "Guido"
TEAM_TYPE = "MATERIAL"      
ARUCO_ID = 7                # your ArUco marker number
ROOM_NUM = 1116             # 1116 or 1120, depending on your lab

# Begin communication with the Vision System
enes100.begin(TEAM_NAME, TEAM_TYPE, ARUCO_ID, ROOM_NUM)

# Wait until connected
while not enes100.is_connected():
    print("Connecting to Vision System...")
    sleep(1)

print("Connected!")

# Example: Print current coordinates
while True:
    print(f"x: {enes100.x:.2f}, y: {enes100.y:.2f}, theta: {enes100.theta:.2f}")
    sleep(1)
