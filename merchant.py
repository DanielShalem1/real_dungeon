import inventory
PRICES_DICT = {'Elixir':5, "Clarity Water":3, 'Cleansing Water':7, "Warrior's Potion":4}
import helpers


def trade(seller, buyer, item, price):
    seller.money += price
    inventory.reduce_item(seller.inventory, item)
    buyer.money -= price
    inventory.add_item(buyer.inventory, item)



def buying(seller, buyer):
    print("{} has: ".format(helpers.name_pick(seller)))
    inventory.present_inventory(seller.inventory)
    print("{} money: {} | {} money: {}".format(helpers.name_pick(seller), seller.money, helpers.name_pick(buyer), buyer.money))
    items = list(seller.inventory.keys())
    items_names = [item.name for item in items]
    user_input = input("chose item to buy: {}".format(items_names + ['exit', 'item description']))
    while not helpers.valid_value(user_input, len(items)+2):
        user_input = input("chose item to buy: {}".format(items_names + ['attacks', 'item description']))
    item_index = int(user_input)
    real_item_index = item_index -1

    while real_item_index == len(items)+1: #the user choose the to show the items' description
        print("{} has: {}".format(helpers.name_pick(seller), inventory.present_inventory(seller.inventory)))
        user_input = input("chose item to buy: {}".format(items_names + ['attacks', 'item description']))
        while not helpers.valid_value(user_input, len(items) + 2):
            user_input = input("chose item to buy: {}".format(items_names + ['attacks', 'item description']))
        item_index = int(user_input)
        real_item_index = item_index - 1

    if real_item_index == len(items):  # the user chose to exit
        print("thank you come again!")
        return 0
    else:
        item = items[real_item_index]
        price = PRICES_DICT[item.name]
        if buyer.money >= price:
            trade(seller, buyer, item, price)
        else:
            print("do not have enough money")
        return buying(seller, buyer)

