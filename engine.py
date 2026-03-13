from .rules import check_dose

def run_checks(order): 
    issues = []

    for med in order.medications:
        dose_issue = check_dose(med)
        if dose_issue:
            issues.append({
                "level": "error",
                "message": dose_issue
            })

    severity = "high" if any(i["level"] == "error" for i in issues) else "low"
    return issues, severity
