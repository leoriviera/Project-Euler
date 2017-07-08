# Solved correctly
n = 1

while True:
    multiples_array, sorted_products = [], []
    answer = False
    
    for i in range(1, 7):
        multiples_array.append(n * i)
    
    for each_index in range(0, len(multiples_array)):
        split_product_list = list(str(multiples_array[each_index]))
        split_product_list.sort()
        
        sorted_products.append(''.join(split_product_list))

    for sorted_multiples_index in range(0, 5):
        if sorted_products[sorted_multiples_index] == sorted_products[sorted_multiples_index + 1]:
            answer = True
        else:
            answer = False
            break
        
    if answer:
        break
    else:
        n += 1

print(n)
