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

# lets pull first
sw_data_response = requests.get("https://swapi.dev/api/people/")
if sw_data_response.status_code == 200:
    print("Success!")
else:
    print("Failed to retrieve data - ", sw_data_response.status_code)

# parse the data into json format
sw_data = sw_data_response.json()

# now we can define a function to clean and normalize the data

sw_data_df = pd.json_normalize(sw_data['results'])

print(sw_data_df.info())

print(sw_data_df.head())

# as you notice here, there are many columns with different types of data but hte data type of all columns is an object
# it prevents us from analyzing the numerical data and producing insights so we need to build a TRANSFORM layer
# we can and (should) create a funtion specifically for this dataset in order to maintain a continous data ingestion and 
# consumption of our systems, it goes like this:


# 1. first i need to make sure that there are no null values.
# 2. then i will clean all string values from wronf spaces and capital letters
# 2. then i want to change al numerical column to numerical data types
# 3. place it all in a main funtion and run the data through it.

def normalize_numeric_values(value):


    # 1. Safety Check: If it's already a number, return it (its a general step)
    if isinstance(value,(int,float)):
        return value
    
    # 2. normalizing nul values to be the same in the data 
    if value in ['unknown','n/a','none']:
        return np.nan
    
    # 3. 
    value =

