def A():
    print("Hello")

def B():
    print("How are you?")

def C():
    print("Hi")

x = str(input("What function do u wanna run?: "))

if x == 'A':
    A()
elif x == 'B':
    B()
elif x == 'C':
    C()
else:
    print("Nuh-uh!")