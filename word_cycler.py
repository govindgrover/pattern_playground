"""
	@author:
		Govind Grover [@govindgrover | @govindgroverji]

	@email:
		reach@govindgrover.com
	
	@description:
		A Python program to make n-combinations of any word of length 'n' such that
		each new word will start with each letter of the original word completing a
		cyclical movement.
	
	@example:
		In[]: python
		out[]: 
			python
			ythonp
			thonpy
			honpyt
			onpyth
			npytho
	
	@how-to-run:
		$ python word_cycler.py
"""

from os import system

system("cls")

while True:
	try:
		word = input("\nEnter any word: ")
		l = len(word)

		for i in range(l):
			print(word[i:l] + word[0:i])
		print()
	except KeyboardInterrupt:
		print("\nBye!! ;)")
		break
