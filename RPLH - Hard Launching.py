import math
import sys
t=input()
i=0
while t>0:
        i+=1
        t=t-1
        a,b=map(float,raw_input().split())
        g=9.806
        temp=(a*g)/(b*b)
        if temp<=1:
                ans=math.asin(temp)*180/(2*math.acos(0.0))
                sys.stdout.write('Scenario #'+str(i)+': '+str(format(round(ans/2,2),'.2f')))
                print ''
        else:
                sys.stdout.write('Scenario #'+str(i)+': '+str(-1))
                print ''
        
