# Exercise 1
# Cube Number Test... Print out all cubed numbers up to the total value 1000.
# Meaning that if the cubed number is over 1000 break the loop.

i = 1
while i ** 3 <= 1000:
    print(i**3)
    i += 1

# Exercise 2
# Get first prime numbers up to 100

for int in range(2,101):
    for num in range(2,int):
        if int % num == 0:
            break
    else:
        print(int)

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids,
# If they're 18 to 65 print adults, else print seniors

user_age = int(input("How old are you? "))

if user_age < 18:
    print("You are a child.")
elif user_age <= 65:
    print("Congrats, you're an adult. Enjoy the responsibility.")
else:
    print("You're quite old.")