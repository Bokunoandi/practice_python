import random
random.seed()

list1=[]
list2=[]
serial=0
n_serial=0
biggest=-101

for i in range(30):
    list1.append(random.randint(-100, 100))
print("First list: \n", list1)

for number in list1:
    serial+=1
    if number>biggest:
        biggest=number
        n_serial=serial
print("Max num =", biggest, ". Its serial number =" , n_serial)

for i in range(len(list1)):
    if list1[i]%2!=0:
        list2.append(list1[i])
list2.sort(reverse=True)
print("List with odd numbers in descending order: \n", list2)
