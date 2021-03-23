# STRING EDITING SECTION

whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

print(whitespace_string.lstrip())
print(normal_string.lstrip('is'))

whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

print(whitespace_string.rstrip())
print(normal_string.rstrip('is'))

whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

print(whitespace_string.strip())
print(normal_string.strip('is'))

print()
word = "Mississippi"
print(word.lstrip("ips"))  # "Mississippi"
print(word.rstrip("ips"))  # "M"
print(word.strip("Mips"))  # ""



# STRING CHANGING SECTION

print()
message = "bonjour and welcome to Paris!"
title_message = message.title()
print(title_message)

replaced_message = message.replace("o", "!")
print(replaced_message)
print()
print(message)




# BOOLEAN SEARCH IN STRING SECTION

print()
email = "email_address@something.com"
print(email.startswith("www."))
print(email.endswith("@something.com"))

print()
email = "my_email@something.com"
print(email.startswith("email", 2))
print(email.startswith("email", 3))

print()
email = "my_email@something.com"
print(email.endswith("@", 5, 8))
print(email.endswith("@", 5, 9))



# PRACTICE SESSION

print()
palindrome = "   live on time, emit no evil   "
print(palindrome)
palindrome = palindrome.rstrip()
print(palindrome)
palindrome = palindrome.lstrip("ilv")
print(palindrome)
palindrome = palindrome.replace("e", "E")
print(palindrome)

print()
print(palindrome.endswith(" "))
print(palindrome.startswith("E"))
print(palindrome.startswith("l", 3))
print(palindrome.endswith("Evil"))

print()

text = input()
length = len(text)
output = ''

for x in range (0, length, 1):
    if(text[x] is '.' or text[x] is ',' or text[x] is '?' or text[x] is '!'):
        continue
    else:
        output += text[x]

output = output.lower()
print(output)


# THAT MUCH CODE CAN BE RE-WRITTEN AS :
text = input()
output = text.replace(",", "").replace("?", "").replace("!", "").replace(".", "")

print(output.lower())