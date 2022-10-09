import yaml

data = {'computers': ['Lenovo', 'HP', 'ASUS'],
        'quantity': 3,
        'prices': {'Lenovo': '30000$',
                   'HP': '40000$',
                   'ASUS': '5000S'}}

with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


with open('file.yaml', 'r') as file:
    res = yaml.load(file, Loader=yaml.FullLoader)

print(data == res)
