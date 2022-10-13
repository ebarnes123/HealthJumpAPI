import requests
from requests.auth import HTTPBasicAuth
import json


# Post method to authenticate API.
auth_url = "https://api.healthjump.com/authenticate"
username = "sandbox@healthjump.com"
password = "R-%Sx?qP%+RN69CS"

# authenticate with header and body
headers = {"Content-Type": "application/json; charset=utf-8"}

# Data is the login credentials
data = {
    "email": "sandbox@healthjump.com",
    "password": "R-%Sx?qP%+RN69CS"
}

# Posts to the authenticate page.
post_response = requests.post(auth_url, headers=headers, json=data)

# Returns codes to show us whether it fails or succeeds
print("Status Code: ", post_response.status_code)
print("JSON Response: ", post_response.json())

token = post_response

# Get method for Demographics
demographics_url = "https://api.healthjump.com/hjdw/SBOX02/demographic"

# Add the Authorization header
headers = {
    'Secretkey': 'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g',
    'Authorization': 'Bearer {{post_response.json()}}',
    'Version': '3.0'
}

params = {'client_patient_id': 'eqf~322571'}

get_response = requests.get(
    demographics_url,
    params=params,
    headers=headers
)

print("Status Code", get_response.status_code)
print("JSON Response ", get_response.json())

def print_hi(name):
    print(f'Hi, {name}') 


if __name__ == '__main__':
    print_hi('PyCharm')
