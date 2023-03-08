group = ["John", "Mike", "Bob", "Taras", "Bob"]
# 2 arr
arr = [1, 23, 13,]

# 1) Find Mikes index

print(group.index("Mike"))

# 2) Slice arr from 0 to 3 and save it into new variable

group_slice = group[0:3]
print(group_slice)

# 3) Count , how much Bobs into arr

counter = 0
bobs = 0
while counter < len(group):
    if group[counter] == "Bob":
        bobs += 1
    counter += 1
print(bobs)

# 4) Remove Taras from arr

group_rem = group[:]
group_rem.remove("Taras")
print(group_rem)

# 5) Sort arr

print(sorted(group))

# 6) Join two arrays into one
# 7) Joined arr must be a string
arr_str = arr[:]
i = 0
while i < len(arr):
    arr_str[i] = str(arr_str[i])
    i += 1

print (arr_str)
print(type(arr_str[0]))

group_join = group
group_join.extend(arr_str)
print(group_join)
