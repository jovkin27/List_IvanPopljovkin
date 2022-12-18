#Задание 1
#linn=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa,","Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#index=""
#n=0
#while type(index)!=int or n!=5:
#    try:
#        index=int(input("Sisesta index> "))
#        n=len(str(index))
#    except:
#        print("Vale index!")

#index_list=list(str(index)) 
#index_list[0]
#print(linn[int(index_list[0])-1])

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

##Задание 4
#user_list=[]
#numbrid=int(input('Kirjutage mitu numbrid '))
#for i in range(0,numbrid):
#    j=int(input())
#    user_list.append(j) 
#print('Loendi sortimine kahanevas järjekorras[1] või tõusvas järjestuses[2]')
#qs=int(input('->'))
#if qs==1:
#    user_list.sort()
#    user_list.reverse()
#    print(user_list)
#if qs==2:
#    user_list.sort()
#    print(user_list)
#else:
#    print('Error')

#Задание 5
a=['крот', 'белка', 'выхухоль']
b=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
c=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']

#a_max=len(max(a, key=len))
#a0=len(a[0])
#s=a_max-a0
#g=a[0]
#for i in range(s):
#    if len(a[0])<a_max:
#       g+='_'
#    if a[0]==a_max:break
#a.pop(0)
#a.insert(0,g)

#a1=len(a[1])
#s=a_max-a1
#g=a[1]
#for i in range(s):
#    if len(a[1])<a_max:
#       g+='_'
#    if a[1]==a_max:break
#a.pop(1)
#a.insert(1,g)
#print(a)

#b_max=len(max(b, key=len))
#b0=len(b[0])
#b1=len(b[1])
#b2=len(b[2])
#b3=len(b[3])
#for i in range(b_max):
#    if b0<b_max and b1<b_max and b2<b_max and b3<b_max :
#       b[0]+='_'
#       b[1]+='_'
#       b[2]+='_'
#       b[3]+='_'
#    if len(b[0])==len(b[1])==len(b[2])==len(b[3])==b_max:break
#print(b)

#Задание 6
nimi=input('Nimi->')
a=nimi[0].upper()
b=nimi[1::]
name=a+b
print(f"Tere tulemast {name}")
pik=len(nimi)
print(f'Sinu nimis on {pik} tähted')
nimi_list=(list(nimi))
nimi_list.sort()
c=nimi_list
print(c)
#не понял