import requests

pj_joke_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(api_url, headers=None):
    response = requests.get(url=api_url, headers=headers)
    try:
        data = response.json()
        # For programming jokes (setup + punchline)
        if "setup" in data and "punchline" in data:
            print(data["setup"])
            print(data["punchline"])
        # For dad jokes (single "joke" field)
        elif "joke" in data:
            print(data["joke"])
        else:
            print("Unexpected response:", data)
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")
        print("Raw response:", response.text)

joke_type = input("Enter the type of joke you want [dad, pj]: ")

if joke_type == "dad":
    api_url = dad_joke_url
    headers = {"Accept": "application/json"}
    get_joke(api_url, headers=headers)
else:
    api_url = pj_joke_url
    get_joke(api_url)
