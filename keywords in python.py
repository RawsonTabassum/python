import keyword

print ("The list of keywords is : ")
print (keyword.kwlist)

print(" ")

# initializing strings for testing while putting them in an array
keys = ["while", "tanisha", "break", "sky",
        "elif", "assert", "pulkit", "lambda"]

for i in range(len(keys)):
    # checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")

