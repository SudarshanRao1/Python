class Hi:
    a = 4

o = Hi()
print(o.a) #printing the class Atributes because the instance attributes are not set

o.a = 0    #printing the instance Atributes because the instance attributes is set
print(o.a)

print(Hi.a) #prints the class Atributes