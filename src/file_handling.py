data = "My first program was related to writing hello world in python"

print(data.split())

for i in data.split():
    print(i)

for i in data:
    print(i)

'''
# I can create a file and store the data there

file = open("data.txt", 'w')

file.write("My first program was related to writing hello world in python")

file.close()
'''

# best practice would be to use with
#with open('data.txt', 'r') as file:
#    print(file.read())


#with open('data.txt', 'a') as file:
#    file.write("\n To create a virtual environment, write the following comman \n 'python3 -m venv env'")


with open('data.txt', 'r') as file:
    #print(file.readline())
    #print(file.readline())
    print(file.readlines())

# Create a file named "commands.txt", write the command to check the version in python
# read the file and print
