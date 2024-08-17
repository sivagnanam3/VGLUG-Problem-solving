m1=[]
m2=[]
d1=[]
d2=[]
a=[]
r=int(input("Enter number of rows in matrix:"))
c=int(input("Enetr number of coloum in matrix:"))
def matrix(m,b):
    print("{}st Matrix".format(b))
    for i in range(r):
        print("Enter {}values of {}row:".format(c,i+1))
        m.append(input().split(","))
        if len(m[i])>=c+1:
            print("invalid input")
            break
        
def diagnol(d,m):
    for i in  range(len(m)):
        d.append(m[i][i])
def addition():
    m3=[[int(i) for i in m] for m in m1]
    m4=[[int(i) for i in m] for m in m2]
    print("1st matrix:",m3)
    print("2nd matrix:",m4)
    for i in range(len(m1)):
        a.append(m3[i][i]+m4[i][i])
        
matrix(m1,1)
matrix(m2,2)
diagnol(d1,m1)
diagnol(d2,m2)
addition()

print("diagnol of 1st matrix:",d1)
print("diagnol of 2nd matrix:",d2)
print("Addition of two diadnol:",a)
