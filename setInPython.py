coders = set(["Arnav","Goransh","mani","parul"])
analysts = set(["Krish","Mehak","shiv","Goransh","mani"])
print ("coders: ",coders)
print ("analysts",analysts)

print("people working as coder as well as analysts : ",coders.intersection(analysts))
print("people working as coders or analysts: ",coders.union(analysts))
print("people working as coder but not analysts : ",coders.difference(analysts))
print("people working as analysts but not coders : ",analysts.difference(coders))
print("people working in only of the groups : ",coders.symmetric_difference(analysts))