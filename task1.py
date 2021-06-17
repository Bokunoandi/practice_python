from random import randint
def rand_arr():
RArr = []
for i in range(0, 30):
RArr.append(randint(-100, 100))
return RArr
def max_in_arr(arr):
max = arr[0]
max_i = 0
for i in range(len(arr)):
if arr[i] > max:
max = arr[i]
max_i = i
return max, max_i
def unpaired_arr(arr):
un_p_arr = []
for i in arr:
if i % 2 != 0:
un_p_arr.append(i)
if len(un_p_arr) == 0:
return "net parnih nomerov"
else:
return un_p_arr
arr = rand_arr()
print("initial random list :\n",arr)
print("max num > ", max_in_arr(arr)[0], "\nposition of max num > ", max_in_arr(arr)[1]+1)
if isinstance(unpaired_arr(arr), list):
print("Spisok neparnih nomerov otsortirovan ot bolshih k malenkim :\n",sorted(unpaired_arr(arr), reverse=True))
else:
print(unpaired_arr(arr))


