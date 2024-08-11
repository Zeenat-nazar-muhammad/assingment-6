
# sum of all element in list

def element(list):
    return sum(list)
list=[22,44,66,89,67,54,32]
sum=element(list)
print(sum)

#smallest element in tuple
t=(22,35,45,54,67,72,83,91)
print(t)
print("lenght of tuple ",len(t))
print("smallest element from tuple ",min(t))

# print all the keys in dictionary
dict={"name":"aleena",
    "course":"cit python",
    "program":"banoqabil 3.0"}
print(dict)
print(dict.keys())
print(dict.values())
for key in dict.keys():
    print(dict[key])
    
#squared of element
def square(x):
    return x ** 2
number=int(input("enter number :"))
print("square of" ,number , "is :",square(number) )


