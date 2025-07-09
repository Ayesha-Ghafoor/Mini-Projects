import random
import string
pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehensiom [for i in range(n)]

password = "*".join([random.choice(charValues) for i in range(pass_len)])
# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

print("Your ramdom password is:" , password)