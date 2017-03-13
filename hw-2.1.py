# яичница, 2 яйца, 100гр помедор
# Стейк, мясо 300гр. специи 5 гр, масло 10 гр
# Салат , помидор 100гр, огурцы 100гр, масло 100гр, лук 1 шт 
cooc_book = {}
ingridients = []
ingridient = {}
ingridient_name = ''
quantity = ''
meassure = ''

f = open('file1.txt', encoding = 'UTF-8')
for dish in f:
  ingridients.clear()
  i = int(f.readline())
  print(i)
  while i > 0:
    print(cooc_book)
    print('--')
    line = f.readline()
    ingridient_name, _, quantity, _, meassure = line.split()
    ingridients.append({'ingridient_name' : ingridient_name, 'quantity' : int(quantity), 'meassure' : meassure})
    i -= 1
  print(dish[:-1])
  
  print(cooc_book)
  print('---')
  
  cooc_book[dish[:-1]] = ingridients[:]
  
  print(cooc_book)
print('---------')
print(cooc_book)

f.close()


cooc_booc = {
  'яичница': [
    {'ingridient_name':'яйца', 'quantity': 2, 'meassure': 'шт'},
    {'ingridient_name':'помидоры', 'quantity': 100, 'meassure': 'гр'},
    ],
  'стейк':[
    {'ingridient_name':'говядина', 'quantity': 300, 'meassure': 'гр'},
    {'ingridient_name':'специи', 'quantity': 5, 'meassure': 'гр'},
    {'ingridient_name':'масло', 'quantity': 10, 'meassure': 'мл'},
    ],
  'салат':[
    {'ingridient_name':'огурцы', 'quantity': 100, 'meassure': 'гр'},
    {'ingridient_name':'помидоры', 'quantity': 100, 'meassure': 'гр'},
    {'ingridient_name':'масло', 'quantity': 100, 'meassure': 'мл'},
    {'ingridient_name':'лук', 'quantity': 1, 'meassure': 'шт'},
    ]
  }
  
  
dishes = ['яичница','стейк','стейк']
person_count = 3

shop_list = {}

for dish in dishes:
  for ingridient in cooc_book[dish]:
    new_shop_list_item = dict(ingridient)
    new_shop_list_item['quantity'] *= person_count
    if new_shop_list_item['ingridient_name'] not in shop_list:
      shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
    else:
      shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
      
for shop_list_item in shop_list.values():
  print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],shop_list_item['meassure']))

print('------')   
   
for shop_list_item in shop_list.values():
  print('{ingridient_name} {quantity} {meassure}'.format(**shop_list_item))   
   