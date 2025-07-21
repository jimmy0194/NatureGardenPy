import json

# Load permissions from file
with open('permissions.json', 'r') as file:
    permissions = json.load(file)

# Expected Permissions by Role
expected_permissions = {
    "admin": {"read", "write", "delete", "manage_users"},
    "user": {"read", "write"},
    "guest": {"read"}
}

# Audit Function
def audit_permissions(actual, expected):
    for role, allowed_actions in actual.items():
        allowed_set = set(allowed_actions)
        expected_set = expected.get(role, set())
        if allowed_set != expected_set:
            print(f"\nRole: {role}")
            print(f"  Expected: {expected_set}")
            print(f"  Actual:   {allowed_set}")
            missing = expected_set - allowed_set
            extra = allowed_set - expected_set
            if missing:
                print(f"  Missing Permissions: {missing}")
            if extra:
                print(f"  Extra Permissions:   {extra}")
            print("  Status: Non-Compliant")
        else:
            print(f"\nRole: {role} is Compliant.")

# Run Audit
audit_permissions(permissions, expected_permissions)
