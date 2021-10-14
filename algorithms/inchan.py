num_list = [1, 5, 3, 7, 9, 5, 9, 5]
input_1 = int(input())
input_2 = int(input())

# input_1 = int(input_1)
if input_1 % 2 == 1:
    num_list.append(input_1)

num_list = list(set(num_list))

if input_2 == 1:
    num_list.sort()
elif input_2 == 2:
    num_list.sort()
    num_list.reverse()
else:
    print('error')

print(*num_list)