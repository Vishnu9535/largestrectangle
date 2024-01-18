import requests

url = "http://127.0.0.1:8000/largest_rectangle"

matrix_example = {
    "matrix": [
        [1, 1, 1, 0, 1, -9],
        [1, 1, 1, 1, 2, -9],
        [1, 1, 1, 1, 2, -9],
        [1, 0, 0, 0, 5, -9],
        [5, 0, 0, 0, 5]
    ]
}

# Send a POST request
response = requests.post(url, json=matrix_example)

# Check if the response contains valid JSON
if response.headers["content-type"] == "application/json":
    try:
        json_response = response.json()
        print("Response JSON:", json_response)
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Non-JSON response:", response.text)
