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

response = requests.post(url, json=matrix_example)

if response.headers["content-type"] == "application/json":
    try:
        json_response = response.json()
        print("response in JSON", json_response)
    except requests.exceptions.JSONDecodeError as e:
        print("error in JSON:", e)
else:
    print("not a JSON response:", response.text)


