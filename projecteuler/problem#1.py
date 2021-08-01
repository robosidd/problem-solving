multiples = 0

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        multiples += num

print(multiples)


# This is shorter method
# print(sum([num for num in range(1,1000) if num% 3 == 0 or num%5 == 0]))
