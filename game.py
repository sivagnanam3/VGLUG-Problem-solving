#PYTHON PROGRAM FOR GAME 
a=0
while a<100:
    print(a)
#PLEASE ENTER THE POSITION OF THE PLAYER
    p1=input("first person enter 1-10 no:")
    while not p1.isdigit():
        p1=input("first person your number is invalid plese enter vaild number(1-10):")
    p1=int(p1)
    while p1>10 or p1==0:
        p1=input("first person your number is invalid plese enter vaild number(1-10):")
        while not p1.isdigit():
            p1=input("first person your number is invalid plese enter vaild number(1-10):")
        p1=int(p1)
    if p1<=10:
        b=a+p1
    if b>=100:
        print(b)
        print("Game Over")
        print("first person is win")
        break
    print(b)
    p2=input("secon person enter 1-10 no:")
    while not p2.isdigit(): 
        p2=input("secon person your number is invalid plese enter number(1-10):")
    p2=int(p2)
    while  p2>10 or p2==0:
        p2=(input("secon person your number is invalid plese enter number(1-10):"))
        while not p2.isdigit():
            p2=(input("secon person your number is invalid plese enter number(1-10):"))
        p2=int(p2)
    if p2<=10:
        c=b+p2
    if c>=100:
        print(c)
        print("Game Over")
        print("secon person is win:")
        break
    a=c
