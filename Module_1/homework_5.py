immutable_var = (1, "2", True)
print("Неизменяемый кортеж: " + str(immutable_var))
#immutable_var[0] Не даст изменить, так как типы int и string не изменяемые,
#но если я добавлю список, то смогу изменить значения списка, так как это
#изменяемый тип
mutable_list = [5, "6", False]
print("Список: " + str(mutable_list))
mutable_list[0] = 10
print("Измененый список: " + str(mutable_list))