import json

with open('dashboard_data.json', 'r') as f:
    data = json.load(f)

print(f'Total records: {len(data)}')

# Count records with valid names
valid_names = 0
invalid_names = 0
for d in data:
    name = d.get('name') or d.get('Name') or ''
    if name and name.strip():
        valid_names += 1
    else:
        invalid_names += 1

print(f'Records with valid names: {valid_names}')
print(f'Records without valid names: {invalid_names}')

# Show first 10 names
print('\nFirst 10 names:')
for i, d in enumerate(data[:10]):
    name = d.get('name') or d.get('Name') or 'NO NAME'
    print(f'{i+1}. {name}')
