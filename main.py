import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Data from the provided table
data = {
    "Country": ["Qatar", "Kuwait", "United Arab Emirates", "Oman", "Jordan", "Bahrain", "Saudi Arabia",
                "Egypt", "Iran", "Israel", "Lebanon", "Yemen", "Iraq", "Syria"],
    "GPI2021": [1.605, 1.688, 1.848, 1.982, 1.916, 2.121, 2.376, 2.397, 2.637, 2.669, 2.797, 3.407, 3.257, 3.371],
    "Land Surface Temperature": [40.406681, 40.4061036, 44.3128752, 43.1890584, 35.5630906, 37.5434058,
                                 41.3134485, 36.8122301, 36.1253434, 34.3117709, 26.0646502, 41.0628148,
                                 38.1250696, 35.6878318],
    "Standardised Precipitation-Evapotranspiration Index": [-2.502014642, -2.633071087, -2.37082592,
                                                            -2.471065153, -1.823052105, -2.532947465,
                                                            -2.356992689, -1.835329204, -2.843789654,
                                                            -1.346503964, -0.998143821, -1.101908271,
                                                            -2.379461143, -1.900984134],
    "Terrestrial and marine protected areas (% of total territorial area)": [5.844564723, 10.71650911, 15.92366583,
                                                                            1.517705243, 4.47071857, 1.686399949,
                                                                            4.528371918, 11.55079649, 7.66652224,
                                                                            10.53908705, 0.805384038, 0.605801456,
                                                                            1.531328179, 0.662807729]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Initialize a dictionary to store the Pearson correlation results
correlations = {}

# Calculate Pearson correlation between GPI2021 and each environmental factor
for column in df.columns[2:]:  # Skip 'Country' and 'GPI2021'
    correlation, _ = pearsonr(df['GPI2021'], df[column])
    correlations[column] = correlation

# Convert the correlations to a DataFrame for easy plotting
correlation_df = pd.DataFrame(list(correlations.items()), columns=['Environmental Factor', 'Pearson Correlation'])

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.barh(correlation_df['Environmental Factor'], correlation_df['Pearson Correlation'], color='skyblue')
plt.xlabel('Pearson Correlation with GPI2021')
plt.title('Correlation between GPI2021 and Environmental Factors')
plt.tight_layout()

# Save the bar chart
plt.savefig("GPI_Environmental_Correlation_BarChart.png")

# Show the plot
plt.show()
