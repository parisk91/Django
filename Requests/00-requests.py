import requests

def main():
    response = requests.get("https://www.google.com/random-1234")
    print("Status code:", response.status_code)
    """ print("Response headers:", response.headers)
    print("Content type", response.headers['Content-Type']) """
    print("Response", response.text)

if __name__ == "__main__":
    main()