def bubble(list):
    litem = len(list)-1                                  #Получем количество элементов в списке
    for z in range(0, litem):                            #Создаем цикл для проверки элементов
        for x in range(0, litem):                        #Проверяем каждый элемент
            if list[x] > list[x+1]:                      #Проверяем если след число больше предыдущего
                list[x], list[x+1] = list[x+1], list[x]  #То меняем их местами
                

    return list                                          #Возвращаем отсортированный список



list1 = [1, 4, 90, -12, 0, 143]

print(bubble(list1))
