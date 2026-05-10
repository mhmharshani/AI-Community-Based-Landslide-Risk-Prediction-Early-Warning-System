import json

REPORTS_FILE = 'app/data/reports.json' 
# Make sure reports.json is not empty by adding [] to it.

def save_report(report):
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
    except FileNotFoundError:
        reports = []
    reports.append(report)

    print("Saving report to file:", reports)

    with open(REPORTS_FILE, 'w') as file:
        json.dump(reports, file, indent=4)

    return report