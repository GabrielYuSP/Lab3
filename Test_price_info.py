import price_info

def test_total_cost_shopping():
    test_price_list = {'apple': 1.40, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70}
    test_quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2,}
    result = price_info.total_cost_shopping(test_price_list,test_quantity_list)
    assert (result == 25.9)

def test_cost_of_fruits():
    result = price_info.cost_of_fruits("orange", 20)
    assert (result == 28)