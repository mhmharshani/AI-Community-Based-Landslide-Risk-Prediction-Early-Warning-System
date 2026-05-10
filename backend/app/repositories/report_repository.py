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

def find_reports():
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
            return reports
    except FileNotFoundError:
        return []
    
def find_report_by_id(id):
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
            for report in reports:
                if report["id"] == id:
                    return report
                else :
                    continue
            return None
    except FileNotFoundError:
        return []