import requests
import json

# API endpoint for first rows
url = "https://datasets-server.huggingface.co/first-rows?dataset=sijieaaa%2FUAVScenes&config=default&split=train"

# Make GET request
response = requests.get(url)

# Check for successful request
if response.status_code == 200:
    data = response.json()
    rows = data.get("rows", [])
    
    print(f">>> Retrieved {len(rows)} rows from UAVScenes preview\n")
    
    # Print a preview of the first few rows
    for i, row in enumerate(rows[:5]):  # limit to first 5 rows
        print(f"Row {i+1}:")
        for k, v in row.items():
            print(f"  {k}: {v}")
        print("-" * 40)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
