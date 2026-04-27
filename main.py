import time
import random

robots = [
    {"id": "Robot_1", "status": "IDLE", "battery": 100},
    {"id": "Robot_2", "status": "IDLE", "battery": 100},
    {"id": "Robot_3", "status": "IDLE", "battery": 100},
]

def simulate():
    for robot in robots:
        robot["battery"] -= random.randint(1, 5)

        if robot["battery"] < 20:
            robot["status"] = "LOW BATTERY"
        else:
            robot["status"] = random.choice(["IDLE", "WORKING"])

        print(f"{robot['id']} | {robot['status']} | Battery: {robot['battery']}%")

while True:
    simulate()
    print("-----")
    time.sleep(2)
