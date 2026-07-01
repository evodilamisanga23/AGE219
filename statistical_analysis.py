# STATISTICAL ANALYSIS
# Dataset: cleaned_sales.csv

# Import libraries
import pandas as pd
import os

# Create Results folder
output_folder = "Results"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load Dataset
data = pd.read_csv("cleaned_sales.csv")

print("Dataset Loaded Successfully")
print()

# Display First Five Rows
print("FIRST FIVE ROWS")
print(data.head())

# Dataset Information
print("\nDATASET INFORMATION")
print(data.info())
# Missing Values
print("\nMISSING VALUES")
print(data.isnull().sum())

# Select Numerical Columns
num = data.select_dtypes(include="number")

# Descriptive Statistics
descriptive = num.describe()

print("\nDESCRIPTIVE STATISTICS")
print(descriptive)

descriptive.to_csv("Results/descriptive_statistics.csv")

# Mean
mean = num.mean()

print("\nMEAN")
print(mean)

mean.to_csv("Results/mean.csv")

# Median
median = num.median()

print("\nMEDIAN")
print(median)

median.to_csv("Results/median.csv")

# Mode
mode = num.mode()

print("\nMODE")
print(mode)

mode.to_csv("Results/mode.csv", index=False)

# Standard Deviation
std = num.std()

print("\nSTANDARD DEVIATION")
print(std)

std.to_csv("Results/standard_deviation.csv")

# Varian# ----------------------------------------------------------ce
variance = num.var()

print("\nVARIANCE")
print(variance)

variance.to_csv("Results/variance.csv")

# Minimum Values
minimum = num.min()

print("\nMINIMUM VALUES")
print(minimum)

minimum.to_csv("Results/minimum.csv")

# Maximum Values
maximum = num.max()

print("\nMAXIMUM VALUES")
print(maximum)

maximum.to_csv("Results/maximum.csv")

# Correlation Matrix
correlation = num.corr()

print("\nCORRELATION MATRIX")
print(correlation)

correlation.to_csv("Results/correlation_matrix.csv")

# Finish
print("\n=======================================")
print("Statistical Analysis Completed Successfully.")
print("All results have been saved in the 'Results' folder.")
