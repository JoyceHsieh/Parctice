# print("1234")

# # 四則運算

# x=int(input("Number1:"))
# y=int(input("Number2:"))
# z=x*y
# print(z)
# if z>100:
#     print("Con")
# elif z>50:
#     print("Don")
# else:
#     print("Fales")

# #BMI 
# x=float(input("m:"))
# y=float(input("kg:"))
# z=y/x**2
# print(z)
# if z<18.5:
#     print("too light")
# elif 18.5<z<23.9:
#     print("normal")
# elif 24<z<27.9:
#     print("too heavy")
# else:
#     print("over heavy")

# n=int(input("輸入一個正整數："))
# for i in range(1,n+1):
#     if i%5==0:
#         continue
#     print(i,end="")


# n=int(input("請輸入大樓層數："))
# for i in range(1,n+1):
#     if i==4:
#         continue
#     print(i,end=" ")


#d = {'A':100,'B':1000, 'Joyce':'Learning','Tim':['student','claremont','CGU','CISAT','MBA']} 
dic={"A":100,"B":1000,"Joyce":"Learning","Tim":["student","claremont","CGU","CISAT","MBA"]}
key1=dic.keys()
print(key1)  #Q1
values1=dic.values()
print(values1) #Q2
for x in key1:
    for y in values1:
        print(x,y)
