"""
def String(str):
    if (len(str) >= 2 and str[:2] == "Is"):
        return str
    else:
        return "Is"+str

print(String("Isvijay"))
print(String("vijay"))
"""
def String(A,n):
    X = ""
    for o in range(1,n+1):
        X = X + A
    return X
    
print(String("abc",2))
print(String("vijay",5))