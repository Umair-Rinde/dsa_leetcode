from typing import List

class Solution:
	def __init__(self):
		pass
	def medianOfArray(self, num1:List[int], num2:List[int])->float:
		num3 = num1+num2
		num3.sort()
		if not num3:
			raise ZeroDivisionError("Both arrays are empty")
		mid = len(num3)//2
		if len(num3)%2 == 0:
			return  (num3[mid]+ num3[mid-1])/2.0
		return num3[mid]
