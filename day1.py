l1 = []
l2 = []

f = open("day1.txt", "r")
for line in f:
    split_line = line.split()
    l1.append(int(split_line[0]))
    l2.append(int(split_line[1]))

l1.sort()
l2.sort()
distance_sum = 0

for i in range(len(l1)):
    distance_sum += abs(l1[i] - l2[i])

print(distance_sum)