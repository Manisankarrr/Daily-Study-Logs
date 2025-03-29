# arbitrary arguments
#*args = tuple
#**kwargs = dict

# def add(*args):
#     #print(type(args)) #<class 'tuple'>
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# tot = add(1, 2, 3, 4 , 5, 6, 7, 8, 9, 10)

# print(tot)

# def name(*args):
#     for arg in args:
#         print(arg, end=" ")
#     print()

# name("John", "Doe", "Smith")

# def add(**kwargs):
#     # #print(type(kwargs)) #<class 'dict'>
#     # for key, value in kwargs.items():# .items=both, .values = right, .keys = left
#     #     print(f"{key}: {value}")
#     if "street" in kwargs:
#         print(f"{kwargs.get('street')}")
#     else:
#         print("Street not found")
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# add(street="123 Main St",
#           city="New York",
#           state="NY", 
#           zip=10001)