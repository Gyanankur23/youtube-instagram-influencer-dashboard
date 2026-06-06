import pandas as pd

xl = pd.ExcelFile('Youtube & Instagram influencers.xlsx')
print('Sheet names:', xl.sheet_names)

for sheet in xl.sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet)
    print(f'\n{sheet}: {len(df)} rows')
    print(df.head(10))
