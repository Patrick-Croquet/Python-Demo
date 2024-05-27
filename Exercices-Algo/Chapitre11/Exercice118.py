a = 10
b = 5

def Inversion(X, Y):
    #Temp = X
    #X = Y
    #Y = Temp
    X, Y = Y, X
    return(X, Y)

a, b = Inversion(a, b)

print(f"valeur de a : {a} \nvaleur de b : {b}")