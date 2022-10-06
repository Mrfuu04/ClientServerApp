import json


def write_order_to_json(item, quantity, price, buyer, date):
    result_dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', encoding='utf-8') as f:
        content = json.load(f)

    with open('orders.json', 'w', encoding='utf-8') as f:
        main_list = content.get('orders')
        main_list.append(result_dict)
        json.dump(content, f, ensure_ascii=False)


write_order_to_json('Ручка', '20', '140', 'Тест', '22.09.1995')
