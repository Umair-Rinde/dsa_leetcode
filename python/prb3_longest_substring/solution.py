class Solution:
	def __init__(self):
		pass

	def substring(self,s:str):

		char_index={}
		left = 0
		max_l = 0
		for i in range(len(s)):
			if s[i] in char_index and char_index[s[i]] >= left :
				left = char_index[s[i]]+1
			char_index[s[i]]=i

			max_l = max(max_l, i-left+1)
		return max_l
