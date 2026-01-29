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







