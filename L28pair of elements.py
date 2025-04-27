class pair_elements:
    def twoSum(self, nums, target):
        # create a cmpty dictionary
        lookup = {}

        #iterate throughthe tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            
            lookup[num] = i

#take inputof dum from the user
value = int(input("enter sum ofr which you want to make this search : "))

#creating object
obj = pair_elements()
result = obj.twoSum((10,20,30,40,50,60,70),value)

print(f"index={result}" )