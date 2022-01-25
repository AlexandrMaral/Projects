"""
Задание 1.
Для каждой из трех функций выполнить следующее:
1) для каждого выражения вместо !!! укажите сложность.
2) определите сложность алгоритма в целом (Сложность: !!!).
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- Сложность нужно указать только там, где есть !!!
-- Сложности встроенных функций нужно искать
    в таблицах (материалы к уроку).
"""

import random


##############################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 1:
    Создать множество из списка
    Сложность: O(n)
    """
    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set  # O(1)


##############################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(n)
    """
    for j in range(len(lst_obj)):          # O(1)
        if lst_obj[j] in lst_obj[j+1:]:    # O(n)
            return False                   # O(1)
    return True                            # O(1)


##############################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(n log n)
    """
    lst_copy = list(lst_obj)                 # O(n)
    lst_copy.sort()                          # O(n log n)
    for i in range(len(lst_obj) - 1):        # O(n)
        if lst_copy[i] == lst_copy[i+1]:     # O(n)
            return False                     # O(1)
    return True                              # O(1)


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))

"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

# Сложность O(n ^ 2)
def get_min_number_2(lst):
    min_number_2 = lst[0]                                   # O(1)
    for i in lst:                                           # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_number_2 > lst[j]:                       # O(n ^ 2)
                min_number_2 = lst[j]                       # O(1)
    return min_number_2                                     # O(1)

# сложность O(n)

def get_min_number(lst):
    min_number = lst[0]                                     # O(1)
    for i in lst:                                           # O(n)
        if i < min_number:                                  # O(n)
            min_number = i                                  # O(1)
    return min_number                                       # O(1)



first_list = [2, 13, 4, 156, 222, 1]

print(get_min_number(first_list))

print(get_min_number_2(first_list))

"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""

class StackClass:
    def __init__(self):
        self.elems = [[],[],[],[],[]]

    def push_in(self, el):
        for i in range(0, len(self.elems) - 1, 1):
            if len(self.elems[i]) < 5:
                self.elems[i].append(el)
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

if __name__ == '__main__':
    stack_1 = StackClass()
    i = 0
    while i < 18:
        stack_1.push_in(1+i)
        i += 1

    print(stack_1.elems)

"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class QueueClass:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []


    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_from_revision_to_base(self):
        self.base.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    qc_obj = QueueClass()

    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.base)
    qc_obj.to_solved()
    print(qc_obj.solved)
    qc_obj.to_revision()
    print(qc_obj.base)
    print(qc_obj.revision)
    qc_obj.return_from_revision_to_base()
    print(qc_obj.revision)
    print(qc_obj.base)
