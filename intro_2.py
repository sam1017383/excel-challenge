
'''
my_variable = 1.0

type(my_variable)

print(my_variable)

str(my_variable)

int(my_variable)

float(my_variable)

my_list = [1,2,3,"a", "rt", [1,2,3]]

for i in range(9):
    print(i)

for each_element in my_list:
    print(each_element)

check = "yes"
while check == "yes":
    check = input("Do you want to continue?")





l = ["a", "b", "c"]

d = {0:"a", 1:"b", 2:"c"}

print(l[0])

print(d[0])


d = {100000:"a", -2:"b", 3:"c"}

print(d[100000])

# keys have to be inmmutable
# inmutable are ints, str, tupples

d = {"first_name": "Sam", "last_name": "Vazquez"}

print(d["first_name"])

d = {(1,2,3) : 0 , (2,3,4):7}
print(d[(1,2,3)])

d = {"list": [1,2,3,[1,2,3],5] }

d = {}

l = []

print(d["list"])


'''
#------------

list_a = [1,2,3,4,5,6]

list_b = ["1","2","3","4","5","6"]


length_list_a = len(list_a)
print("list_a has", length_list_a, "elements")

list_range = list(range(40,10,-3))

print("list returned by range function", list_range)


for each_index in range(len(list_a)):
    print(list_a[each_index], list_b[each_index])




