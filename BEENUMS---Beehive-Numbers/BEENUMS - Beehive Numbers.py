'''A beehive is an enclosed structure in which some honey bee species live and raise their
young. In this problem we consider a two-dimensional sketch of the beehives. Each
beehive is composed of a certain number of cells, where each cell is a regular hexagon.
Each cell may have some neighbors, which are other cells that share a side with that cell.
A cell with exactly 6 neighbors is an internal cell, while a cell with fewer neighbors is an
external one. Notice that an external cell can always be changed to internal by adding
some neighbor cells.


We are interested in a particular class of beehives. This class of valid beehives is defined
recursively as follows: a) a single cell is a valid beehive; and b) given a valid beehive B,
if we add the minimum number of cells such that each external cell of B becomes an
internal cell, the result is a valid beehive.

The number of cells in a valid beehive is called a beehive number. Given an integer N ,
you must decide whether it is a beehive number.'''

a=[0]*100000
a[0]=1
for i in range(1,100000):
    a[i]=a[i-1]+6*(i-1)
while True:
    t=input()
    if t==-1:
        break
    if t in a:
        print 'Y'
    else:
        print 'N'


    
