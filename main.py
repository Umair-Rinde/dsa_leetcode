class solution:
    
    def __init__(self):
        pass
    
    def twosum(self,nums:list,target:int )-> list:
        lookup = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup:
                return [lookup[complement],i]
            lookup[nums[i]] = i
        return []    