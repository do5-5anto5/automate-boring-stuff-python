import time

def calculate_product():
    product = 1
    for i in range(1, 100_001):
        product = product * 1
    return product

start_time= time.time()
calculate_product()
end_time = time.time()

print(f'It took {end_time - start_time} seconds to calculate product')