print("123456")

y=0
for x in range(11):
    z=y+x
print(z)

y=0
for x in range(11):
    y=y+x
print(y)


# 1+2+3+4+.....10
n=1
y=0  #紀錄累家的結果
while n<=10:
    y=y+n
    n+=1
print(y)


#break sample
n=0
while n<5:
    if n==3:
        break
    print(n) #印出迴圈中的n
    n+=1
print("最後的n",n) #印出迴圈結束後的n


#contunue
n=0
for x in [0,1,2,3,]:
    if x%2==0: #取餘數，x為偶數
        continue
    print(x)
    n+=1
print("最後的n",n)


#else sample
sum=0
for x in range(11):
    sum=sum+x
else:
    print(sum) 
print(sum)

n=input("輸入一個正整數：")
n=int(n) #轉換輸入的數億
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數的平方根")

    