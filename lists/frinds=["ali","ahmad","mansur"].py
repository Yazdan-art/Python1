# frinds=["ali","ahmad","mansur"]
# for frind in frinds:
#     print("hello ",frind)
# print("done")   
# frinds[0] ="mohammd"
# print(frinds)
#______________________________
# t=[0,1,2,3,4,5]
# print(t[:])
# print(t[1:3])# از ابتدای یک تادابتدای 3
# print(t[:3])
#______________________
# x=list()
# print(type(x))
# print(dir(x))


#_______________________________
# stuff=list()
# stuff.append("Yazdan")
# stuff.append(30)
# stuff.append(20.0)
# print(stuff)
# print("Yazdan"in stuff)
#______________________________
# names=list()
# names.append("ali")
# names.append("ahmad")
# names.append("nima")
# families=["ahmadi","abasi"]
# print(families)
# families=names+families
# age=[19,20,30]
# families=families+age
# print(families)
# families.sort()
# print(families)
# # print(names)
# # names.sort()
# # print(names)
# # print(names[0])
#__________________________
rate=list()
while 1:
    inp=input("enter your rate")
    if inp=="done" :
        break
    inp = int(inp)
    rate.append(inp)
print(sum(rate)/len(rate))    

