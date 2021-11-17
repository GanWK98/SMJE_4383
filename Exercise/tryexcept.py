#read a particular line from a file. User provides both the line number and file name

file_str = input("Open what file:")
find_line_str = input("Which line (integer):")

try:
	input_file = open(file_str)	#potential user error
	find_line_int = int(find_line_str)	#potential user error
	line_count_int = 1
	for line_str in input_file:
		if line_count_int == find_line_int:
			print("Line {} of file {} is {}". format(find_line_int, file_str, line_str))
			break

		else:
			#get here if line sought doesn't exist
			print("Line {} of file {} not found". format(find_line_str, file_str))
		line_count_int += 1
		
	input_file.close()

#Added Except Error
except:
	pass
