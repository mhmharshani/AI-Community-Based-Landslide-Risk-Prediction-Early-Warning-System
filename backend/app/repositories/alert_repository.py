import json

ALERTS_FILE = 'app/data/alerts.json' 
# Make sure alerts.json is not empty by adding [] to it.

def save_alert(alert):
    try:
        with open(ALERTS_FILE, 'r') as file:
            alerts = json.load(file)
    except FileNotFoundError:
        alerts = []
    alerts.append(alert)

    print("Saving alert to file:", alerts)

    with open(ALERTS_FILE, 'w') as file:
        json.dump(alerts, file, indent=4)

    return alert