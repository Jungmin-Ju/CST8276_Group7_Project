import requests
import os
from datetime import datetime

def download_csv(url, output_path):
    """
    Downloads a CSV file from a given URL and saves it locally.
    """
    try:
        # Headers to simulate a real web browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Raise an error for failed requests
        
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f" Download complete! File saved as {output_path}")
        return output_path
    except Exception as e:
        print(f" Error downloading file: {e}")
        return None

if __name__ == "__main__":
    # Ontario COVID-19 Vaccine Data URL
    data_url = "https://data.ontario.ca/dataset/752ce2b7-c15a-4965-a3dc-397bf405e7cc/resource/2a362139-b782-43b1-b3cb-078a2ef19524/download/vaccines_by_age_phu.csv"

    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = f"vaccines_by_age_phu_{timestamp}.csv"

    download_csv(data_url, output_file)
