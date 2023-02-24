group = ["John", "Mike", "Bob", "Taras", "Bob"]
# 2 arr
arr = [1, 23, 13,]

# 1) Find Mikes index
# 2) Slice arr from 0 to 3 and save it into new variable
# 3) Count , how much Bobs into arr
# 4) Remove Taras from arr
# 5) Sort arr

# 6) Join two arrays into one
# 7) Joined arr must be a string

print(group.index("Mike"))

group_next = group[0:3]
print(group_next)

counter = 0
bobs = 0
while counter < len(group):
    if group[counter] == "Bob":
        bobs += 1
    counter += 1
print(bobs)

group_rm = group.remove("Taras")
print(group_rm)

print(sorted(group))

group_ex = group.extend(arr)
print(group_ex)

arr_str = str(arr)
print(type(arr_str[0]))
