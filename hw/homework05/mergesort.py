import sys


def merge(list1, list2):
    empty_list = []
    new_list = []

    while list1 != empty_list and list2 != empty_list:
        a = int(list1[0])
        b = int(list2[0])

        if a < b:
            new_list.append(a)
            list1.pop(0)

        else:  # b <= a
            new_list.append(b)
            list2.pop(0)

    if list1 == empty_list:
        for item in list2:
            new_list.append(item)
    else:  # list2 == empty_list
        for item in list1:
            new_list.append(item)

    return new_list


def sort(unsorted):
    half = len(unsorted) // 2
    half_1 = unsorted[:half]
    half_2 = unsorted[half:]
    if len(half_1) != 1:
        half_1 = sort(half_1)
    if len(half_2) != 1:
        half_2 = sort(half_2)
    return merge(half_1, half_2)



if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as file1:
        nums = file1.readlines()

    sorted_nums = sort(nums)

    with open(output_file, "w") as file2:
        for num in sorted_nums[:-1]:
            file2.write(f"{num:03}\n")

        last_num = sorted_nums[-1]
        file2.write(f"{sorted_nums[-1]:02}")



    # with open(output_file, "w") as file2:
    #     i = 0
    #     while i > len(sorted_nums)-1:
    #
    #         for num in sorted_nums:
    #
    #             file2.write(f"{num}\n")