def mutiply_tuple (nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return temp

nums1 = (4, 3, 2, -1, 18)
print("og tulpe")
print(nums1)
print()

print("product - multiplying all number of the said tuple:",mutiply_tuple(nums1))
print()

nums2 = (2, 4, 4, 8, 8, 3, 2, 9)
print("og tulpe")
print(nums2)
print()

print("product - multiplying all number of the said tuple:",mutiply_tuple(nums2))
print()