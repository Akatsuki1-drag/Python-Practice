def pair_sum(list1, unique_no):
    count = 0
    sum_set = set()
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i == j:
                continue
            else:
                if list1[i] + list1[j] == unique_no:
                    if list1[i] in sum_set and list1[j] in sum_set:
                        continue
                    else:
                        count +=1
                        sum_set.add(list1[i])
                        sum_set.add(list1[j])
    return count            


print(pair_sum([1,2,3,1],3))