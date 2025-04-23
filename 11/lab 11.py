Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
... while True:
...     try:
...         num = int(input("Enter an integer: "))
...         print("You entered:", num)
...         break  
...     except ValueError:
