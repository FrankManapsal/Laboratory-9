number = int(input("Enter a Number: "))
i = 1
print(f"Multiplication Table for {number}:")

while i < 11:
    multiple = number * i
    print(f"{number} x {i} = {multiple}")
    i += 1