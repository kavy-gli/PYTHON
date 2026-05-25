print("=================================================Welcome to pattern generator and number analyzer!=================================================")
print("Please select an option:")
print("1. generate an pattern")
print("2. analyze a number ")
print("3. exit")
dec=int(input("Enter your choice: "))
print("===================================================================================================================================================")

match dec:
    case 1:
        dec2=int(input("Enter your choice:"))
        dec3=int(input("Enter the number of rows:"))
        print("===================================================================================================================================================")

        print("Here is your pattern:")
        print("*"
              "**"
              "***"
              "****"
              "*****")
    case 2:

        num=int(input("Enter the starting value :"))
        num2=int(input("Enter the ending value :"))
        print("===================================================================================================================================================")
        print("Here are the even numbers between",num,"and",num2,":")

        for i in range(num,num2+1) :
            if i%2==0:
                print(i)
        print("===================================================================================================================================================")
        print("The sum of even numbers between",num,"and",num2,"is:")        
        print(sum(i for i in range(num,num2+1) if i%2==0))

