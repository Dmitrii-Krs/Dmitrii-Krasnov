class Door:
    """
    Класс Door  позволяет создать экземпляр "дверь" и задать ему определенные параметры
    """

    def __init__(self, naming: str, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Дверь"
        :param naming: Название двери
        :param width: Ширина двери
        :param height: Высота двери

        Пример:
        >>> door = Door("Входная дверь", 750, 2100)
        """
        self.width = width
        self.height = height
        self.naming = naming

    def material(self, material: str) -> str:
        """
        Метод material позволяет задать экземпляру "дверь" материал
        :param material: Материал двери
        :return: Строка

        Пример
        >>> door = Door("входная", 750, 2100)
        >>> door.material("металл")
        'Дверь входная. Ширина: 750, высота: 2100. Материал: металл'
        """
        self.material = material
        return f"Дверь {self.naming}. Ширина: {self.width}, высота: {self.height}. Материал: {self.material}"

    def handle(self, presence: bool) -> str:
        """
        Метод handle позволяет задать экземпляру "дверь" налчие или отсутствие ручки
        :param presence: Наличие ручки
        :return: Строка
        >>> door = Door("входная", 750, 2100)
        >>> door.handle(True)
        'Дверь с ручкой входная. Ширина: 750, высота: 2100.'
        """
        self.presence = presence
        if presence == True:
            return f"Дверь с ручкой {self.naming}. Ширина: {self.width}, высота: {self.height}."
        else:
            return f"Дверь без ручки {self.naming}. Ширина: {self.width}, высота: {self.height}."

    def __str__(self) -> str:
        """
        Магический метод __str__
        :return: Строка

        Пример
        >>> door = Door("Входная", 750, 2100)
        >>> str(door)
        'Дверь Входная. Ширина: 750, высота: 2100.'
        """
        return f"Дверь {self.naming}. Ширина: {self.width}, высота: {self.height}."

    def __repr__(self) -> str:
        """
        Магический
        метод __repr__
        :return: Строка

        Пример
        >>> door = Door("входная", 750, 2100)
        >>> repr(door)
        "Door(naming = 'входная', width = 750, height = 2100)"
        """
        return f"{self.__class__.__name__}(naming = {self.naming!r}, width = {self.width!r}, height = {self.height!r})"

class SwingDoor(Door):
    """
    Подкласс SwingDoor позволяет создать экземпляр "распашная дверь" и задать ему определенные параметры
    """

    def __init__(self, opening_type: str, naming: str, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Распашная дверь"
        Перегружается метод __init__ родительского класса с добавлением аргумета
        :param opening_type: Тип открывания

        Пример:
        >>> door = SwingDoor("правая","входная", 750, 2100)
        """
        super().__init__(naming, width, height)
        self._opening_type = opening_type # Необходима проврека поля на корректность

    def __str__(self) -> str:
        """
        Перезагрузка магического метода __str__
        :return:

        Пример
        >>> door = SwingDoor("правая","входная", 750, 2100)
        >>> str(door)
        'Дверь правая входная. Ширина: 750, высота: 2100.'
        """
        return f"Дверь {self._opening_type} {self.naming}. Ширина: {self.width}, высота: {self.height}."

    def __repr__(self) -> str:
        """
        Перезагрузка магического метода __repr__
        :return: Строка

        Пример
        >>> door = SwingDoor("правая","входная", 750, 2100)
        >>> repr(door)
        "SwingDoor(opening_type = правая, naming = 'входная', width = 750, height = 2100)"
        """
        return f"{self.__class__.__name__}(opening_type = {self._opening_type}, naming = {self._naming!r}, width = {self._width!r}, height = {self._height!r})"

    def handle(self, handle_type: str) -> str:
        """
        Перезагрузка метода handle.
        Метод перезагружен, так как объект "распашная дверь" должен иметь ручку.
        Метод позволяет задать ее тип
        :param handle_type: Тип ручки
        :return: Строка

        Пример
       >>> door = SwingDoor("правая","входная", 750, 2100)
       >>> door.handle("Ручка-скоба")
       'Дверь правая с Ручка-скоба ручкой входная. Ширина: 750, высота: 2100.'
        """
        self.handle_type = handle_type
        return f"Дверь {self._opening_type} с {self.handle_type} ручкой {self._naming}. Ширина: {self._width}, высота: {self._height}."

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass

