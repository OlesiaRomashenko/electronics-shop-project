import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, prod_name):
        if len(prod_name) > 10:
            self.__name = prod_name[:10]
        else:
            self.__name = prod_name

    @classmethod
    def instantiate_from_csv(cls, file_name):
        with open(file_name) as f:
            reader = csv.DictReader(f)
            Item.all = []
            for row in reader:
                __name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(__name, price, quantity)

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.all_price = self.price * self.quantity
        return self.all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
