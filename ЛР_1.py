# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class LemonTree:
    def __init__(self, count_lemons: int, tree_color: str):
        self.count_lemons = count_lemons
        self.tree_color = tree_color
        """
        Создание и подготовка к работе объекта "Лимонное дерево"
        :param count_lemons:
        :param tree_color:

        Необходимы проверки на положительность и целосчисленость количества лимонов,
        на соотвествие цвета дерева типу "string"

        Пример:
        >>> lemon_tree = LemonTree(29, "Желтый")
        """
    def collect_lemons(self, count_collected_lemons: int) -> None:
        ...
        """
        Метод считает количество оставшихся лимонов на дереве после снятие какого-то количества.
        Необходима проверка на положительность количества собранных лимоонов,
        необходима проверка на не превышение количеством собранных лимоонов количества лимонов на дереве
        
        :param count_collected_lemons:
        Пример:
        >>> lemon_tree = LemonTree(29, "Желтый")
        >>> lemon_tree.collect_lemons(6) 
        """
    def repaint_tree(self, new_color: int)-> None:
        ...
        """
        Метод меняет цвет дерева.
        Необходима проверка на соответсвтвие нового цвета типу "string"
    
        :param new_color:
        
        Пример:
        >>> lime_tree = LemonTree(29, "Желтый")
        >>> lime_tree.repaint_tree("Зеленый")
        """
class YellowSubmarine:
    def __init__(self, count_seats: int, count_free_seats: int, passengers_list: list) :
        self.count_seats = count_seats
        self.count_free_seats = count_free_seats
        self.passengers_list = passengers_list
        """
        Создание и подготовка к работе объекта "Желтая подводная лодка"
        
        :param count_seats:
        :param count_free_seats:
        :param passengers_list:
        
        Необходимы проверки на положительность и целосчисленость количества мест и количества свободных мест
        
        Пример:
        >>> trip = YellowSubmarine(25, 21, ["Джон Леннон", "Пол Маккартни", "Джордж Харрисон", "Ринго Старр"])
        """
    def buy_tickets(self, name_passangers: list) -> None:
        ...
        """
        Метод добавляет имена новых пассжиров в список, уменьшает количество свободных мест на число пассажиров
        
        :param name_passangers:
        
        Необходима проверка на соотвествие набору имен пассажиров типу "list".
        Необходима проверка на наличие достаточного количества свободных мест.
        
        Пример:
        >>> trip = YellowSubmarine(25, 21, ["Джон Леннон", "Пол Маккартни", "Джордж Харрисон", "Ринго Старр"])
        >>> trip.buy_ticket(["Вася Пупкин", "Иван Иванович")
        """
    def anonymous_ticket(self) -> None:
        ...
        """
        Метод добавляет в список "Анонимного пассажира", уменьшает количество свободных мест на 1
    
        Пример:
        >>> trip = YellowSubmarine(25, 21, ["Джон Леннон", "Пол Маккартни", "Джордж Харрисон", "Ринго Старр"])
        >>> trip.anonymous_ticket()
        """
class Notebook:
    def __init__(self, notes_dict: dict):
        self.notes = notes_dict
        """
        Создание и подготовка к работе объекта "Блокнот"
        
        :param notes_dict:
        
        Необходима проверка на соответствие заметок типу "dict"
        
        Пример:
        >>> notebook = Notebook(notes_dict)
        """
    def new_note(self, new_notes: dict) -> None:
        ...
        """
        Метод добавления заметок в блокнот
        
        :param new_notes: 
        Необходима проверка на соответствие заметок типу "dict"
        
        Пример:
        >>> notebook = Notebook(notes_dict)
        >>> notebook.new_note({"Заметка 2" : "Вася Пупки"})
        """
    def delete_note(self, note_name) -> None:
        ...
        """
        Метод удаления заметок
        
        :param note_name:
        Необходима проверка на соответствие названия заметки типу "str"
        
        Пример:
        >>> notebook = Notebook(notes_dict)
        >>> notebook.new_note({"Заметка 2" : "Вася Пупки"})
        >>> notebook.delete_note("Заметка 2")
         
        """


if __name__ == "__main__":
    print(doctest.testmod())
    pass

