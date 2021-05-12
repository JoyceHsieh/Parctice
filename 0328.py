def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)
calculate(10)
calculate(20)

def power(base,exp=0):
    print(base**exp)
power(3,2)
power(4)

#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n1=5,n2=10)

def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)


# sys模組：取得系統相關資訊
import sys
print(sys.platform)
print(sys.maxsize)

