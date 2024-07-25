import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def baseline_correction(y, degree=3):
    """
    Corrects the baseline of a signal using polynomial fitting.
    
    Args:
        y (numpy array): Array of intensity values.
        degree (int): Degree of the polynomial for fitting.

    Returns:
        numpy array: Baseline-corrected intensity values.
    """
    x = np.arange(len(y))
    z = np.polyfit(x, y, degree)
    p = np.poly1d(z)
    return y - p(x)

# Define the folder path containing the CSV files
folder_path = r''

# List to store all peak detection results
all_results = []

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.csv'):  # Process only CSV files
            file_path = os.path.join(root, file)

            # Read the CSV file
            data = pd.read_csv(file_path)
            data.columns = ['Wavenumber', '1']
            data.columns = [col.strip() for col in data.columns]

            # Convert columns to numeric values
            wavenumber = pd.to_numeric(data['Wavenumber'], errors='coerce')
            intensity = pd.to_numeric(data['1'], errors='coerce')

            # Apply baseline correction
            intensity_corrected = baseline_correction(intensity)

            # Smooth the corrected intensity values
            smoothed_intensity = np.convolve(intensity_corrected, np.ones(10)/10, mode='same')

            # Detect peaks in the smoothed intensity data
            peaks_corrected, _ = find_peaks(smoothed_intensity, prominence=130, threshold=0, height=0)
            peak_wavenumbers_corrected = wavenumber[peaks_corrected]
            peak_intensities_corrected = smoothed_intensity[peaks_corrected]

            # Plot the spectrum with baseline correction and detected peaks
            plt.figure(figsize=(10, 6))
            plt.plot(wavenumber, smoothed_intensity, label='Spectrum with Baseline Correction')
            plt.plot(peak_wavenumbers_corrected, peak_intensities_corrected, "x", label='Peaks')
            plt.xlabel('Wavenumber (cm^-1)')
            plt.ylabel('Intensity (a.u.)')
            plt.title('Spectrum with Baseline Correction and Peaks')
            plt.ylim(bottom=-1000)
            plt.legend()
            plt.show()

            # Append the peak data to the results list
            for wn, intensity in zip(peak_wavenumbers_corrected, peak_intensities_corrected):
                all_results.append({'Filename': file, 'Peak Wavenumber (Corrected)': wn, 'Peak Intensity (Corrected)': intensity})

# Create a DataFrame from the results list
results_df = pd.DataFrame(all_results)

# Save the results to a CSV file
results_df.to_csv('peak_detection_resultsbox2.csv', index=False)
print("Results saved to peak_detection_resultsbox2.csv")

# Read the common peaks data from an Excel file
file = r'box1-2 common peaks.xlsx'
data = pd.read_excel(file)

# Count the frequency of each peak wavenumber
peak_counts = data.groupby('Peak Wavenumber (Corrected)').size().reset_index(name='Count')

# Sort the peak counts if needed
peak_counts = peak_counts.sort_values(by='Count', ascending=False)

# Save the peak counts to a CSV file
output_path = os.path.join(folder_path, 'all_peaks_frequency.csv')
peak_counts.to_csv(output_path, index=False)

print(f'Results saved to {output_path}')
