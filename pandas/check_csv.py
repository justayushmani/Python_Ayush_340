from pathlib import Path
import pandas as pd

p = Path(r"C:/Python/Python_Ayush_340/pandas/data.csv")
print('Path:', p)
print('Exists:', p.exists())

try:
    df = pd.read_csv(p, on_bad_lines='skip', engine='python', encoding='utf-8')
    print('Loaded rows:', len(df))
    print(df.head())
except Exception as e:
    print('Error reading CSV:', repr(e))
