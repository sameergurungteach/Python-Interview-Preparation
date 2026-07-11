import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()
    print(data)
    print("Name:", data["name"])

except requests.exceptions.ConnectionError:
    print("No internet connection.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.HTTPError:
    print("Server returned an error.")

except Exception as e:
    print("Unexpected Error:", e)