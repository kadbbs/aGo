
#100到999里有多少个水仙花数


for item in range(100,1000):
    gei=item%10
    shi=item//10%10
    bai=item//100
    if(item==(gei*gei*gei+shi*shi*shi+bai*bai*bai)):
        print(item,"=",gei,"*",gei,"*",gei,"+",shi,"*",shi,"*",shi,"+",bai,"*",bai,"*",bai)
#列表
lst=['jiefj','af3',89,45,9,89,34,23,0,3,458,4567,6,]
lst1=[89,34,23,0,3,458,4567,6,]
lst4=[43,12,344354535345345,423432434234234234,]
lst.remove('af3')
lst.pop(0)
lst.pop()
print(lst1[1:3])
# lst1.append("dhtrdrth")
# lst.insert(0,'hefawihuiawheuifhawuiehfuiaweh')
# lst1.extend(lst)
# lst[6:]=lst4
# # for itea in  lst:
# #     print(itea,type(lst),id(lst[0]),id(lst),lst.index(89))
# print(lst[2::3])
# print(89 not in lst)
# # tu=range(1,6)
# # ui=range(7,9)
# # op=tu+ui
# # print(op)
# # io=lst1+lst
# # print(io)
print(lst)
print(lst1)
# lst=["eff",23,"trh4"]
# lst1=list(["eff",23,"trh4"])
# lis2=list(lst)
# print(lst,lst1,lis2)
# print(id(lst),id(lst1),id(lis2))
# lst3=lst
# print(id(lst3))



