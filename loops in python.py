# list1 = ["Harry" , "Larry"]
# for item in list1:
#     print(item )

# kushal = ["word","excel","power-point"]
# for word in kushal:
#     print(word)
# saman = [["kushal",1],["nishant",2],["sabir",3]]
# for item, roti in saman:
#     print(item,"liking number of roti is",roti)
#
# dict1 = dict(saman)
# print(dict1)
# for item, roti in dict1.items():
#     print(item,"he likes",roti)
#     for item in dict1:
#         print(item)
items = [int,float,"Harry",5,3,4,6,7,8,9,10]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
