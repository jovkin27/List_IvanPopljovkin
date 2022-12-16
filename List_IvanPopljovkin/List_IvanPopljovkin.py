##Задание 2
#list1=[123, 'list', 'Ivan', 27, 228, 1337]
#print(list1)
#print("Valige!Mitu elementid soovib muuta?")
#while True: 
#    ask=int(input("-> "))
#    if ask==1:
#        a=list1.pop(0)
#        b=list1.pop(4)
#        list1.insert(4,a)
#        list1.insert(0,b)
#        print(list1)
#    elif ask==2:
#        a=list1.pop(0)
#        b=list1.pop(4)
#        list1.insert(4,a)
#        list1.insert(0,b)
#        c=list1.pop(1)
#        d=list1.pop(3)
#        list1.insert(3,c)
#        list1.insert(1,d)
#        print(list1)
#    elif ask==3:
#        list1.reverse()
#        print(list1)
#    if ask>=4:
#        print('Maximum 3 elementid') 
#        break 

##Задание 3
#list2=[25, 11, 65, 1, 20]
#print(list2)
#list_copy=list2.copy()
#list_copy.sort()
#list_copy.reverse()
#suurem=list_copy[0]
#answer=suurem / len(list2)
#list2.pop(2)
#list2.insert(2,round(answer))
#print(list2)

#Задание 4
user_list=[]
numbrid=int(input('Kirjutage mitu numbrid '))
for i in range(0,numbrid):
    j=int(input())
    user_list.append(j) 
print('Loendi sortimine kahanevas järjekorras[1] või tõusvas järjestuses[2]')
qs=int(input('->'))
if qs==1:
    user_list.sort()
    user_list.reverse()
    print(user_list)
if qs==2:
    user_list.sort()
    print(user_list)
else:
    print('Error')

