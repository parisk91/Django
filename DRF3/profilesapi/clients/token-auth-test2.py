import requests

def clients():
    data = {
        "username":"resttest",
        "email":"/rest@example.com",
        "password1":"chageme123",
        "password2":"changeme123"
    }

    response = requests.post("kjsdnvcksdnv", data=data)
    print("Status code:", response.status_code)

if __name__ == "__main__":
    client()