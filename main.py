# Find the most common element in a List in Python

from collections import Counter

a_list = ['one', 'one', 'one', 'two', 'two', 'three']

counter = Counter(a_list)

most_common = counter.most_common(1)[0][0]
print(most_common)  # 👉️ one

most_common_2 = counter.most_common(2)
print(most_common_2)  # 👉️ [('one', 3), ('two', 2)]