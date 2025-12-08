from hash_table import HashTable, Pair

# hash_table = HashTable(capacity = 1)
# for i in range(20):
#     pairs = len(hash_table)
#     empty = hash_table.capacity - pairs
#     print(f"{pairs:>2}/{hash_table.capacity:>2}", ("X" * pairs) + ("." * empty))
#     hash_table[i] = i
#
hashtable = HashTable(4)
hashtable._array = [Pair(0, 0), Pair(1, 1), Pair(2, 2), Pair(3, 3)]
del hashtable[1]
hashtable[5] = 5
print(hashtable)