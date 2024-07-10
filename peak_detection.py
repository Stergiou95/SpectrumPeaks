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

# Define the file name and path
file_name = "example.csv"
file_path = os.path.join("C:/Users/..")

# Read the file
data = pd.read_csv(file_path, sep=';', decimal=',')

# Set the column names
data.columns = ['Wavrnumbers', 'Intensity']

# Parse the data as numeric values
wavenumber = pd.to_numeric(data['Wavrnumbers'], errors='coerce')
intensity = pd.to_numeric(data['Intensity'], errors='coerce')

# Apply baseline correction
intensity_corrected = baseline_correction(intensity)

# Smooth the data using convolution
intensity_smoothed = np.convolve(intensity_corrected, np.ones(10)/10, mode='same')

# Find peaks in the smoothed data
peaks, _ = find_peaks(intensity_smoothed, prominence=1000, height=50, threshold=10) #Modife the params for the detection of peaks 
peak_wavenumber = wavenumber[peaks]
peak_intensity = intensity_smoothed[peaks]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(wavenumber, intensity_smoothed, label='Corrected and Smoothed Intensity')
plt.plot(peak_wavenumber, peak_intensity, "x", label='Peaks', color='red')
plt.xlabel('Wavenumber (cm^-1)')
plt.ylabel('Intensity (a.u.)')
plt.title('Spectrum with Baseline Correction and Peaks')
plt.ylim(bottom=-1000)
plt.legend()
plt.show()

# Save peaks to CSV
peaks_data = pd.DataFrame({'Wavenumber': peak_wavenumber, 'Intensity': peak_intensity})
peaks_file_name = "peaks.csv"
peaks_file_path = os.path.join("C:/Users/..", peaks_file_name)
peaks_data.to_csv(peaks_file_path, index=False)
