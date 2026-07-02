# Project title
Post-Harvest Loss Prevention in Maize Production Systems

# Author

Name: Chananja Maswali Buyunge

Registration Number:BPE/D/2024/0019

Course: AGE219 – Basics of Computer Programming
Instructor name: Dr Kadeghe Fue
Institution: Sokoine University of Agriculture (SUA)

# Project Overview

This project was developed as part of the AGE219 Capstone Project. The objective is to apply Python programming, data mining, statistical analysis, and scientific visualization techniques to analyze weather conditions that may influence post-harvest loss in maize production systems.

The project demonstrates how weather variables such as precipitation, maximum temperature, minimum temperature, wind speed, and weather conditions can be analyzed using Python libraries including Pandas, NumPy, and Matplotlib.


# Problem Statement

Post-harvest loss is one of the major challenges affecting maize production. Poor weather conditions during harvesting, drying, transportation, and storage can increase grain moisture and promote fungal growth, insect infestation, and spoilage.

Understanding weather patterns helps farmers and agricultural engineers make informed decisions that reduce post-harvest losses and improve maize quality and food security.


# Project Objectives

# General Objective

To analyze weather data using Python and scientific visualization techniques in order to understand environmental conditions that may influence post-harvest loss in maize production systems.

# Specific Objectives

- Load and combine multiple datasets using Pandas.
- Clean and organize weather data.
- Perform statistical analysis on weather variables.
- Calculate descriptive statistics and correlations.
- Generate scientific visualizations using Matplotlib.
- Export analysis results and figures for reporting.


# Dataset Description

The project uses ten yearly weather datasets which were combined into one cleaned dataset named:

cleaned_sales.csv

The dataset contains the following variables:

| Variable | Description | Unit |
|-----------|-------------|------|
| precipitation | Daily rainfall | mm |
| temp_max | Maximum temperature | °C |
| temp_min | Minimum temperature | °C |
| wind | Wind speed | m/s |
| weather | Weather category | Text |


# Data Source

Weather datasets were collected from publicly available weather data sources and combined into a single cleaned dataset for analysis.

The original data consisted of ten CSV files representing multiple years of observations.


# Software and Libraries Used

- Python 3
- Visual Studio Code (VS Code)
- Pandas
- NumPy
- Matplotlib

# Methodology

The project followed these steps:

# Phase 1: Data Collection

- Obtained ten yearly weather datasets.
- Stored datasets in CSV format.

# Phase 2: Data Cleaning

- Loaded all datasets using Pandas.
- Combined datasets into one file.
- Removed duplicate records.
- Checked missing values.
- Saved the cleaned dataset as:

cleaned_sales.csv

# Phase 3: Statistical Analysis

The following statistical analyses were performed:

- Descriptive Statistics
- Mean
- Median
- Mode
- Standard Deviation
- Variance
- Minimum Values
- Maximum Values
- Correlation Matrix

The results were exported into the **Results** folder.

# Scientific Visualization

Eight scientific plots were generated using Matplotlib.

1. Maximum Temperature Trend
2. Minimum Temperature Trend
3. Rainfall Trend
4. Weather Category Comparison (Bar Chart)
5. Scatter Plot with Trend Line
6. Wind Speed Histogram
7. Rainfall Box Plot
8. Weather Category Pie Chart

Each figure includes:

- Descriptive title
- Axis labels
- Units
- Grid
- Legend (where applicable)

The figures were exported as PNG images.

# Results

The statistical analysis shows variation among rainfall, temperature, and wind speed throughout the observations.

The correlation analysis indicates the degree of relationship between different weather variables.

The scientific visualizations clearly demonstrate:

- Temperature trends over time.
- Rainfall variability.
- Distribution of wind speed.
- Frequency of different weather categories.
- Relationship between maximum and minimum temperatures.
- Possible rainfall outliers.

These findings provide useful information for understanding weather conditions that may influence maize drying and storage.

# Conclusion

The project successfully demonstrated the use of Python for agricultural data analysis.

Using Pandas, NumPy, and Matplotlib, the weather datasets were cleaned, analyzed, and visualized.

The generated statistical summaries and scientific plots provide useful information that can support agricultural decision-making and contribute to understanding environmental conditions related to post-harvest management.

Future work may combine weather information with actual post-harvest loss measurements to build predictive machine learning models.

# Project Structure

AGE219_Capstone_Project
│
├── YEAR1.csv
├── YEAR2.csv
├── YEAR3.csv
├── YEAR4.csv
├── YEAR5.csv
├── YEAR6.csv
├── YEAR7.csv
├── YEAR8.csv
├── YEAR9.csv
├── YEAR10.csv
│
├── cleaned_sales.csv
│
├── data_cleaning.py
├── statistical_analysis.py
├── visualization.py
│
├── Results
│   ├── descriptive_statistics.csv
│   ├── mean.csv
│   ├── median.csv
│   ├── mode.csv
│   ├── variance.csv
│   ├── standard_deviation.csv
│   ├── minimum.csv
│   ├── maximum.csv
│   └── correlation_matrix.csv
│
├── Plots
│   ├── Plot1_Maximum_Temperature_Trend.png
│   ├── Plot2_Minimum_Temperature_Trend.png
│   ├── Plot3_Rainfall_Trend.png
│   ├── Plot4_Weather_BarChart.png
│   ├── Plot5_Scatter_TrendLine.png
│   ├── Plot6_Histogram.png
│   ├── Plot7_BoxPlot.png
│   └── Plot8_PieChart.png
│
└── README.md


# Figures

# Figure 1

![Maximum Temperature Trend](Plots/Plot1_Maximum_Temperature_Trend.png)
# Figure 2

![Minimum Temperature Trend](Plots/Plot2_Minimum_Temperature_Trend.png)

# Figure 3

![Rainfall Trend](Plots/Plot3_Rainfall_Trend.png)

# Figure 4

![Weather Categories](Plots/Plot4_Weather_BarChart.png)

# Figure 5

![Scatter Plot](Plots/Plot5_Scatter_TrendLine.png)

# Figure 6

![Histogram](Plots/Plot6_Histogram.png)

# Figure 7

![Box Plot](Plots/Plot7_BoxPlot.png)

# Figure 8

![Pie Chart](Plots/Plot8_PieChart.png)


# Acknowledgements

I sincerely thank the Department of Agricultural Engineering, the School of Engineering and Technology, and the course instructor for providing guidance throughout this capstone project.


# Instructor Tag

@kadefue
