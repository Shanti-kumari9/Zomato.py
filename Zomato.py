List_of_items = ['panir-chaumin', 'pija', 'maggi', 'bargar']
Price_of_items = [100, 200, 300, 400]

username = input('Please enter your Username : ')
print ('Hii!!!👋 {}, Welcome to Zomato....:)'.format(username))
passwd = input('Please enter your Password : ')
re_enter_passwd = input('Please enter your Password : ')

if passwd == re_enter_passwd:
    print ('Welcome to Zomato   :)')
print ('\nPlease, Choose your location number where delivery will reach.....:)\n\n')


location = ['Delhi', 'Haryana', 'UP', 'Banglore', 'Pune', 'Karnatak']
a = 0
while a < len(location):
    print(a + 1, '  ', location[a])
    a += 1
Location_to_reach = int(input())
Location_choosen = location[Location_to_reach - 1]

print('Choose items what you want to order.....:)')
a=0

while a < len(List_of_items):
    print(a + 1,'  ', List_of_items[a],'  ----   ₹', Price_of_items[a])
    a += 1
Items_to_cart = []
No_of_items = []
Price_to_cart = []

Want_to_choose_items = input( 'For Placing order, Enter "no" or "YEs : ')
if Want_to_choose_items == 'no':
    break
while Want_to_choose_items == 'no' or Want_to_choose_items == 'yes':
    items = (int(input('Enter item number which you want to order : ')))
    Items_to_cart.append(List_of_items[items - 1])
    print(Items_to_cart)

    print ('Enter quantity of {} : '.format(Items_to_cart[-1]))
    No_of_items.append(int(input()))

    print ('You ordered these items......')
    i = 0
    while i < len(Items_to_cart):
        print(Items_to_cart[i],'   ', No_of_items[i])
        i += 1

    Want_to_choose_items = input('Want More !!! \nEnter "no" or "YES" : ').lower()

else: 
    print('Wrong Input....')

Price_to_cart = []
Total = 0

for i in Items_to_cart:
    for j in List_of_items:
        if i == j:
            Price_of_cart = Price_of_items[List_of_items.index(j)]
            Price_to_cart.append(Price_of_cart)
            print(Price_to_cart)

for i in range(len(Price_to_cart)):
    Total += Price_to_cart[i] *No_of_items[i]


print ('\nTotal Amount of your Items = ', Total)
print('\nYour Items Will Deliver to {}'.format(Location_choosen))
print('\nThank You For Giving Us A Chance To Offer......\nWelcome Again.....:)')