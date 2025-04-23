Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
... a=int(input("enter the number"))
... b=int(input("enter the number"))
... 
... if a>b:
...     print("a is largest",a)
... elif a==b:
...     print(a,"=",b)
... else:
...     print("b is largest",b)
... 
... #2
... a=int(input("enter the number"))
... b=int(input("enter the number"))
... c=int(input("enter the number"))
... 
... if a>b and a>c:
...     print("a is largest",a)
... elif b>a and b>c:
...     print("b is largest",b)
... elif a==b and b==c and a==c:
...     print(a,"=",b,"=",c)
... else:
...     print("c is largest",c)
... 
... #3
... a=int(input("enter the number"))
... 
... if a%2==0:
...     print(a,"the number is even")
... else:
...     print(a,"the number is odd")
... 
... #4
... a=int(input("enter the number"))
... 
... if a%10==0:
...     print(a,"the number is divisible by 10")
... else:
...     print(a,"the number is not divisible by 10")
... 
... #5
... a=int(input("enter the number"))
... if a<18:
...     print(a,"person  minor")
... else:
...     print(a,"person  major")
... 
... #6
... a=input("enter the number")
... b=len(a)
... print("no. of digits is",len(a))
... 
... #7
... a=int(input("enter the number"))
... 
... if a%400=!0 or a%4==0 and a%100==0:
...     print("this",a," is  leap year")
... else:
...     print("this",a," is not leap year")
... 
... #8
... a=int(input("enter the number"))
... b=int(input("enter the number"))
... c=int(input("enter the number"))
... 
... if a+b+c==180:
...     print("exist triangl")
else:
    print("not exist triangle")

#9
a=int(input("enter the number"))

if a<0:
    print(abs(a))
else:
    print(a)

#10
a=int(input("enter the number"))
b=int(input("enter the number"))
area=a*b
perimter=a+b

if area>perimter:
    print(area,">=",perimter)
elif area==perimter:
    print(area,"=",perimter)
else:
      print(area,"<=",perimter)

#11
def num(x1,y1,x2,y2,x3,y3):
    
    area=0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

    return area==0
x1,y1=int(input("enter the number")) , int(input("enter the number"))
x2,y2=int(input("enter the number")) , int(input("enter the number"))
x3,y3=int(input("enter the number")) , int(input("enter the number"))

if  num(x1,y1,x2,y2,x3,y3):
    print("the point are coolinear")
else:
    print("the point are not coolinear")

#12
def poi_pos(r,center,point):
    dist = ((center[0]**2 - point[0]**2) - (center[1]**2 - point[1]**2))**0.5
    if dist > r:
        print("Point lies outside the circle.")
    elif dist == r:
        print("Point lies on the circle.")
    else:
        print("Point lies inside the circle")    

r = int(input("Enter radius: "))
cx = int(input("Enter center x: "))
cy = int(input("Enter center y: "))
px = int(input("Enter point x: "))
py = int(input("Enter point y: "))

poi_pos(r,(cx,cy),(px,py))
#13
words = ["zero","one","two","three","four","five",'six', "seven","eight", "nine", "ten", "eleven","twelve", "thirteen"]
for i in range(0,20):
    if i < 14:
        print(words[i])
    else: 
        print(f"{words[i-10]}teen")
#14
def pass_or_fail(s1,s2,s3):
    if s1<=39 or s2 <= 39 or s3 <= 39:
        return "Fail"
    return "Pass"
def assign_grade(grade):
    if grade <= 100 and grade>=80:
        return 'O'
    elif grade>= 79:
        return 'A+'
    elif grade >= 69: 
        return 'A'
    elif grade >= 59 and grade >= 55:
        return 'B+'
    elif grade >= 54 and grade >= 50:
        return 'B'
    elif grade >= 49 and grade >= 45:
        return 'C' 
    elif grade >= 44 and grade >= 40:
        return 'P'
    elif grade >= 39 and grade >= 0:
        return 'F'  

s1 = int(input("Enter subject 1 marks: "))
s2 = int(input("Enter subject 2 marks: "))
s3 = int(input("Enter subject 3 marks: "))

total = s1+s2+s3
avg = total/3
s1G = assign_grade(s1)
s2G = assign_grade(s2)
s3G = assign_grade(s2)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Result: {pass_or_fail(s1,s2,s3)}")
print(f"Subject 1 : Grade: {s1G}")
print(f"Subject 2 : Grade: {s2G}")
