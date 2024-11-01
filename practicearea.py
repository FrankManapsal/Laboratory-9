start=int(input("Which Number do you want to Start the Sequence with?: "))
end=int(input("Which Number do you want to end the Sequence With?: "))
if start>end:
    print("Error! (Ending Number must be Greater than Starting Number)")
for number in range(start, end+1):
    print(number)