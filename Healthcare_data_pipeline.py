import pandas as pd
import numpy as np

# Healthcare provider dataset simulation & extraction
raw_data = {
    'Clinic_Name': ['City Health Clinic ', 'CarePlus Diagnostics', 'Wellness Family Practice', 'Metro Dental Care ', 'Apollo Health Centre'],
    'Location': ['Pune', 'Mumbai', 'Pune', 'Nagpur', 'Mumbai'],
    'Contact': ['+91 9876543210', '+91 9123456789', '+91 9988776655', '+91 9811223344', None],
    'Specialty': ['General Practice', 'Pathology', 'Family Medicine', 'Dentistry', 'General Practice'],
    'Daily_Patients': [45, 120, 30, 25, 200]
}

# Create DataFrame
df = pd.DataFrame(raw_data)

# Data Cleaning & Preprocessing
df['Clinic_Name'] = df['Clinic_Name'].str.strip()  # Remove unwanted spaces
df['Contact'] = df['Contact'].fillna('Not Available')  # Handle missing values

# Data Transformation & Intelligence Summary
total_clinics = len(df)
pune_clinics = df[df['Location'] == 'Pune']

print("=== CLEANED HEALTHCARE DATASET ===")
print(df)
print("\n=== SUMMARY INSIGHTS ===")
print(f"Total Clinics Processed: {total_clinics}")
print(f"Clinics in Pune: {len(pune_clinics)}")

# Save output to CSV file
df.to_csv('healthcare_providers_cleaned.csv', index=False)
print("\nCleaned dataset exported to 'healthcare_providers_cleaned.csv' successfully!")