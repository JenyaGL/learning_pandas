import pandas as pd
import seaborn as sns

# welcome to my interactive notebook

# what is a dataframe?

# honestly, a dataframe is just pandas lengu for a data table.
# it calls columns Series and unique IDs Indexes - important to know.

#-----------
# from EXCEL POV:
# In Excel, you are used to seeing a grid. A DataFrame is also a grid.
# When you type df.head(N)/df.tail(N), it shows you the first/last N rows in a grid.
# with calculations,Just like you would write =A2 * B2 and drag it down, 
# in a DataFrame you write df['Total'] = df['Price'] * df['Quantity'].
# It applies the math to the whole column instantly
# Like Excel, Pandas has a literal
# .pivot_table() function that works exactly like the drag-and-drop version in Excel.

#-----------
# from SQL POV:
# While Excel is visual, Pandas is declarative like SQL.
# Filtering: Instead of SELECT * FROM table WHERE age > 25, you write df[df['age'] > 25].
# Joining: Instead of INNER JOIN, you use pd.merge(df1, df2, on='id').
# It supports Left, Right, Outer, and Inner joins
# Grouping: Instead of GROUP BY department, you write df.groupby('department').sum()

#-----------
# biggest Difference: The Index
# In SQL, your "row ID" is just another column (the Primary Key).
# In Excel, your row ID is the number on the far left.
# In a DataFrame, the Index is a special "address" for the row.
# It can be a number, a date, or even a string (like a SKU).
# This makes looking up specific rows incredibly fast
# much faster than a VLOOKUP or a WHERE clause on a non-indexed column.    


# Summary:
# As an analyst, your new workflow will likely look like this:
# Extract: Run a SQL query to pull data from a database into a DataFrame (pd.read_sql).
# Clean: Use Pandas to handle nulls (.fillna) or fix typos that are too annoying to do in SQL.
# Analyze: Run your complex logic or stats in Python.
# Output: Export the final result back to Excel (.to_excel) for your stakeholders.

# ---------------------------------------

# How to load data - (i will use a seaborn dataset for examples)

# df = pd.read_csv('file.csv')  # CSV file
# df = pd.read_excel('file.xlsx')  # Excel file
# df = pd.read_json('file.json')  # JSON file


# how to do pull data from a database:

# from google.cloud import bigquery
# Client = bigquery.Client()  # BigQuery
# sql = "SELECT * FROM dataset.table LIMIT 100"
# df = client.query(sql).to_dataframe()

data = sns.load_dataset('iris')
df = pd.DataFrame(data)


# ----------------------------------------

# How to explore data - basic commands

print('head:')
print(df.head(5)) # this command shows the first 5 rows of the dataframe
print('tail:')
print(df.tail(5)) # this command shows the last 5 rows of the dataframe
print('info:')
print(df.info()) # this command shows a summary of the dataframe
print('shape:')
print(df.shape) # this command shows the number of rows and columns in the dataframe
print('Dtypes:')
print(df.dtypes) # this command shows the data types of each column
print('describe:')
print(df.describe()) # this command shows basic statistics of numerical columns

print("-----------------------------------")

# How to sort Values

print('sorted_df:')
sorted_df = df.sort_values(by='sepal_length', ascending=False) # sorts the data by sepal_length, descending
# PS : you can sort by multiple columns by passing a list to 'by' parameter

print(sorted_df.head(5))

print("-----------------------------------")

# How to group data
grouped_df_mean = df.groupby('species').mean() # groups the data by species and calculates the mean of each group
grouped_df_median = df.groupby('species').median() # groups the data by species and calculates the median of each group
grouped_df_sum = df.groupby('species').sum() # groups the data by species and calculates the sum of each group
grouped_df_count = df.groupby('species').count() # groups the data by species and calculates the sum of each group

print('grouped mean')
print(grouped_df_mean)
print("-------------")
print('grouped median')
print(grouped_df_median)
print("-------------")
print('grouped sum')
print(grouped_df_sum)
print("-------------")
print('grouped count')
print(grouped_df_count)

print("-----------------------------------")

# How to filter data

fitered_df = df[(df['petal_length'] > 1.3)] # filters the data where petal_length is greater than 1.3
print(fitered_df.head(5))

# there is a better, more sql style way of filtering data using the query method
fitered_df_query = df.query('petal_length > 1.3') # filters the data where petal_length is greater than 1.3
print(fitered_df_query.head(5))

# i prefer it becasue im more comfterable with sql syntax

print("-----------------------------------")

# How To Manipulate Data

# groups the data by petal_width and counts the number of occurrences of each petal_width
grouped_data = df.groupby('petal_width').agg({'petal_width': 'count'})
print(grouped_data)

print("-----------------------------------")

# Now lets do some Practice Exercises

# i will include a dataset in the github repo, its called weather_data.csv 

# what you need to find:
# 1. find differences between average max temprateure per day and record max temprature
# 2. sort hottest months of the year by max AVG temprature

# Load the dataset

# read the data
data = pd.read_csv('weather_data.csv')
print('head:')
print(data.head(5)) # this command shows the first 5 rows of the dataframe
print('tail:')
print(data.tail(5)) # this command shows the last 5 rows of the dataframe
print('info:')
print(data.info()) # this command shows a summary of the dataframe
print('shape:')
print(data.shape) # this command shows the number of rows and columns in the dataframe
print('Dtypes:')
print(data.dtypes) # this command shows the data types of each column
print('describe:')
print(data.describe()) # this command shows basic statistics of numerical columns

# ----------------
# 1) find differences between average max temprateure per day and record max temprature

# create a new column and substract record from average
# print out sorted df ascending = False

data['temp_diff'] = data['record_max_temp'] - data['average_max_temp']
print(data.sort_values(by='temp_diff', ascending=False).head(5))


# -----------------
# 2) sort hottest months of the year by max AVG temprature

# extract month from date column
# group data by month and calculate mean of average_max_temp
# sort the result by average_max_temp descending
# Force the column to be a datetime object
data['date'] = pd.to_datetime(data['date'], format = 'ISO8601')
group_by_month = data.groupby(data.date.dt.month)['average_max_temp'].max()
sort_by_month =group_by_month.sort_values(ascending=False)
print(sort_by_month)