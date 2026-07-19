info ={
    "Name" : "Sharfuddin",
    "City" : "Ghaziabad",
    "Qualification" : "BTech",
    "Married" : False
}

print("I live in: " ,info["City"])
print("My Qualification: ",info.get("Qualification"))

info.update({"Learning" : "DevOps"})
print(info)
print(dir(info))

print(info.get.__doc__)

for i in info:
    print(i,":", info[i])

print("=========================================================")
for key,value in info.items():
    print(key, ":" ,value)