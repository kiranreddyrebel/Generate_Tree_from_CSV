#by U.kiranvas Reddy

import csv
from treelib import Node, Tree

r=open('data.csv','r')
reader=csv.reader(r, delimiter=',')
w=open('test.csv','w')
writer=csv.writer(w, delimiter=',')


data1=set()

# it removes duplicate rows
#----------------------------

for row in reader:
	if row[1] not in data1:
		writer.writerow(row)
		data1.add(row[1])

w.close()
r.close()

# reading file data for tree
#----------------------------


reader=csv.reader(open('test.csv','r'), delimiter=',')


data=set()

tree=Tree()


parent=''
for row in reader:
    if row[3]=='':
        parent = row[1]  # now this stores parent node
        tree.create_node(parent,parent)

    if row[3]!='':   #now except parent node remain will be processed here
        tree.create_node(row[1],row[1],parent=row[3])

tree.show()
