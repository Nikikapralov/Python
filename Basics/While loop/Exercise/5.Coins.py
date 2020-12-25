change = float(input())
change_coins = change * 100

number_of_coins = 0
while True:
   if change_coins - 200 >= 0:
       change_coins -= 200
   elif change_coins - 100 >= 0:
       change_coins -= 100
   elif change_coins - 50 >= 0:
       change_coins -= 50
   elif change_coins - 20 >= 0:
       change_coins -= 20
   elif change_coins - 10 >= 0:
       change_coins -= 10
   elif change_coins - 5 >= 0:
       change_coins -= 5
   elif change_coins - 2 >= 0:
       change_coins -= 2
   elif change_coins - 1 >= 0:
       change_coins -= 1
   number_of_coins += 1
   if change_coins < 1:
       break


print(number_of_coins)


