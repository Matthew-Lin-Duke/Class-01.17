# caculator

def add(a, b):
    c = a + b
    print("{}+{}={}".format(a,b,c))
    return c

def sub(a,b):
    c = a - b
    print("{}-{}={}".format(a,b,c))
    return c

# basics
a = int(input("Enter the first number: "))
print("First number you entered {}".format(a))
b = int(input("Enter the second number: "))
print("Second number you entered {}".format(b))
x = input("What caculation you want: ")
print("You want to do {}".format(x))

#print("Hello, World")
#print(x)
if x == "a":
    c = add(a,b)
    #if c > 100:
     #   print("number too large")
elif x == "s":
    sub(a,b)
elif x == "m":
    a = 233
    b = 666
    c = a*b
    print("{}*{}={}".format(a,b,c))
else:
    print("The {} command is not recognized.".format(x))
    