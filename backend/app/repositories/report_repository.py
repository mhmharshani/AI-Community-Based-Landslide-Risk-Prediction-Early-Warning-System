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
            active_reports = []
            for report in reports:
                if report["is_deleted"] == False:
                    active_reports.append(report)
            return active_reports
    except FileNotFoundError:
        return []
    
def find_report_by_id(id):
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
            for report in reports:
                if report["id"] == id and report["is_deleted"] == False:
                    return report
                else :
                    continue
            return None
    except FileNotFoundError:
        return []
    
def remove_report_by_id(id):
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
        
            deleted_report = None

        for report in reports:

            if report["id"] == id:
                report["is_deleted"] = True
                deleted_report = report
                break

        with open(REPORTS_FILE, 'w') as file:
            json.dump(reports, file, indent=4)

        return deleted_report
    except FileNotFoundError:
        return []
    
def find_reports_by_risk(risk: str):
    try:
        with open(REPORTS_FILE, 'r') as file:
            reports = json.load(file)
            filtered_reports = []
            for report in reports:
                if report["risk"] == risk.upper() and report["is_deleted"] == False:
                    filtered_reports.append(report)
            return filtered_reports
    except FileNotFoundError:
        return []