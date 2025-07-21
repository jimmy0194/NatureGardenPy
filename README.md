## NatureGarden Information Security Governance Compliance Tools

---

## **Project Purpose**
This folder contains **three Python-based tools** developed to demonstrate how automation can support **Information Security Governance, Risk, and Compliance (GRC)** activities for an organization like **NatureGarden**.  
These tools align with frameworks such as **ISO 27001**, **NIST Cybersecurity Framework (CSF)**, and **COBIT 5** to enhance:
- Continuous monitoring
- Risk management
- Incident detection
- Access control governance

---

## **Folder Structure**
/NatureGarden-SecurityGovernance-Tools
│
├── policy_checker.py # Tool 1: Policy Compliance Checker
├── log_scanner.py # Tool 2: Log Scanner
├── permissions_audit.py # Tool 3: Access Permissions Validator
│
├── sample_policies.json # Sample data for policies
├── sample_logs.txt # Sample data for logs
├── sample_permissions.json # Sample data for permissions
└── README.md # This Documentation File



---

#  **How to Run These Tools**

### **Prerequisites**
- Python 3.x installed
- VS Code or Terminal access to the project directory

---

### **Policy Compliance Checker**
#### **File:** `policy_checker.py`  
**Description:**  
Compares current security settings (password policies, MFA, lockout thresholds) against a defined policy (from JSON).  
Outputs whether each rule is **Compliant** or **Non-Compliant**.

## Why This Supports Governance, Risk, and Compliance (GRC) in Cybersecurity
---
These tools directly align with the principles of data security governance and compliance because they:

* Policy Compliance Checker Ensures systems comply with internal security policies and ISO/NIST standards (e.g., password/MFA).
* Log Scanner	Detects security events early for audit readiness and incident response (ISO 27001 A.16).
Permissions Audit	Enforces least-privilege and role-based access controls (ISO 27001 A.9, NIST AC-2).

## These tools:
* Assist risk management by identifying security gaps.
* Enable continuous compliance monitoring through automation.
* Provide evidence for audits and reporting.
* Reduce human error by automatically detecting issues.

## Mapping to Frameworks
* Standard / Framework	How These Tools Support It
* ISO 27001 (Annex A)	A.5-A.18: Policy, Access, Audit, Incidents
* NIST CSF	Identify, Protect, Detect, Respond
* COBIT 5	DSS05, DSS06: Risk Management, Security Monitoring


## Conclusion
* These scripts demonstrate how automation strengthens Information Security Governance at NatureGarden by:

* Improving visibility into security controls

* Reducing manual audit efforts

* Enabling proactive compliance and incident management
