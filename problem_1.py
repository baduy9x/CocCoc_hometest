from collections import Counter

sample = open('../../hash_catid_count.csv', 'r')
freq_counter = Counter()
total_counter = Counter()

for line in sample.readlines():
    object_id, cat_list, count_list = line.split("\t")
    object_id = int(object_id)
    cat_list = list(map(int, cat_list.strip()[1:-1].split(",")))
    count_list = list(map(int, count_list.strip()[1:-1].split(",")))
    for i, j in zip(cat_list, count_list):
        freq_counter[i] += 1
        total_counter[i] += j

print(freq_counter.most_common(1))
print(total_counter.most_common(1))

# For analyzing and visualize the data, we can create a pandas data frame such that contain 3 columns:
# 1: category
# 2: frequency
# 3: total_count