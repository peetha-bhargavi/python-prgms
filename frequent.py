from collections import Counter
f1=open('file1.txt','w')
f1.write(input("enter some text"))
f1.close()
f2=open('file1.txt','r')
t=f2.read().split()
print(Counter(t).most_common())
