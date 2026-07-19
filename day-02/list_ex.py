a=[100,200,True,4.6]
print(type(a))
a.append(500)
print(a)

clouds=list()
print(type(clouds))
clouds.append("AWS")
clouds.append("GCP")
clouds.append("IBM")
print(clouds)

print("World leader for cloud service providers is", clouds[0])
print("Length of list is: ",len(clouds))


print(dir(clouds))
print(clouds.reverse.__doc__)

for i in clouds:
    if (i == "AWS"):
        print("Cloud market Dominator")
    elif( i == "GCP"):
        print("Cloud provider is Microsoft")
    else:
        print("There are many more cloud services")
