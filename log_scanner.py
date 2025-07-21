def scan_logs(file_path, keywords):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    suspicious_entries = [line.strip() for line in lines if any(keyword.lower() in line.lower() for keyword in keywords)]

    print("\n--- Suspicious Entries Found ---")
    for entry in suspicious_entries:
        print(entry)

# Keywords to Search
keywords_to_find = ['failed login', 'unauthorized', 'error', 'critical', 'account locked']

# Run
scan_logs('logs.txt', keywords_to_find)
