Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
'''#1.
a=int(input("enter your number"))
b=int(input("enter your number"))
print(a+b)
#2.
a=int(input("enter your number"))
b=int(input("enter your number"))
print(a-b)
#3.
a=int(input("enter your number"))
... b=int(input("enter your number"))
... print(a*b)
... #4.
... a=int(input("enter your number"))
... b=int(input("enter your number"))
... print(a/b)
... #5.
... b=int(input("enter your number"))
... print("Your answers are")
... print(a+b,a*b,a-b,a/b,sep=',')
... #6.
... b=float(input("enter hours"))
... print("No of minutes are ",60*b)
... #7.
... b=float(input("enter minutes"))
... print("No of hours are ",b/60)
... #8.
... b=float(input("enter dollars"))
... print("No of ruppees are ",b*48)
... #9.
... b=float(input("enter ruppees"))
... print("No of dollars are ",b/48)
... #10.
... b=float(input("enter dollars"))
... print("No of pounds are ",(b*48)/70)
... #11.
... b=float(input("enter grams"))
... print("No of kilos are ",b/1000)
... #12.
... b=float(input("enter kilos"))
... print("No of grams are ",b*1000)
... #13.
... #14.
... b=float(input("enter celcius temp"))
... print("temp in farenheit will be  ",(9*b)/5 + 32)
... #15.
... b=float(input("enter farenheit"))
... print("temp in celcius is ",(5/9)*(b-32))
... #16.
... b=float(input("enter principal "))
... c=float(input("enter rate "))
... d=float(input("enter time "))
... print("interest is ",(b*c*d)/100)
... #18.
... b=float(input("enter side"))
... print("area is",b**2)
... #19.
... a=float(input("enter length "))
... b=float(input("enter width "))
... print("area is",a*b,"perimeter is",2(a+b))
... #20.
... a=float(input("enter length "))
... b=float(input("enter height "))
... print("area is",(a*b)/2)
... #21.
... b=float(input("enter gross salary"))
... print("net salary is",1.13*b)
... #22.
... b=float(input("enter gross sales"))
... print("net sales is",0.9*b)
... #23.
... a=float(input("enter a"))
... b=float(input("enter b"))
... c=float(input("enter c"))
... print("sum is",a+b+c,"average is",(a+b+c)/3)
... #24.
... a=float(input("enter a "))
... b=float(input("enter b "))
... a,b=b,a
