# Code to print all values from 1 to 100
# Skip the numbers which are divisible  by 3 or 5

for i in range(1, 100):
    if i % 3 != 0 or i % 5 != 0:
        print(i)
    else:
        pass

# While loop

i = 1
while (i < 101):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
    i = i + 1

# Print pattern

####
####
####
####

i = 1
while i <= 5:
    print(5 * '#')
    i = i + 1
    print()
