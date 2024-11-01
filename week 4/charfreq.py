string=input("enter a string:")
for char in set(string):
    count=0
    for c in string:
        if c==char:
            count+=1
    print(char,".",count)
