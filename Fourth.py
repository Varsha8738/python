#sample list
list1 = [1,2,3,4,5]
list2 =[1,"Hi",4.5]
print(list1)
print(list2)
#accessing with index number
print(list2[1])
#update list with append()
list2.append("Hello")
print(list2)
#changing values of list using index
list2[0]="CSE"
print(list2)
#remove item from list
list2.remove('Hi')
print(list2)
#length of list and type
print(len(list1))
print(type(list1))
-->OUTPUT
[1, 2, 3, 4, 5]
[1, 'Hi', 4.5]
Hi
[1, 'Hi', 4.5, 'Hello']
['CSE', 'Hi', 4.5, 'Hello']
['CSE', 4.5, 'Hello']
5
<class 'list'>
