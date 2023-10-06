import pandas as pd
import numpy as np
import csv
data = pd.read_csv('Crop_recommendation.csv')


# class Crop:
#     def __init__(self, crop_data):
#         self.crop_data = crop_data

#     def get_min_max_first_row(self):
#         if not self.crop_data:
#             return None, None
        
#         first_row = self.crop_data[0]
#         if not first_row:
#             return None, None
        
#         min_value = min(first_row)
#         max_value = max(first_row)
        
#         return min_value, max_value

#     def get_min_max_by_label(self, label):
#         if not self.crop_data:
#             return None, None
        
#         values = [row for row in self.crop_data if label in row]
#         if not values:
#             return None, None

#         label_values = [row[1] for row in values]
#         min_value = min(label_values)
#         max_value = max(label_values)

#         return min_value, max_value

# def get_crop_data_from_user():
#     crop_data = []
#     num_rows = int(input("Enter the number of rows of crop data: "))
    
#     for i in range(num_rows):
#         row = input(f"Enter space-separated values for row {i+1}: ").split()
#         row = [int(value) for value in row]
#         crop_data.append(row)
    
#     return crop_data

# def add_label_to_crop_data(crop_data, values, label):
#     for row in crop_data:
#         if all(val in row for val in values):
#             row.append(label)

# # Example test case:
# crop_data = get_crop_data_from_user()
# crop = Crop(crop_data)

# # Add a label to values [10, 20, 30] in the crop data
# values_to_label = [10, 20, 30]
# label = "SampleLabel"
# add_label_to_crop_data(crop_data, values_to_label, label)

# min_value, max_value = crop.get_min_max_by_label(label)
# if min_value is not None and max_value is not None:
#     print(f"Minimum value with label '{label}': {min_value}")
#     print(f"Maximum value with label '{label}': {max_value}")
# else:
#     print(f"No values found with label '{label}'.")





import pandas as pd

def get_suitable_crops(nutrient_values):
    nitrogen, phosphorus, potassium = nutrient_values
    
    # Read crop recommendation data from CSV file
    crop_data = pd.read_csv("Crop_recommendation.csv")

    # Filter crops based on nutrient values
    filtered_crops = crop_data[
        (crop_data['N'] >= nitrogen) &
        (crop_data['P'] >= phosphorus) &
        (crop_data['K'] >= potassium)
    ]

    # Create a dictionary to store suitable temperature ranges for each crop
    crop_temperature_ranges = {}

    # Iterate through filtered crops and extract temperature information
    for _, row in filtered_crops.iterrows():
        crop_name = row['Crop']
        min_temp = row['Min_Temperature']
        max_temp = row['Max_Temperature']

        if crop_name not in crop_temperature_ranges:
            crop_temperature_ranges[crop_name] = []

        crop_temperature_ranges[crop_name].append([min_temp, max_temp])

    return crop_temperature_ranges

# Input nutrient values as a list
nutrient_values = [70, 40, 60]  # Example values for Nitrogen, Phosphorus, Potassium

# Get suitable crops and their temperature ranges
suitable_crops = get_suitable_crops(nutrient_values)

# Print the result
for crop, temperature_ranges in suitable_crops.items():
    print(f"Crop: {crop}")
    print("Temperature Ranges:")
    for i, temp_range in enumerate(temperature_ranges):
        print(f"Range {i+1}: Min = {temp_range[0]}, Max = {temp_range[1]}")
    print()




# Read crop recommendation data from CSV file
crop_data = pd.read_csv("Crop_recommendation.csv")

# Find minimum and maximum values for Nitrogen, Phosphorus, and Potassium
min_nitrogen = crop_data['N'].min()
max_nitrogen = crop_data['N'].max()

min_phosphorus = crop_data['P'].min()
max_phosphorus = crop_data['P'].max()

min_potassium = crop_data['K'].min()
max_potassium = crop_data['K'].max()

# Print the results
print(f"Minimum Nitrogen Value: {min_nitrogen}")
print(f"Maximum Nitrogen Value: {max_nitrogen}")
print(f"Minimum Phosphorus Value: {min_phosphorus}")
print(f"Maximum Phosphorus Value: {max_phosphorus}")
print(f"Minimum Potassium Value: {min_potassium}")
print(f"Maximum Potassium Value: {max_potassium}")







import pandas as pd

# Read crop recommendation data from CSV file
crop_data = pd.read_csv("Crop_recommendation.csv")

# Input the crop name for which you want to find nutrient values
crop_name = input("Enter the crop name: ")

# Filter the dataset to get data for the specified crop
crop_data_for_crop = crop_data[crop_data['Crop'] == crop_name]

# Check if the crop exists in the dataset
if crop_data_for_crop.empty:
    print(f"Crop '{crop_name}' not found in the dataset.")
else:
    # Get the minimum and maximum values of Nitrogen, Phosphorus, and Potassium for the specified crop
    min_nitrogen = crop_data_for_crop['N'].min()
    max_nitrogen = crop_data_for_crop['N'].max()

    min_phosphorus = crop_data_for_crop['P'].min()
    max_phosphorus = crop_data_for_crop['P'].max()

    min_potassium = crop_data_for_crop['K'].min()
    max_potassium = crop_data_for_crop['K'].max()

    # Print the results
    print(f"Minimum Nitrogen Value for {crop_name}: {min_nitrogen}")
    print(f"Maximum Nitrogen Value for {crop_name}: {max_nitrogen}")
    print(f"Minimum Phosphorus Value for {crop_name}: {min_phosphorus}")
    print(f"Maximum Phosphorus Value for {crop_name}: {max_phosphorus}")
    print(f"Minimum Potassium Value for {crop_name}: {min_potassium}")
    print(f"Maximum Potassium Value for {crop_name}: {max_potassium}")
