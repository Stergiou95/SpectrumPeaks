# Raman Spectroscopy Peak Detection and Aggregation

This script processes Raman spectroscopy data from multiple CSV files, corrects the baseline, smooths the signal, detects peaks, and aggregates the results into an overall file. It also counts the frequency of common peaks and saves the results to a CSV file.

## Features

- Baseline correction using polynomial fitting.
- Smoothing of intensity values using convolution.
- Peak detection with customizable parameters.
- Aggregation of detected peaks from multiple files.
- Counting and sorting of common peaks by wavenumber.
- Export of results to CSV files for further analysis.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- SciPy

## Installation

1. Clone the repository or download the script.
   ```sh
   git clone https://github.com/Stergiou95/SpectrumPeaks.git
