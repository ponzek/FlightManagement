# -*- coding: utf-8 -*-
"""passenger_analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sNcPXVh28K3Ug1B0eejqptOb-uViKtdZ

#Task 1: Data loading and cleaning.

##a.) Load Data Function
"""

import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

"""##b.) Clean Data Function"""

def clean_data(df):
    if df is None:
        return None

    # Handling missing values
    for column in df.columns:
        if df[column].dtype == 'object':  # Categorical data
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:  # Numerical data
            df[column].fillna(df[column].mean(), inplace=True)

    # Ensure appropriate data types
    for column in df.columns:
        if 'date' in column.lower():
            df[column] = pd.to_datetime(df[column], errors='coerce')
        elif df[column].dtype == 'object':
            try:
                df[column] = df[column].astype(float)
            except ValueError:
                pass

    return df

def clean_data(df):
    # Filter and handlings missing data (na)
    df.fillna(df.mean(), inplace=True)  # There are different ways of handling missing data. here we replace with the mean.

    # This ensures and determines other types of object types and convert to allow any missing or no value (NaN)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category')
        elif df[col].dtype == 'int64':
            df[col] = df[col].astype('float64')

    return df

"""#Task 2: Decision Making and Loops

##a.) Function that calculates the average age of passengers in a given travel class.
"""

def calculate_average_age(df, travel_class):
    # Filter the DataFrame based on the travel class
    df_class = df[df['TravelClass'] == travel_class]

    # Calculate the average age
    avg_age = df_class['Age'].mean()

    return avg_age

"""###Take DF and TravelClass as input to return list of names of passengers who are on LoyaltyMembers.

##b.) Functions that finds loyalty program members.
"""

def find_loyalty_members(df):
    # Filter the DataFrame based on loyalty program membership
    df_loyalty = df[df['LoyaltyMember'] == True]

    # Extract the names of the loyalty program members
    names = df_loyalty['Name'].tolist()

    return names

"""###Returns a list of names of employees with experience greater than or equal to the specified years."""

def find_experienced_employees(df, years):
    # Filter the DataFrame based on experience
    df_experience = df[df['Experience'] >= years]

    # Extract the names of the experienced employees
    names = df_experience['Name'].tolist()

    return names

"""#Task 3: Fuctions and Modules

###a.) Function that calculates the average age and number of loyalty members for each travel class
"""

def get_class_statistics(df):

    # Initialize an empty dictionary to store the results
    class_stats = {}

    # Iterate over each travel class
    for travel_class in df['TravelClass'].unique():
        # Filter the DataFrame based on the travel class
        df_class = df[df['TravelClass'] == travel_class]

        # Calculate the average age
        avg_age = df_class['Age'].mean()

        # Count the number of loyalty members
        loyalty_members = df_class['LoyaltyMember'].sum()

        # Add the results to the dictionary
        class_stats[travel_class] = {'Average Age': avg_age, 'Loyalty Members': loyalty_members}

    return class_stats

"""###b) Write a module named passenger_analysis.py and move all the above functions to this module.
  Done.

###c) Import this module into your main script and call the functions as needed.
  Done.
"""