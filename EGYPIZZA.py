n=input()
a=[0 for x in range(0,n+1)]
b=list
c=0
for i in range(0,n):
        c=raw_input()
        a[i]=c

b=list(a)
co3=a.count('3/4')
co2=a.count('1/2')
co4=a.count('1/4')
count=co3

rem=0
temp=0
if co3>=co4:
        co4=0
else:
        co4=co4-co3
if co2!=0 and co2%2==0:
        count=count+co2/2
elif co2!=0:
        count=count+int(co2/2)+1
        rem=1
        
if co4>=0:
        if co4<=2 and rem==1:
                co4=0
        else:
                co4=co4-rem*2
                temp=co4%4
                if temp==0:
                        count=count+co4/4
                else:
                        count=count+(co4/4)
                        count=count+1
                
print count+1      

