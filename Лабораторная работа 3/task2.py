# TODO Напишите функцию find_common_participants


def find_common_participants(s1,s2,rasd = ","):
    s1 = s1.split(rasd)
    s2 = s2.split(rasd)
    result = list(set(s1).intersection(set(s2)))
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group,rasd = "|"))