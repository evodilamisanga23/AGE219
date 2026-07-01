# PHASE 4: SCIENTIFIC VISUALIZATION
# Dataset: cleaned_sales.csv

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
data = pd.read_csv("cleaned_sales.csv")

# Plot 1: Maximum Temperature Trend
plt.figure(figsize=(10,5))

plt.plot(data["temp_max"],
         linewidth=2,
         label="Maximum Temperature")

plt.title("Trend of Maximum Temperature")
plt.xlabel("Observation Number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.savefig("Plot1_Maximum_Temperature_Trend.png", dpi=300)
plt.show()


# Plot 2: Minimum Temperature Trend
plt.figure(figsize=(10,5))

plt.plot(data["temp_min"],
         linewidth=2,
         label="Minimum Temperature")

plt.title("Trend of Minimum Temperature")
plt.xlabel("Observation Number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.savefig("Plot2_Minimum_Temperature_Trend.png", dpi=300)
plt.show()


# Plot 3: Rainfall Trend
plt.figure(figsize=(10,5))

plt.plot(data["precipitation"],
         linewidth=2,
         label="Rainfall")

plt.title("Trend of Rainfall")
plt.xlabel("Observation Number")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.legend()

plt.savefig("Plot3_Rainfall_Trend.png", dpi=300)
plt.show()


# Plot 4: Weather Category Comparison
weather = data["weather"].value_counts()

plt.figure(figsize=(8,5))

plt.bar(weather.index,
        weather.values,
        label="Weather Category")

plt.title("Weather Category Comparison")
plt.xlabel("Weather Type")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.savefig("Plot4_Weather_BarChart.png", dpi=300)
plt.show()


# Plot 5: Scatter Plot + Trend Line
x = data["temp_max"]
y = data["temp_min"]

plt.figure(figsize=(8,5))

plt.scatter(x,
            y,
            label="Observed Data")

m,b = np.polyfit(x,y,1)

plt.plot(x,
         m*x+b,
         linewidth=2,
         label="Trend Line")

plt.title("Maximum Temperature vs Minimum Temperature")
plt.xlabel("Maximum Temperature (°C)")
plt.ylabel("Minimum Temperature (°C)")
plt.grid(True)
plt.legend()

plt.savefig("Plot5_Scatter_TrendLine.png", dpi=300)
plt.show()

# Plot 6: Histogram
plt.figure(figsize=(8,5))

plt.hist(data["wind"],
         bins=20,
         edgecolor="black",
         label="Wind Speed")

plt.title("Distribution of Wind Speed")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Frequency")
plt.grid(True)
plt.legend()

plt.savefig("Plot6_Histogram.png", dpi=300)
plt.show()

# Plot 7: Box Plot
plt.figure(figsize=(6,5))

plt.boxplot(data["precipitation"])

plt.title("Box Plot of Rainfall")
plt.ylabel("Rainfall (mm)")
plt.grid(True)

plt.savefig("Plot7_BoxPlot.png", dpi=300)
plt.show()


# Plot 8: Pie Chart
plt.figure(figsize=(8,8))

plt.pie(weather.values,
        labels=weather.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Percentage Distribution of Weather Categories")

plt.savefig("Plot8_PieChart.png", dpi=300)
plt.show()

# Finish
print("="*50)
print("Scientific Visualization Completed Successfully.")
print("Eight plots have been generated and saved.")
print("="*50)
