import pandas as pd
import numpy as np


log_data = './Log_data.xlsx'
data_c1 = './Data_C1.xls'

# Данные принятого металла из бумажного журнала
log_data_acc = pd.read_excel(log_data, sheet_name="Accepted", usecols="A,C,D",
                             dtype={"D": np.float64, "A": np.datetime64}, skiprows=0, nrows=2260)
# Данные сданного металла из бумажного журнала
log_data_pas = pd.read_excel(log_data, sheet_name="Passed", usecols="A,C,D",
                             dtype={"D": np.float64, "A": np.datetime64}, skiprows=0, nrows=2305)

# Данные принятого металла из 1С
data_c1_acc = pd.read_excel(data_c1, usecols="B,K,L", dtype={"L": np.float64}, skiprows=9, nrows=3935)

# Данные сданного металла из 1С
data_c1_pas = pd.read_excel(data_c1, usecols="B,K,M", dtype={"M": np.float64}, skiprows=9, nrows=3935)


# Удаляем пустые строки
sort_acc = data_c1_acc[data_c1_acc['Вес приход'] > 0]
sort_pas = data_c1_pas[data_c1_pas['Вес расход'] > 0]

# awdawd=data_c1_pas[data_c1_pas['Вес расход'] == 188.63]
# print(awdawd.values[0][0])

dict_log_acc = {}
dict_log_pas = {}
id_acc = 0
id_pas = 0

for i in log_data_acc["Вес"]:
    if type(i) == float:
        if i > 0:
            dict_log_acc[id_acc] = i
    id_acc += 1

for i in log_data_pas["Вес"]:
    if type(i) == float:
        if i > 0:
            dict_log_pas[id_pas] = i
    id_pas += 1


def search_for_value_log(dict_, value):
    a = 0
    for k, v in dict_.items():
        if v == value:
            a = f"Сошлось!" \
                f"В бумажном журнале Строка №{k}, Вес - {v} грамм"
    if a != 0:
        return a
    if a == 0:
        return f"НЕСОШЛОСЬ!" \
               f"В бумажном журнале Вес {value} не найден"

def get_1c_acc(wight_c1: float):
    data_acc = data_c1_acc[data_c1_acc['Вес приход'] == wight_c1]
    return data_acc.values

def get_1c_pass(wight_c1: float):
    data_pas = data_c1_pas[data_c1_pas['Вес расход'] == wight_c1]
    return data_pas.values

print("Приемка")
for i in sort_acc.values:
    print(get_1c_acc(i[2]))
    print((search_for_value_log(dict_log_acc, i[2])))
    print("__________________")

print("Сдача")
for i in sort_pas.values:
    print(get_1c_pass(i[2]))
    print((search_for_value_log(dict_log_pas, i[2])))
    print("__________________")