Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

print('key value pair >>> ')
for i in Dictionary1:
    print('key:', i)
    print('value:', Dictionary1.get(i))

listOfKey = list(Dictionary1.keys())
print('\nlistOfKey >>> ', listOfKey)

Dictionary1.update({'C': 'Cars'})
print('\nkey value pair after updating >>> ')
for i in Dictionary1:
    print('key:', i)
    print('value:', Dictionary1.get(i))

