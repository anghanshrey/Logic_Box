while True:
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choices = int(input("Enter your Choice:"))

    match choices:
        case 1:
            Rows = int(input("Enter the number of rows for the pattern: "))
            if Rows < 0 :
                print("Enter vaild Number")
            else:
                print("Pattern:")
                for i in range(0,Rows+1):
                    for j in range(0,i):
                        print("*",end="")
                    print("")
        case 2:
            start = int(input("Enter the start of the range:"))
            end = int(input("Enter the end of the range:"))

            sum = 0
            
            for i in range(start,end+1):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is odd")
                sum += i
            print(f"Sum of all numbers from {start} to {end} is: {sum}")
        case 3:
            print("Exiting the program. Goodbye!")
            break
        
