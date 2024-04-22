import requests
import pandas as pd
import os

# Load the dataset
df = pd.read_csv('common_voice/cv-valid-dev.csv')

def transcribe_audio(file_path):
    url = 'http://localhost:8001/asr'
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        return response.json()

# Assuming the files are named in a column 'filename'
results = []
for index, row in df.iterrows():
    file_path = os.path.join('common_voice/cv-valid-dev', row['filename'])
    result = transcribe_audio(file_path)
    results.append(result)

df['generated_text'] = [res['transcription'] for res in results]

# Save updated dataframe
# df.to_csv('cv-valid-dev-updated.csv', index=False)
df.to_csv('cv-valid-dev.csv', index=False)
