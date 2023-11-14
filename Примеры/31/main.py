# Импорт пакета целиком и импорт отдельных определений
import my_package.average_module
from my_package.median_module import median

lst = [2, 3, 5, 20]
result_1 = my_package.average_module.avg(lst)
result_2 = median(lst)
print(result_1)  # 7.5
print(result_2)  # 4.0
