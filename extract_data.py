import pandas as pd
import json

df = pd.read_csv('cleaned_data.csv')

# Clean and normalize data
df['Core_Area_Clean'] = df['Core_Area'].str.strip().str.upper()
df['Core_Area_Clean'] = df['Core_Area_Clean'].apply(lambda x: 
    'JEE' if 'JEE' in x and 'NEET' not in x else 
    'NEET' if 'NEET' in x and 'JEE' not in x else 
    'JEE/NEET' if 'JEE' in x and 'NEET' in x else 
    'OTHER')

df['Subject_Clean'] = df['Subject'].apply(lambda x: 
    'Physics' if str(x) in ['2', 'Physics'] else 
    'Chemistry' if str(x) in ['3', 'Chemistry'] else 
    'Mathematics' if str(x) in ['4', 'Maths', 'Mathematics'] else 
    'Biology' if str(x) in ['1', 'Biology', 'Bio'] else 
    'General' if str(x) in ['0', 'General'] else 
    'Other')

df['Cross_Platform_Clean'] = df['Cross_Platform'].str.strip().str.lower().apply(lambda x: 
    'Yes' if x in ['yes', 'y'] else 'No')

df_final = df[['name', 'Channel_Name', 'Platform', 'Start_Year', 'Follower/Subscriber_count', 
               'Avg_Views_count', 'Core_Area_Clean', 'Subject_Clean', 'Key_points', 
               'Cross_Platform_Clean', 'Cross_Platform_Type', 'Uploaded by', 'Engagement_Rate']]

df_final.columns = ['name', 'channel', 'platform', 'start_year', 'subscribers', 
                    'avg_views', 'core_area', 'subject', 'key_points', 'cross_platform', 
                    'cross_type', 'auditor', 'engagement_rate']

records = df_final.to_dict(orient='records')

with open('dashboard_data.json', 'w') as f:
    json.dump(records, f, default=str)

print(f'Exported {len(records)} records to dashboard_data.json')
