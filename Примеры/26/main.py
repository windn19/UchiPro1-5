# Сочетание способов импорта
import my_module
from my_module import average as avg

result = avg([2, 3, 5])
print(my_module.PRECISION)
print(result)
