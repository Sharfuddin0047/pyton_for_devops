file = open("demo.txt","w+")
file.write("Who are you")

# Move pointer back to the beginning
file.seek(0)

print(file.read())
file.close()
