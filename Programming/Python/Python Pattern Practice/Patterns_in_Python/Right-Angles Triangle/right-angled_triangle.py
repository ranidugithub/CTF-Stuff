n = int(input("Please neter a number: "))

for r in range(n):
    for c in range(r+1):
        print("*", end= " ")
    print()