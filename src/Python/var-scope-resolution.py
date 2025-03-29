#variable scope = visible & accessible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
#LEGB = Python's scope resolution order

#Local

# def func1():
#     a = 1
#     print(a)
#     def func2():
#         a = 2
#         print(a)
#     func2() # Call func2 from func


# func1() # 1 2


#Enclosed

# def func1():
#     a = 1
#     print(a)
#     def func2():
#         print(a)
#     func2() # Call func2 from func


# func1() # 1 1

#Global


# def func1():
#     print(a)
#     def func2():
#         print(a)
#     func2() # Call func2 from func

# a = 3
# func1() # 3 3

#Built-in like PI or e