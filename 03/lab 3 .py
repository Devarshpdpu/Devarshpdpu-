Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
... s=input("enter a name:")
... count=0
... for i in s:
...     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
...         count+=1
... print(count)
... 
... #2
... def change():
...     s=input("enter to change:")
...     p=input("ënter name:")
...     if s=="upper":
...         p=p.upper()
...         print(p)
...     elif s=="lower":
...         p=p.lower()
...         print(p)
...     elif s=="toggle":
...         p=p.swapcase()
...         print(p)
... change()
... 
... #3
... x=input()
... y=input()
... count=0
... for i in x:
...     for j in range(len(y)):
...         if y[j]==i:
...             count+=1
... if count==len(y):
...     print("Yes")
... else:
...     print("No")
... 
... #3
... 
... x=input()
... y=input()
... for i in range(len(x)):
...     if y==x[i:len(y)+i]:
...         print("yes")
... 
... #4
... x=input()
... y=input()
... for i in range(len(x)):
...     if y==x[i:len(y)+i]:
