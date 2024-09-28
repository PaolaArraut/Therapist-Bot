import pandas as pd
from bs4 import BeautifulSoup
import re

csv_files = ['Dataset.csv', 'counselchat-data.csv', 'counsel_chat2.csv']

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.encode('latin1', 'replace').decode('utf8', 'replace')
    text = re.sub(r'[^A-Za-z0-9\s]', "", text)
    return text

for file in csv_files:
    df = pd.read_csv(file)
    
    df = df.fillna('')
    for column in df.columns:
        df[column] = df[column].astype(str).apply(clean_text)
    
    print(f"Processed DataFrame from {file}:")
    print(df)

    df.to_csv(f'cleaned_{file}', index=False)
