import sys
from storage import *

def zad_menu():
    print('''Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Выход
''')

    
def zad_spisok():
    r = find_all(conn)
    print('Список всех задач\n' + str(r))

def zad_insert():
    task_name = input('Введите имя задачи: ')
    task_text = input('Введите вышу задачу: ')
    task_status = input('Введите статус')
    add_task(conn, task_name, task_text, task_status)
    print('Добалено')


def zad_edit():
    id = input('Введите номер задачи, которую хотите отредактировать')
    if not id.isdigit():
        print('Введите число')
    task_name = input('Введите имя задачи: ')
    task_text = input('Введите вышу задачу: ')
    task_status = input('Введите статус')
    redact_task(conn, id, task_name, task_text, task_status)
        
        
def zad_close():
    print('завершить задачу')
    id = input('введите номер задачи')
    if not id.isdigit():
        print('id должен быть числом')
    close_task(conn, id)

def zad_exit():
    sys.exit(0)


def main():
    

    zad_menu()

    actions = {
        '1': zad_spisok,
        '2': zad_insert,
        '3': zad_edit,
        '4': zad_menu,
        '5': zad_exit
    }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда!')

main()

    
        

    
    



