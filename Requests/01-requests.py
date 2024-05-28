import requests

def main():
    response = requests.get("https://api.nationalize.io?name=george")
    if response.status_code != 200:
        print("Status code", response.status_code)
        raise Exception("Error")
    
    data = response.json()
    print("Data in JSON", data)

if __name__ == "__main__":
    main()