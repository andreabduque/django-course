option = 'nenhuma'

while(option != '0'):
	option = input("type an option: 1- talk to me 2-exit\n")

	if(option == '1'):
		names_string = input("Say names. Separate them with blankspace\n")

		names = names_string.split(',')

		for name in names:
			if(name == 'andrea'):
				print("hi " + name.strip())
			else:
				print("hi " + name)

	elif(option == '2'):
		print("bye")
		break
	else:
		print('invalid option')


	
