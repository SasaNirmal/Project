#get_input().py

def input_data():
    try:
        num1=int(input("Enter frist Number:"))
        num2=int(input("Enter second Number:"))
        num3=int(input("Enter third Number:"))
        return num1,num2,num3

    except:

        print("Invaled Number")

input_data()
