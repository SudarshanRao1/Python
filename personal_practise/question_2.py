n1 = float(input("enter the number you want: "))
n2 = float(input("enter another nubmber: "))
symbol = input("enter the operator you wanna perform babyuyyyyyyyyyyyyyyyyyyyyyyy: ")


match symbol: 
    case "+":
        a  = n1 + n2
        print("the sum is: " ,a)
    case "-":
        a = n1 - n2
        print("the subtraction is: ", a)
    case "*":
        a = n1*n2
        print("the multipalication is: ",a)
    case "/":
        if n2!=0:
            a = n1/n2
            print("the devision is: ",a)
        else:
            raise ValueError("devision by the zero will not work!!!!!!!!!!!")              
    case _:
        raise ValueError("Invalid value symbol or input")
