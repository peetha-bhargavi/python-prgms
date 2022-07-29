a='AEIOUaeiou'
b=input("enter a string")
l=len(b)
count=0
for i in b:
    if i in a:
        count=count+1
print(count)
print("the percentage is:",count/l*100)
