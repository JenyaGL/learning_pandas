# this notebook is for learning the requests library

# Goal: Stop analyzing files on your computer and start pulling live data from the internet.
# Requests library (import requests) is The most popular Python library in the world.

# 1. using GET requests to pull data from a website
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 200 means success

# 2. "Status Code" (The Traffic Light)
# Before you touch the data, you must check if the door opened.

# 200: OK (Green Light).
# 404: Not Found (Wrong URL).
# 500: Server Error (Their fault, not yours).
# 403: Forbidden (You need a password/key).


# 3. Safety checks (try/except)
# Always check for errors when pulling data from the internet.
# so we would have silect fails in the scripts.
try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    response.raise_for_status()  # Raises an error for bad responses
    data = response.json()  # Parse JSON data
    print(data)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # e.g. 404 Not Found
except Exception as err:
    print(f"Other error occurred: {err}")  # Other errors


print("--------------------")

# Fetching data from a test database

# first we get the API request and check the status code

test_response = requests.get("https://jsonplaceholder.typicode.com/users/1")
if test_response.status_code == 200:
    print("Success!")
else:
    print("Failed to retrieve data - ", test_response.status_code)

# then we parse the data into json format
test_data = test_response.json()

# now we can access specific fields in the json data
user_email = test_data['email']
user_adress = test_data['address']['city']

# finally we display the data using f-strings
print(f"this is emails {user_email} is from the city of {user_adress}")


print("--------------------")

# Now lets pull data from API and force it into a clean table using pandas.
import pandas as pd
import numpy as np

pandas_responce = requests.get("https://jsonplaceholder.typicode.com/users")

# making sure the API request is succesful
if pandas_responce.status_code == 200:
    print("Success!")
else:
    print("Failed to retrieve data - ", pandas_responce.status_code)

# then we parse the data into json format
pandas_data = pandas_responce.json()

# now we can normalize the jaon to a flat table
users_data = pd.json_normalize(pandas_data)

# now we can display the data as a table, but we need to chech the column names first
print(users_data.columns)

# renaming columns for better readability
users_data.rename(columns={'address.street': 'street', 'address.suite': 'suite', 'address.city': 'city', 'address.zipcode': 'zipcode', 'address.geo.lat': 'geo.lat','address.geo.lng': 'geo.lng',
                    'company.name': 'name', 'company.catchPhrase': 'catchPhrase','company.bs':'bs' }, inplace=True)

# Now we can display the table
print(users_data.head())



print("--------------------")

# Automations and reusable functions!

# The Goal: Write code that doesn't crash when the data is "dirty" (and it always is).
# lets pull data from API, push it though a cleaning and normalization funtion and store it in a dataframe

import time

# 1. the configuration
url = "https://swapi.dev/api/people/"
all_data = [] # this is the master bucket


# 2. setup
while url:
    sw_response = requests.get(url)

    if sw_response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        break # Stop the loop if it fails

    # parse the data into json format
    sw_data = sw_response.json()

    # add data from eahc page to the all_data(master bucket)
    # .extend() adds a list to a list (flattens it)
    all_data.extend(sw_data['results'])

    print(f"Fetched {len(sw_data['results'])} people. Total so far: {len(all_data)}")

    # D. UPDATE THE URL (The most important step!)
    # The API tells us what the next page is. If it's null, the loop ends.
    url = sw_data['next']

    # E. Pause for 0.5 seconds (Good manners so we don't crash their server)
    time.sleep(0.5)

print("Extraction Complete!")

# --- STEP 3: Create the DataFrame ---
# Now we make the DataFrame from the full list of 82 people
sw_data_df = pd.json_normalize(all_data)

# Verify
print(sw_data_df.info())
print(f"Total Rows: {len(sw_data_df)}")




# as you notice here, there are many columns with different types of data but hte data type of all columns is an object
# it prevents us from analyzing the numerical data and producing insights so we need to build a TRANSFORM layer
# we can and (should) create a funtion specifically for this dataset in order to maintain a continous data ingestion and 
# consumption of our systems, it goes like this:


# we need a function that handles values:

# 1. first i need to make sure that there are no null values.
# 2. then i will clean all string values from wrong spaces and capital letters
# 3. then i want to change all numerical column to numerical data types
# 4. place it all in a main funtion and run the data through it.

def normalize_numeric_values(value):

# this funtion check if a value is numnerical already, it only runs on values that are not numerical

    # 1. Safety Check: If it's already a number, return it (its a general step)
    if isinstance(value,(int,float)):
        return value
    
    # 2. clean all string values from wrong spaces and capital letters
    value = str(value).strip().lower().replace(",","")

    # 3. normalizing nul values to be the same in the data 
    if value in ['unknown','n/a','none']:
        return np.nan
    
    # 4. change all numerical column to numerical data types
    try:
        return float(value)
    except ValueError:
        # If it's text like "yoda", return NaN
        return np.nan


# Now we need a function that handles dataframes
# 1. Convert Numeric Columns (Height, Mass)
# 2. Convert "List" Columns to Int (Films)
# 3. Convert Dates (Created, Edited)

def transform_swapi_data(df):

# This function runs the cleaning of the entire DataFrame.

    # Always work on a copy!
    df_clean = df.copy()

# A. Convert Numeric Columns (Height, Mass)
# Apply our helper function to these specific columns

    numeric_columns = ['height', 'mass']
    for col in numeric_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].apply(normalize_numeric_values)

# B. Convert "List" Columns to Int (Films)
# Films is a list of URLs (e.g. ['url1', 'url2']). 
# We likely want the *Count* of films (an Integer).
    if 'films' in df_clean.columns:
        # Logic: If it's a list, count it. If it's missing, 0.
        df_clean['films_count'] = df_clean['films'].apply(lambda x: len(x) if isinstance(x, list) else 0)

# C. Convert Dates (Created, Edited)
# Pandas handles ISO formats (like '2014-12-09T13:50:51.644000Z') automatically
    date_columns = ['created', 'edited']
    for col in date_columns:
        if col in df_clean.columns:

# errors='coerce' turns bad dates into NaT (Not a Time)
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')

# Special Case: Birth Year
# 'birth_year' is weird (e.g., '19BBY'). It cannot be a standard DateTime.
# We will just clean it (strip spaces) for now.

    if 'birth_year' in df_clean.columns:
        df_clean['birth_year'] = df_clean['birth_year'].str.strip()

    return df_clean


# Now afer we have the TRANSFORM system
# Catch the result in a new variable (you can name it whatever you want)
final_df = transform_swapi_data(sw_data_df)


print(final_df.head())
print(final_df.info())

final_df.to_csv('swapi_df.csv', index=False)


