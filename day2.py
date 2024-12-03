# Day 2
class Unsafe(Exception):
    pass

final_lisp=[]
count1 = 0


def safe_unsafe_append_print(diff, param):
    if param:
        final_lisp.append("Safe")
    else:
        final_lisp.append("Unsafe")
    print(diff, " | ", final_lisp[-1])


with open("day2_aoc", "r") as file:
    for line in file.readlines():
        count1 += 1
        lisp = []
        diff = []
        data_dump = line.split()
        for jtem in data_dump:
            lisp.append(int(jtem))

        i=0
        try:
            while i < len(lisp)-1:
                if not lisp[i] - lisp[i+1] == 0:
                    diff.append(int(lisp[i]) - int(lisp[i+1]))
                    i+=1
                else:
                    raise Unsafe
            count_of_positives = 0
            count_of_negatives = 0
            # all increasing and decreasing
            for item in diff:
                if item > 0:
                    count_of_positives += 1
                else:
                    count_of_negatives += 1
            if count_of_positives == len(diff) or count_of_negatives == len(diff):
                # difference is 1 or <=3
                for num in diff:
                    if abs(num) > 3 or abs(num) < 1:
                        raise Unsafe
                safe_unsafe_append_print(diff, True)
            else:
                raise Unsafe

        except Unsafe:
            safe_unsafe_append_print(diff, False)


final_count=0
for k in range(len(final_lisp)):
    if final_lisp[k] == 'Safe':
        final_count += 1

print('Safe count: ',final_count)
print('count1: ',count1)
