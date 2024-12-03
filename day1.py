import itertools

left_list = []
right_list = []
with open ('day1_aoc.txt', 'r') as file:
    for line in file.readlines():
        data_dump = line.split()
        left_list.append(int(data_dump[0]))
        right_list.append(int(data_dump[1]))

    left_list.sort()
    right_list.sort()

    total_distance = 0
    list_3 = []
    for item1, item2 in zip(left_list, right_list):

        if item1 > item2:
            difference = item1 - item2
            total_distance = total_distance + difference
            list_3.append(difference)
        else:
            difference = item2 - item1
            total_distance = total_distance + difference
            list_3.append(difference)

print(total_distance)


# how often each number from the left list appears in the right list
appear_in_right_list=0
similarity_score=0
for count1 in left_list:
    # similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
    total_appearance = count1 * right_list.count(count1)
    similarity_score += total_appearance

print(similarity_score)




