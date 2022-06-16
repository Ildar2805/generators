
def flat_generator(nested):
	for sublist in nested:
		for item in sublist:
			yield item


# def flat_generator(nested): #пытался сделать 4* через рекурсию, но не получилось до конца разобраться. Подскажите, пожалуйста, в чем подвох.
# 	for sublist in nested:
# 		if isinstance(sublist, list):
# 			flat_generator(sublist)
# 		else:
# 			yield sublist


def main():
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f'],
		[1, 2, None],
	]

	for item in flat_generator(nested_list):
		print(item)

	print(list(flat_generator(nested_list)))


if __name__ == '__main__':
	main()
