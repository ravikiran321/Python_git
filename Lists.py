"""this is a list constructor -> means if u want convert tuple or some arguments in to list
then we will use this list constructor"""
thisList = list(("apple", "banana","cherry"))
print(thisList[:2])  # it will display from 0 to 1 index , bcz mentioned range is [:2]
print(thisList[1:2])  # it will display only second index, bcz specified range is 1:2
print(thisList[-2])   # it will display last 2 indexes in the list , bcz we  specified range is [-2]
print(thisList[0:])   # it will display from starting to end even last range is not specified.

mylist = ["kiran", 10 ,"Arun", 100]
print(mylist)  # it will give you the values in the list even it is int, float, string etc.

name = "Ravikiran"
print(list(name))  # it will provide the result as single char in a string ravikiran bcz it considers as tuple.

thisList.append("orange")  # append is used to add the value at the end of the list , only 1 value can add.
print(thisList)

thisList.insert(1,"grapes")  # insert is used to insert the value in a specified index position like 1
print(thisList)

thisList[2] = "butter fruit"  # it will replace the butter fruit in place of 2nd index (banana)
print(thisList)

thisList[0:2] = ["banana","jack"]  # it will replace one or more than one values in the list bcz we range
print(thisList)

thisList.extend(mylist)  # extend is used to add the other list , here we are changing with the list not using 3rd list
print(thisList)

thisList = thisList[:-4]  # it will omit the last 4 values in the list bcz we specified the range as [:-4]
print(thisList)

newlist = thisList + mylist  # we are concatenating the 2 list and displaying that result in 3rd list.
print(newlist)

newlist.pop()  # this is used to delete the last value in the list
print(newlist)

newlist.pop(0)  # it will delete the value based on the provided index
print(newlist)

newlist.remove("jack")  # to remove the value by specifying that value
print(newlist)

del newlist[0:2]  # del is a keyword to delete the specified range
print(newlist)

del newlist[:]  # to delete all the values but structure remains same.
print(newlist)

del newlist  # to delete complete list including list structure
print(newlist)
