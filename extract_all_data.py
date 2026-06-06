import pandas as pd
import json
import numpy as np
from datetime import datetime

# Read both sheets
xl = pd.ExcelFile('Youtube & Instagram influencers.xlsx')

youtube_df = pd.read_excel(xl, sheet_name='Youtube')
instagram_df = pd.read_excel(xl, sheet_name='Instagram')

print(f'YouTube sheet: {len(youtube_df)} rows')
print(f'Instagram sheet: {len(instagram_df)} rows')

# Add platform column
youtube_df['Platform'] = 'YouTube'
instagram_df['Platform'] = 'Instagram'

# Normalize column names (case insensitive)
youtube_df.columns = youtube_df.columns.str.strip()
instagram_df.columns = instagram_df.columns.str.strip()

# Combine both datasets
combined_df = pd.concat([youtube_df, instagram_df], ignore_index=True)

print(f'Total combined records: {len(combined_df)}')

# Replace NaN and datetime with None using a custom function
def replace_nan(obj):
    if isinstance(obj, dict):
        return {k: replace_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_nan(item) for item in obj]
    elif isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    elif pd.isna(obj):
        return None
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return obj

# Export to JSON without any processing
records = combined_df.to_dict(orient='records')
records = replace_nan(records)

with open('dashboard_data.json', 'w') as f:
    json.dump(records, f)

print(f'Exported {len(records)} records to dashboard_data.json')
