import csv
import random
import time

OUTPUT_FILE = "fleet_report.csv"

robots = [
    {"id": "Robot_1", "status": "IDLE", "battery": 100, "task": "None"},
    {"id": "Robot_2", "status": "IDLE", "battery": 100, "task": "None"},
    {"id": "Robot_3", "status": "IDLE", "battery": 100, "task": "None"},
]

tasks = [
    "Inspect part",
    "Move material",
    "Scan work area",
    "Return to charging station",
]


def assign_task(robot):
    if robot["battery"] < 20:
        robot["status"] = "LOW BATTERY"
        robot["task"] = "Return to charging station"
    else:
        robot["status"] = random.choice(["IDLE", "WORKING"])
        robot["task"] = random.choice(tasks)


def update_telemetry(robot):
    battery_drain = random.randint(1, 8)
    robot["battery"] = max(robot["battery"] - battery_drain, 0)

    if robot["battery"] == 0:
        robot["status"] = "OFFLINE"
        robot["task"] = "None"
    elif random.randint(1, 20) == 1:
        robot["status"] = "FAULT"
        robot["task"] = "Maintenance required"
    else:
        assign_task(robot)


def check_alerts(robot):
    alerts = []

    if robot["battery"] < 20 and robot["status"] != "OFFLINE":
        alerts.append("LOW BATTERY")

    if robot["status"] == "FAULT":
        alerts.append("FAULT DETECTED")

    if robot["status"] == "OFFLINE":
        alerts.append("ROBOT OFFLINE")

    return alerts


def write_report(rows):
    with open(OUTPUT_FILE, mode="w", newline="") as file:
        fieldnames = ["RobotID", "Status", "Battery", "Task", "Alerts"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def run_simulation(cycles=5):
    report_rows = []

    for cycle in range(1, cycles + 1):
        print(f"\n--- Cycle {cycle} ---")

        for robot in robots:
            update_telemetry(robot)
            alerts = check_alerts(robot)

            alert_text = ", ".join(alerts) if alerts else "None"

            print(
                f'{robot["id"]} | {robot["status"]} | '
                f'Battery: {robot["battery"]}% | '
                f'Task: {robot["task"]} | Alerts: {alert_text}'
            )

            report_rows.append({
                "RobotID": robot["id"],
                "Status": robot["status"],
                "Battery": robot["battery"],
                "Task": robot["task"],
                "Alerts": alert_text
            })

        time.sleep(1)

    write_report(report_rows)

    print("\nFleet Simulation Complete")
    print(f"Report Generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_simulation()
