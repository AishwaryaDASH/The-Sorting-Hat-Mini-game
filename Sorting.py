
from random import choice

print('Welcome sophomores to Hogwarts School Of Witchcraft and Wizardry!')
teams=['Ravenclaw', 'Gryffindor', 'Slytherin', 'Hufflepuff']
def userchoice():
	print('''Make your choice:
	1. Press 'A' to enter your own list of witches and wizards
	2. Press 'B' to watch sorting our selected list of would-be sorcerers''')
	ch=input()
	choice_entered=ch.strip()
	if choice_entered=='A' or choice_entered=='a':
		return True
	elif choice_entered=='B' or choice_entered=='b':
		return False
	else:
		print("Wrong item entered, let's try again")
		userchoice()
def sorting(players, m):
	L=list(players.strip().split(m))
	while len(L)>0:
		player=choice(L)
		print('{0} : {1}'.format(player, choice(teams)))
		L.remove(player)
ch=userchoice()
if ch==True:
	print("Enter your list of people for sorting to respective houses:")
	s=input()
	sorting(s, ' ')
else:
	print("Here we have some great names in the wizarding history!")
	file=open('in.txt','r')
	in_put=file.read()
	sorting(in_put, '  ')
