import re

def first_on_floor(input_str,floor):
	i = 0
	index = 0
	while i != floor:
		i += 1 if input_str[index] == "(" else -1
		print("Character {} -- {}\tFloor -- {}".format(index, input_str[index], i))
		index+=1
	return index

if __name__ == "__main__":
	input_file = open("input_1.txt", "r")
	input_data = input_file.read()
	input_file.close
	print(input_data)

	# PART 1 -- Find final floor
	pos = re.findall("\(", input_data)
	neg = re.findall("\)", input_data)
	res = len(pos) - len(neg)
	print("Final Floor -- {}".format(res))
	
	#PART 2 -- Get first time on a certain floor as index of character in input string
	floor = -1
	res = first_on_floor(input_data,floor)
	print("First time on Floor {} -- {}".format(floor,res))
	
