n=int(input("Enter number of elements in list:"))
nums=[]
dup=[]
flag=0
for i in range(n):
    x=int(input("Enter element:"))
    nums.append(x)
for i in nums:
    if i in dup:
        print("True")
        flag=1
        break
    else:
        dup.append(i)
if flag==0:
    print("False")