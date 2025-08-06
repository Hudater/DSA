# You are given an array of n - 1 integers which are in the range between 1 and n. All numbers appear exactly once, except one number, which is missing. Find this missing number.
# https://florian.github.io/xor-trick/

list1=[1,2,3,4,5,7]
list2=[1,2,3,4,5,6,7]
# print(f"List one:{list1} \nList two: {list2}\n")

# for element in list2:
#     print(f"Element: {element}, Type: {type(element)}")
# a = 10
# b = 4

# for i, j in zip(list1, list2):
#     # print(i, j)
#     print("a ^ b =", i ^ j)


def num_finder(list_in):
    num=0
    for i in range(len(list_in)):
        # print(f"Index {i} has {list_in[i]}")
        num^=list_in[i]
        # print("Sum is currenty: ", num)
    return num

sum_list1=(num_finder(list1))
sum_list2=(num_finder(list2))
# print(f"Sums are {sum_list1} and {sum_list2}")

print(f"Missing number is: {sum_list1+sum_list2}")
