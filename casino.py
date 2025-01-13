# GitHub: codelao/Pocket-Casino
# ! Licensed under MIT

import random, sys, os, time


PATH = os.path.dirname(__file__)

def todays_x_calc():
	'''
	change value to increase/decrease win amount multiplier
	'''
	global todays_x
	todays_x = 3 # 3 is a multiplier size set by default

def generate_prizes():
	'''
	change range value to increase/decrease win chances
	'''
	for i in range(5): # there will be 5 numbers for each win type except jackpot
		free_bets.append(random.randint(0, 500)) # sets 5 random numbers from 0 to 500 for free bets
		wins.append(random.randint(501, 950)) # sets 5 random numbers from 501 to 950 for money win
	jackpot.append(random.randint(951, 1000)) # sets 1 random number from 951 to 1000 for jackpot

def wallet_actions(action, amount):
	with open(PATH+'/wallet.csv', 'r', encoding='utf-8') as f: ###
		wallet_file = f.read()
		content = wallet_file.split('\n')
		wallet = content[1].split(',')
		if action == 'deposit' or action == 'freebets':
			if action == 'deposit':
				update = [content[0], f'\n{amount},{wallet[1]}']
			elif action == 'freebets':
				update = [content[0], f'\n{wallet[0]},{amount}']
			with open(PATH+'/wallet.csv', 'w') as f2: ###
				f2.writelines(update[0])
				f2.writelines(update[1])
		elif action == 'current':
			return wallet

def x_calc(bet_size):
	if 1<=bet_size<=100:
		return 1
	elif 101<=bet_size<=1000:
		return 2
	elif 1001<=bet_size<=5000:
		return 3
	elif 5001<=bet_size<=10000:
		return 4
	elif 10001<=bet_size<=100000:
		return 5
	elif bet_size>100000:
		return 6

def win_size(common):
	if common == True:
		size = random.randint(0, 100)
		if 0<=size<=60:
			win = random.randint(1, 100)
			return win
		elif 61<=size<=85:
			win = random.randint(1, 1000)
			return win
		elif 86<=size<=97:
			win = random.randint(1, 10000)
			return win
		else:
			win = random.randint(1, 100000)
			return win
	elif common == False:
		win = random.randint(100001, 1000000)
		return win

def spin(x, bet_size):
	value = random.randint(0, 1000)
	if value in free_bets:
		return 'free bets'
	elif value in wins:
		win = win_size(True) * x + bet_size * todays_x
		return 'win', win
	elif value in jackpot:
		win = win_size(False) * x + bet_size * todays_x
		return 'jackpot', win
	else:
		return False



free_bets = []
wins = []
jackpot = []

def menu():
	correct_choice = False
	
	deposit = int(wallet_actions('current', 0)[0])
	freebets_left = int(wallet_actions('current', 0)[1])

	bet_txt = f'\n*___ Welcome ___*\n\nToday\'s X is {todays_x}!\nDeposit: ${deposit}\n{freebets_left} free bets left.\n\nChoose your bet size (or (Q)uit): $'
	bet_size = input(bet_txt)
	while correct_choice == False:
		if not bet_size.upper() == 'Q':
			if bet_size.isdigit():
				bet_size = int(bet_size)
				if bet_size <= 0:
					incorrect_bet_txt = f'Your bet should be between $1 and $1,000,000.\n\nDeposit: ${deposit}\n\nChoose your bet size (or (Q)uit): $'
					bet_size = input(incorrect_bet_txt)
				else:
					correct_choice = True
			else:
				bet2_txt = f'Incorrect input!\n\nDeposit: ${deposit}\n\nChoose your bet size (or (Q)uit): $'
				bet_size = input(bet2_txt)
		else:
			sys.exit(0)
	spin_again = True
	while spin_again == True:
		if deposit>=bet_size:
			if not freebets_left > 0:
				deposit -= bet_size
				result = spin(x_calc(bet_size), bet_size)
				freebets = 10 * x_calc(bet_size)
			else:
				freebets_left -= 1
				result = spin(1, 0)
				freebets = 10
			again_txt = f'Deposit: ${deposit}\n{freebets_left} free bets.\nSpin again? (Enter, or (Q)uit)\n'
			again2_txt = f'Incorrect choice!\n Press \'Enter\' to play more, or \'Q\' to exit.\n'
			nowin_txt = f'No win.\n'
			if result == False:
				print(nowin_txt)
				choice = input(again_txt)
			elif result == 'free bets':
				freebets_left += freebets
				freebet_txt = f'@@@//FREE BET TIME!//@@@\nYou just earned {freebets} free bets!\n'
				print(freebet_txt)
				choice = input(again_txt)
			elif result[0] == 'win':
				amount = result[1]
				deposit += amount
				win_txt = f'(w)---!WIN!---(w)\nYou just won ${amount}!\n!!!Congratulations!!!\n'
				bigwin_txt = f'*(w)*---!$!BIG WIN!$!---*(w)*\nYou just won ${amount}!\n!!!Congratulations!!!\n'
				if amount > 999:
					print(bigwin_txt)
					choice = input(again_txt)
				else:
					print(win_txt)
					choice = input(again_txt)
			elif result[0] == 'jackpot':
				amount = result[1]
				deposit += amount
				jackpot_txt = f'$$$#^^^___JACKPOT___^^^#$$$\n^^^^^^^ You just won ${amount}!\n!!!Congratulations!!!\n'
				print(jackpot_txt)
				choice = input(again_txt)
			###time.sleep(1)
			wallet_actions('deposit', deposit)
			wallet_actions('freebets', freebets_left)
			again_choice = False
			while again_choice == False:
				if not choice == '':
					if choice.upper() == 'Q':
						spin_again = False
						again_choice = True
					else:
						choice = input(again2_txt)
				else:
					again_choice = True
		else:
			not_enough_txt = f'Not enough funds! Returning back...\n\n'
			print(not_enough_txt)
			spin_again = False


def main():
	try:
		while True:
			todays_x_calc()
			generate_prizes()
			menu()
	except Exception as e:
		error_choice = input('\nUnexpected error occured. (V)iew more details? ')
		if error_choice.upper() == 'V':
			print(e)
		sys.exit(1)

if __name__ == '__main__':
	main()
