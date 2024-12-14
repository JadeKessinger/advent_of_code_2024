def sum_distance(l1, l2):
    ''' 
    Calculates the sum of the distances between two lists by sorting them and taking the difference between every pair 
    of elements.
    
    Inputs:
    - l1 and l2, two integer lists of equal length
    
    Outputs:
    - the sum of the distances between each pair of sorted elements 
    '''
    l1.sort()
    l2.sort()
    distance_sum = 0

    for i in range(len(l1)):
        distance_sum += abs(l1[i] - l2[i])

    return distance_sum

def calculate_similarity_score(l1, l2):
    '''
    Calculates the similarity score between two lists by multiplying the number of times an integer from the first list 
    appears in the second list by that integer.
    
    Inputs:
    - l1 and l2, two integer lists of equal length
    
    Outputs:
    - the similarity score
    '''
    similarity_score = 0
    l1_set = set(l1)
    for i in l1_set:
        similarity_score += l2.count(i) * i

    return similarity_score

l1 = []
l2 = []

f = open("day1.txt", "r")
for line in f:
    split_line = line.split()
    l1.append(int(split_line[0]))
    l2.append(int(split_line[1]))

print(calculate_similarity_score(l1, l2))