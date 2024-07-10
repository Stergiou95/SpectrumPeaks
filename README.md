#  Spectroscopy Peak Detection

This script processes  spectroscopy data to correct the baseline, smooth the signal, and detect peaks. It is designed to handle spectral data in CSV format and save the detected peaks to a new CSV file.

## Features

- Baseline correction using polynomial fitting.
- Smoothing of intensity values using convolution.
- Peak detection with customizable parameters.
- Visualization of the corrected spectrum and detected peaks.
- Export of detected peaks to a CSV file.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- SciPy

## Installation

1. Clone the repository or download the script.
   ```sh
   git clone https://github.com/USERNAME/REPOSITORY_NAME.git
