
l1=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list:"))
    l1.append(e)

print("Positive numbers in",l1,"are: ")

for i in l1:   
    if i >= 0:
       print(i, end = " ")
