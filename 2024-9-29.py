import string
import sys
import math
import os
import string
import random
from collections import defaultdict
sys.setrecursionlimit(100000)
re=[]
n=int(input())
def max_list(mylist):
    max_value1=max(mylist)
    mylist.remove(max_value1)
    for i in mylist:
        max_value1=max(i+max_value1,max_value1)
    return max_value1
def max_s(table_tree,n):
    if not table_tree[n]:
        re.append(tree_value[n])
        return tree_value[n]
    temp_table=[]
    max_value=0
    while  table_tree[n]:
        i=table_tree[n].pop(0)
        table_tree[i].remove(n)
        temp_table.append(max_s(table_tree,i))
    max_value=max_list(temp_table)
    re.append(max_value+tree_value[n])
    return max(max_value+tree_value[n],tree_value[n])
table_tree=defaultdict(list)
tree_value=list(map(int,input().split()))
for i in range(n-1):
    v,u=map(int,input().split())
    table_tree[v-1].append(u-1)
    table_tree[u-1].append(v-1)
re.append(0)
max_s(table_tree,0)
print(max(re))
