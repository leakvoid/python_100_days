from art import logo

print(logo)

def clear():
    for i in range(10):
        print('\n')

bid_dict = {}

is_another_bid = True
while is_another_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid(in $)?: "))
    bid_dict[name] = bid

    is_another_bid = True if input("Are there any other bidders(yes or no)?: ") == "yes" else False
    clear()

max_bid_name = ""
max_bid = 0
for key in bid_dict:
    if bid_dict[key] > max_bid:
        max_bid = bid_dict[key]
        max_bid_name = key

print(f"Max bidder is {max_bid_name} with amount {max_bid}$")