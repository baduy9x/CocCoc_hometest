from collections import Counter
import pandas as pd

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
# 2: freq
# 3: total

df_freq = pd.DataFrame.from_dict({"cat": freq_counter.keys(), "freq": freq_counter.values()})
df_total = pd.DataFrame.from_dict({"cat": total_counter.keys(), "total": total_counter.values()})

df_stat = pd.merge(df_freq, df_total, on = 'cat')
print(df_stat.head())

print(df_stat.describe())
