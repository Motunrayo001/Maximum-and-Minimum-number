#initialize largest and smallest to none
largest = None
smallest = None
#prompt the user to enter the numbers
while True:
    num = input("Enter a number: ")
    #check if the user is done
    if num == "done":
        break
        #Try converting the input to float
    try:
        number = int(num)
        if largest is None:
            largest = number
        elif  largest < number:
            largest = number
        if smallest is None:
            smallest = number
        elif smallest > number:
            smallest = number
    except ValueError:
        print("Invalid input")
        continue
    #print(num)
if largest is not None and smallest is not None:
    print("Maximum is",largest)
    print("Minimum is",smallest)