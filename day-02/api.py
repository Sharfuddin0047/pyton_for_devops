import requests

api_url ="https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url=api_url)
print(dir(response))
print()

print(type(response.json()))

for key,value in response.json().items():
    print(key,":",value)

for key,value in response.json().items():
    if(key == "userId"):
        if(value in [1,2,3,4]):
            print("User Found")