# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group,participants_second_group,c=","):
    #Создаем список с участниками двух групп
    participants_first_group_split = participants_first_group.split(c)
    participants_second_group_split = participants_second_group.split(c)
    sum_participants = participants_second_group_split + participants_first_group_split
    #Находим общих участников
    first_set = set(sum_participants[:2])
    second_set = set(sum_participants[3:])
    global_participants_set = first_set.intersection(second_set)
    # Сортируем по алфавиту
    global_participants_list = list(global_participants_set)
    global_participants_list.sort()
   #Возвращаем отсортированный список
    return global_participants_list

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

global_participants_list = find_common_participants(participants_first_group,participants_second_group,"|")
print(global_participants_list)

