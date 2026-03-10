# set = colllection which is unordered, unindexed. No duplicate values.
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup", "knife"}

#utensils.add("napkin") #--> add something into set
#utensils.remove("fork") #--> remove something from set
#utensils.clear() #--> clear everything from set
#utensils.update(dishes) #--> put dishes into to utensils
dinner_table = utensils.union(dishes)
#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)

