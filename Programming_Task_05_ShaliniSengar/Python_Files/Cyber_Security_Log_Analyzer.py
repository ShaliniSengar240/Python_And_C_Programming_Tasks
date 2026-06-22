# Cyber Security Log Analyzer

# Store login attempts in a list
login_attempts = ["Success", "Failed", "Failed",
                  "Success", "Failed", "Success"]

# Count total attempts
total_attempts = len(login_attempts)

# Initialize counters
successful_logins = 0
failed_logins = 0

# Count successful and failed logins using a loop
for attempt in login_attempts:
    if attempt == "Success":
        successful_logins += 1
    elif attempt == "Failed":
        failed_logins += 1

# Display results
print("Total Attempts:", total_attempts)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)
