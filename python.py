"""#Calculator
number_1 = int(input())
operation=input()
number_2 = int(input())

if operation == '+':
    print('{} + {} ='.format(number_1, number_2),number_1 + number_2)

elif operation == '-':
    print('{} - {} ='.format(number_1, number_2),number_1 - number_2)

elif operation == '*':
    print('{} * {} ='.format(number_1, number_2),number_1 * number_2)

elif operation == '/':
    print('{} / {} ='.format(number_1, number_2),number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')"""
#password


"""print("Password 8-13 araligi olmalidir")
password=input('Enter password:')
if len(password)>=8 and len(password)<=13:
	print(password)
else:
	print("Password yeteri qeder uzun deyil!")"""
#Teyin edilen parol	
"""password="sureyya2003"
i=1
while i<=3:
	parol=input('Parolu daxil edin:')
	if parol==password:
		print("Sistemə daxil oldunuz!")
		break
	else :
		print("Yalnis giris")
	i+=1
	if i==4:
		print("Cehd sayi bitdi")
		break"""

eded_1=int(input())
eded_2=int(input())
print(eded_1/eded_2)
while True:
	try:
		a=int(input("Daxil edin:"))
		b=int(input("Daxil edin:"))
		print(a/b)
	except ZeroDivisionError:
		print("0-a bolunmur")
	except ValueError:
		print("Yalnis datatype")
	except:
		print("Yalnis prosess")