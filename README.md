# Robot Fleet Monitor

A Python-based robot fleet monitoring simulation that models robot status, telemetry, task assignment, and operator alerts.

## Purpose

This project was built to demonstrate basic robotics software concepts related to fleet management, telemetry monitoring, task scheduling, and diagnostic alerting.

## Tools Used

- Python
- CSV report generation
- Randomized telemetry simulation
- Conditional logic
- Iterative control loops
- Basic state management

## Features

- Simulates multiple robots in a fleet
- Updates robot battery levels over time
- Assigns operational tasks based on robot condition
- Tracks robot status such as IDLE, WORKING, LOW BATTERY, FAULT, and OFFLINE
- Generates alerts for low battery, faults, and offline status
- Exports fleet activity to a CSV report

## Example Output

```text
--- Cycle 1 ---
Robot_1 | WORKING | Battery: 96% | Task: Inspect part | Alerts: None
Robot_2 | IDLE | Battery: 94% | Task: Move material | Alerts: None
Robot_3 | FAULT | Battery: 92% | Task: Maintenance required | Alerts: FAULT DETECTED
```

## How to Run
```bash
python main.py
```


