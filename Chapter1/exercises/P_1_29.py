def choose_perm(arr, k):
    if len(arr) == 1:
        return [arr]
    else:
        if k == 1:
            return list(list(arr[i]) for i in range(len(arr)))
        else:
            result = []
            for i in range(len(arr)):
                rest_arr = arr[:i] + arr[i+1:]
                rest_list = choose_perm(rest_arr, k-1)
                new_list = []
                for perm in rest_list:
                    new_list.append([arr[i]] + perm)
                result += new_list
            return result


words = ['c', 'a', 't', 'd', 'o', 'g']
temp = []
for num in range(1, len(words)+1):
    temp += choose_perm(words, num)
array = []
for item in temp:
    array.append(''.join(item))
print(array)
