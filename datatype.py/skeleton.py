# def calc_total_price(apple_weight, APPLE_PRICE):
# 	return apple_weight * APPLE_PRICE

# def calc_return(total_price, money_given):
# 	if money_given < total_price:
# 		return -1


# 	return money_given - total_price


# def main():
# 	APPLE_PRICE = 21 # K vnd
# 	apple_weight = input("Enter weight of apples:")
# 	money_given = input("Total money customer give you:")

# 	apple_weight = float(apple_weight)
# 	money_given = float(money_given)


# 	total_price = calc_total_price(apple_weight, APPLE_PRICE)
# 	money_return = calc_return(total_price, money_given)

# 	if money_return == -1:
# 		print("Not enough cash")
# 	else:
# 		print("You need to return to customer" + str(money_return))

# main()

def print_return_info(total): # assumption
	# 500 200 100 50 20 10 1
	total = int(total) 
	count_500 = total/500
	total = total - 500*count_500
	print("500 : " + str(count_500))

	count_200 =  int(total/200)
	total = total - 200*count_200
	print("200 :" + str(count_200))

	count_100= int(total/100)
	total = total - 100*count_100
	print("100 :" + str(count_100))

	count_50 = int(total/50)
	total = total - 50*count_50
	print("50 :" + str(count_50))

	count_20 = int(total/20)
	total = total - 20*count_20
	print("20 : " +str(count_20))

	count_10 = int(total/10)
	total = total - 10*count_10
	print("10 :" + str(count_10))

	count_1 = total
	print(count_1)




print_return_info(input("Cash"))