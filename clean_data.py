import pandas as pd
import os
from datetime import datetime

def get_latest_csv():
    today_date = datetime.now().strftime("%Y%m%d")
    filename = f"vaccines_by_age_phu_{today_date}.csv"

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Error: {filename} not found in directory.")

    return filename

def clean_data(input_csv, output_csv):
    """
    Cleans the dataset by removing duplicates, handling missing values, 
    and renaming columns to match the database format.
    """
    df = pd.read_csv(input_csv)

    # Debugging: Print column names
    print("Detected Columns:", df.columns.tolist())

    # Check if expected columns exist
    expected_columns = ["PHU name", "Agegroup"]
    missing_columns = [col for col in expected_columns if col not in df.columns]

    if missing_columns:
        raise KeyError(f"Missing columns in dataset: {missing_columns}")

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove rows with missing critical data
    df.dropna(subset=expected_columns, inplace=True)

    # Rename columns to match Oracle database table format
    df.rename(columns={
        "PHU name": "phu_name",
        "Agegroup": "age_group",
        "Date": "record_date",
        "PHU ID": "phu_id",
        "At least one dose_cumulative": "at_least_one_dose_cumulative",
        "Second_dose_cumulative": "second_dose_cumulative",
        "fully_vaccinated_cumulative": "fully_vaccinated_cumulative",
        "third_dose_cumulative": "third_dose_cumulative",
        "Total population": "total_population",
        "Percent_at_least_one_dose": "percent_at_least_one_dose",
        "Percent_fully_vaccinated": "percent_fully_vaccinated",
        "Percent_3doses": "percent_3doses"
    }, inplace=True)

    # Convert 'record_date' to standard date format
    df['record_date'] = pd.to_datetime(df['record_date'])

    # Save the cleaned data
    df.to_csv(output_csv, index=False)

    print(f"Cleaned data saved to {output_csv}")

if __name__ == "__main__":
    latest_csv = get_latest_csv()
    print(f"Using latest file: {latest_csv}")
    clean_data(latest_csv, "vaccines_by_age_phu_cleaned.csv")
