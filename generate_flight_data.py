import numpy as np
import pandas as pd

# Define the number of samples
num_samples = 1000

# Generate synthetic data for features (temperature, precipitation, wind speed)
temperature = np.random.randint(10, 35, num_samples)  # Temperature in Celsius
precipitation = np.random.rand(num_samples) * 10  # Precipitation in mm
wind_speed = np.random.randint(5, 25, num_samples)  # Wind speed in km/h

# Generate synthetic data for the target variable (delayed or not delayed)
delay_prob = np.random.rand(num_samples)  # Probability of delay
delayed = (delay_prob > 0.5).astype(int)  # 1 if delayed, 0 if not delayed

# Create a DataFrame to store the synthetic dataset
flight_data = pd.DataFrame({
    'Temperature (°C)': temperature,
    'Precipitation (mm)': precipitation,
    'Wind Speed (km/h)': wind_speed,
    'Delayed': delayed
})

# Save the dataset to a CSV file
flight_data.to_csv('flight_data.csv', index=False)
