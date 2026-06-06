import json

with open('dashboard_data.json', 'r') as f:
    data = json.load(f)

print(f'Total records in JSON: {len(data)}')
print(f'First record keys: {list(data[0].keys()) if data else "No data"}')
print(f'First record sample: {data[0] if data else "No data"}')
