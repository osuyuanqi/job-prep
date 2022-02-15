# **********************************************
# 383. Ransom Note
# **********************************************
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	# not necessary
	# if len(magazine) < len(ransomNote):
	#     return False 
	# logic calculation, {} is false and not {} is True
	return not collections.Counter(ransomNote) - collections.Counter(magazine)
if __name__ == "__main__":
	print('test')
