import requests

# URL of the diamonds CSV file
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv"

# Send a GET request to fetch the CSV file
response = requests.get(url)

# Specify the full local path where you want to save the file
file_path = r"C:\Projects\datafun-06\datafun-06-eda\data\diamonds.csv"

# Write the content of the response to a file
with open(file_path, 'wb') as file:
    file.write(response.content)

print(f"CSV file downloaded successfully and saved as {file_path}")

