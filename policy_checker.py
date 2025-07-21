import json

def load_policies(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def check_compliance(system_settings, policy_rules):
    compliance_report = {}
    for rule, expected in policy_rules.items():
        actual = system_settings.get(rule, None)
        compliance_report[rule] = {
            "Expected": expected,
            "Actual": actual,
            "Compliant": actual == expected
        }
    return compliance_report

def print_report(report):
    for rule, details in report.items():
        status = "Compliant" if details['Compliant'] else "Non-Compliant"
        print(f"{rule}:\n  Expected: {details['Expected']}\n  Actual:   {details['Actual']}\n  Status:   {status}\n")

# Example System Settings to Evaluate
current_system_settings = {
    "password_length_minimum": 10,
    "password_complexity_required": True,
    "account_lockout_threshold": 5,
    "multi_factor_authentication": False
}

# Run
policies = load_policies('policies.json')
report = check_compliance(current_system_settings, policies)
print_report(report)
