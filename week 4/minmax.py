list1=input("enter the list")
list2=list(map(int,list1.split()))
sort1=sorted(list2)
print("sorted list",sort1)
max1=max(list2)
print("maximum value",max1)
min1=min(list2)
print("minimum value",min1)
sort1.reverse()
print("reverse",sort1)
count=len(list2)
print("length of list",count)
sum=sum(list2)
print("sum of list",sum)
