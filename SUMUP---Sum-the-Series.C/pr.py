//Nilendu is a brilliant student of Mathematics and always scores A+ in it. 
His professor RamjiLal is quite impressed seeing his mathematical skills and asks him to sum the following series:

1/3 + 2/21 + 3/91 + 4/273 + .....

But the fact is Nilendu is quite lazy to do his assignment. 
He has to watch a film and many other activities to do. So he asks you for your help. Will you be able to solve it ??//
a=[]
for _ in xrange(0,int(raw_input())):a.append(input())
for i in range(0,len(a)):print format((0.5-0.5/(a[i]*a[i]+a[i]+1)),'.5f')
