import random
from math import floor, ceil

divider = '-------------------------------------------------'

def main():
    validSize = False
    size = 0
    while not validSize or size < 1 or size > 5:
        try:
            size = input('What size town? 1-5 or exit: ')
            if size.lower() == 'exit':
                return
            size = int(size)
            if size < 1 or size > 5:
                print('Invalid number.')
            else:
                validSize = True
        except:
            print('Invalid entry.')

    mod = size / 5
    shop = input('What type of shop? ').lower()
    if shop == 'spells': spells(mod)
    elif shop == 'adventure': gen('Adventure', mod)
    elif shop == 'alchemist': gen('Alchemist', mod)
    elif shop == 'artificer': gen('Artificer', mod)
    elif shop == 'general': gen('General', mod)
    elif shop == 'smith': gen('Smith', mod)
    elif shop == 'jeweler': gen('Jeweler', mod)
    elif shop == 'tailor': gen('Tailor', mod)
    else: print('Invalid shop type: %s' % shop)

def spells(mod):
    '''
    A magic item shop inventory generator for Era of Magic
    '''
    # Initialize spells with levels
    canList = []
    l1List = []
    l2List = []
    l3List = []
    with open('./Lists/SpellScrolls.csv') as f:
        doc = f.readlines()
        for line in doc:
            line = line.split(',')
            if line[1].strip() == 'Cantrip':
                canList.append(line[0])
            elif line[1].strip() == '1':
                l1List.append(line[0])
            elif line[1].strip() == '2':
                l2List.append(line[0])
            else:
                l3List.append(line[0])

    

    cantrips = random.randint(2, floor(15 * mod))
    l1 = random.randint(0, floor(10 * mod))
    l2 = random.randint(0, floor(5 * mod))
    l3 = random.randint(0, floor(2 * mod))

    stock = []

    for spell in range(cantrips):
        scroll = { 'name': '', 'price': 0, 'level': 'C' }
        scroll['name'] = random.choice(canList)
        scroll['price'] = random.randint(80, 120)
        stock.append(scroll)
    for spell in range(l1):
        scroll = { 'name': '', 'price': 0, 'level': '1' }
        scroll['name'] = random.choice(l1List)
        scroll['price'] = random.randint(130, 400)
        stock.append(scroll)
    for spell in range(l2):
        scroll = { 'name': '', 'price': 0, 'level': '2' }
        scroll['name'] = random.choice(l2List)
        scroll['price'] = random.randint(380, 700)
        stock.append(scroll)
    for spell in range(l3):
        scroll = { 'name': '', 'price': 0, 'level': '3' }
        scroll['name'] = random.choice(l3List)
        scroll['price'] = random.randint(580, 1200)
        stock.append(scroll)

    print('Spell Name                       | Price | Level')
    print(divider)
    for spell in stock:
        line = '%-32s | %5d | %s'
        print(line % (spell['name'], spell['price'], spell['level']))

def gen(type, mod):
    itemsList = []
    with open('./Lists/' + type + '.csv') as f:
        doc = f.readlines()
        for line in doc:
            line = line.split(',')
            item = { 'name': line[0], 'price': line[1], 'avail': line[2], 'min': line[3], 'max': line[4] }
            itemsList.append(item)

    stock = []
    for item in itemsList:
        inStock = (mod * float(item['avail']) * random.uniform(1.0, 4.0)) > 1
        if inStock:
            num = random.randint(int(item['min']), int(item['min']) if ceil(int(item['max']) * mod) < int(item['min']) else ceil(int(item['max']) * mod))
            price = random.uniform(float(item['price']) * 0.8, float(item['price']) * 1.35)
            if price < 0.1:
                price = 0.1
            stock.append({ 'name': item['name'], 'num': num, 'price': round(price, 1) })

    print('Item Name                       | Price | Stock')
    print(divider)
    for item in stock:
        line = '%-31s | %5.1f | %d'
        print(line % (item['name'], item['price'], item['num']))

main()