dictionary = {20:"january"}
print(dictionary)

dictionary = {1:"kiran", 2:"arun"}
print(dictionary)

dictionary = {1:"kiran", 2:"arun", 2:"mahesh", 2:"pavan"}
print(dictionary)

print(dictionary[1])
print(dictionary[2])

print(dictionary.get(1))

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

dictionary[1]="jeethu"
print(dictionary)

dictionary.update({3:"venki"})
print(dictionary)

dictionary[4]="Naveen"
print(dictionary)

dictionary.pop(1)
print(dictionary)

dictionary.pop(1,2)
print(dictionary)

dictionary.popitem()
print(dictionary)

del dictionary[2]
print(dictionary)

dictionary.clear()
print(dictionary)

for element in dictionary:
    print(element)

for element in dictionary:
    print(dictionary[element])

for element in dictionary.values():
    print(element)

for element in dictionary.items():
    print(element)

for key,values in dictionary.items():
    print(key,values)

print("--------------------------------------------------------------------------")

test = {"xxx":{5:"madhu", 6:"Ashu", 7:"Praveen"},"yyy":{8:"aaa",9:"bbb",10:"ccc"}}
print(test)

test = {"xxx":{5:"madhu", 6:"Ashu", 7:"Praveen"},"yyy":{8:"aaa",9:"bbb",10:"ccc"},"yyy":{8:"aaa",9:"bbb",10:"ccc"}}
print(test)

test = {"xxx":{5:"madhu", 6:"Ashu", 6:"Chethan"},"yyy":{8:"aaa",9:"bbb",10:"ccc"},"yyy":{8:"aaa",9:"bbb",10:"ccc"}}
print(test)

print(test["xxx"])

print(test.get("yyy"))

print(test.keys())
print(test.values())
print(test.items())

test["xxx"]={11:"apple",12:"orange"}
print(test)

test.update({"zzz":{30:"fff",40:"lll"}})
print(test)

test["ttt"]={50:"audi"}
print(test)

test.pop("zzz")
print(test)

# test.popitem()
# print(test)

del test["yyy"]
print(test)

test.clear()
print(test)
