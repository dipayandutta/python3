import os
hostname = "google.com"

ping_status = os.system("ping -n 1 "+hostname)
print(ping_status)

if ping_status == 0:
    result = "Network Reachable"

else:
    result = "Unable to Reach remote destination"

print(result)
