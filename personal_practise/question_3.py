# swpping 2 numbers using python

def swap(a,b):
    
    print("before swapping:")
    print("a = " ,a)
    print("b = " ,b)
    
    a,b = b,a
    
    print("after swapping:")
    print("a = " ,a)
    print("b = " ,b)    


a = int(input("enter a number: "))
b = int(input("enter another number: "))    
swap(a,b)