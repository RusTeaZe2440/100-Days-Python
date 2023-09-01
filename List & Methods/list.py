marks = [2, 45, 12, 523, 2]

print(marks[2])

# list can have different data types

marks = [2, 3, 1, "bhavya", True, 4.2]
print(marks)

# accessing list items using indexing

marks = [2, 3, 1, "bhavya", True, 4.2]

print(marks[5])
print(marks[2])

# negative indexing
# first convert into positive indexing

marks = [ 2,3,1, "bhavya" , True ,4.2 ]

print(marks[-3])
print(marks[len(marks)-3])


# check wheather the item is present or not

marks = [ 2,3,1, "bhavya" , True ,4.2 ]
 
if "bhavya" in marks:
    print("present")
else:
    print("not present")

# Range of index 

marks = [2,5,6,2,3,5]

print(marks[1:4])
print(marks[1:6:2])

# start :end :jumpbox


# list comprehension

lst = [i for i in range(4)]
print(lst)
