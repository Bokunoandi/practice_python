from random import randint
def rand_arr():
    RArr = []
    for i in range(0, 30):
        RArr.append(randint(-100, 100))
    return RArr
def max_in_arr(arr):

    arr_i = list(enumerate(arr, 0))
    max_i = max(arr_i, key=lambda i: i[1])

    return max_i[1], max_i[0]
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
print("sozdanii slychainii list :\n", arr)
print("maximalnii nomer > ", max_in_arr(arr)[0], "\npositiya of maximalnogo nomera > ", max_in_arr(arr)[1]+1)
if isinstance(unpaired_arr(arr), list):
    print("Spisok neparnih nomerov otsortirovan ot bolshih k malenkim :\n",
          sorted(unpaired_arr(arr), reverse=True))
else:
    print(unpaired_arr(arr))

