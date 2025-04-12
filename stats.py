import sys
arg = sys.argv[1]
with open(arg) as c:

	file_contents = c.read()

	lowercase = file_contents.lower()

	def wcount():
		words = file_contents.split()
#		print (f"{len(words)} words found in the document")
		return len(words)

	def count_characters():
		cha_count = {}

		characters = list(lowercase)

		for character in characters:
			if character not in cha_count:
				cha_count[character] = 1
			else:
				cha_count[character] += 1
		return (cha_count)


	def make_report():
		word_count = wcount()
		cha_count = count_characters()
		cha_list = []
		sorted_list = []
		letter_num_list = []
		sort_letter_list = []
		letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
"æ", "â", "ê", "ë", "ô"]
		for x in cha_count:
			if x not in cha_list:
				cha_list.append({"name": x, "num": cha_count[x]})
		for i in cha_list:
			if i["name"] in letter_list:
				letter_num_list.append(i)
		for y in letter_num_list:
			def sort_on(dict):
	                        return dict["num"]
			letter_num_list.sort(reverse=True, key=sort_on)
		for z in letter_num_list:
			if z not in sorted_list:
				sorted_list.append({z["name"]: z["num"]})
		print ("============ BOOKBOT ============")
		print (f"Analyzing book found at {arg}...")
		print ("----------- Word Count ----------")
		print (f"Found {word_count} total words")
		print ("--------- Character Count -------")
		for i in letter_num_list:
			print (f"{i["name"]}: {i["num"]}")
		print ("============= END ===============")

