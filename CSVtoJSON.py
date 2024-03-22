""" 
    This code is used to convert a CSV into a JSON file that coule later be saved in a mongoDB
    
    IN:
        - Path to the CSV file you want to convert
        - Path to create a new JSON file

    OUT:
        - New JSON file containing the data of the CSV
        
    NB:
        - Be careful when inputting the path where the data will get saved, you need to input the name of the JSON that will get created as part of the path 
    
[Malek Miled]
"""
import os
import csv
import json

def csv_to_json(variables, path):
    # Create a dictionary to store observations for each longitude value
    data = {}

    # Iterate over each variable and read corresponding CSV files
    for variable in variables:
        # Create path
        csv_file_path = os.path.join(path, f"{variable}.csv")
        
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                # Iterate over each longitude value and store observations
                for longitude, value in row.items():
                    if longitude not in data:
                        data[longitude] = {}
                    if variable not in data[longitude]:
                        data[longitude][variable] = []
                    data[longitude][variable].append(value)

    # Write the data into a single JSON file
    json_file_path = os.path.join(path, "data.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    #print("Conversion completed. JSON file saved at:", json_file_path)
