# name = input("What's your name?")
# age = input("What's your age?")
# occupation = input("What's your occupation?")

data = input("What's your name, age and occupation?")

name, age, occupation = data.split()

print(f"Hi {name}! I see you are {age} years old and work as a {occupation}.")

s = "abcd"
print(s[5:6])
