# terms = 10
terms = int(input("How many terms? "))
# anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:", terms)

for i in range(terms):
    print("2 raised to power", i, "is", result[i])
