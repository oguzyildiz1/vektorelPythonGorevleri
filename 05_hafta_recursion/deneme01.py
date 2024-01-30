x = 100

def test(x):
    x -= 10
    print("inside", x)

    if x < 90:
        return x #base
    
    return test(x) #recursion




y = test(x)
print("outside", y)