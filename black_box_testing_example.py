# black_box_testing_example.py
from black_box_testing import add

result = add(3, 5)
print(result)  # 8

result = add(-3, -5)
print(result)  # -8

result = add(2, -5)
print(result)  # -3
