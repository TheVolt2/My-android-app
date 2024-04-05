import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Класс для представления пиццы
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Класс для представления напитка
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Класс для представления заказа
class Order:
    def __init__(self):
        self.selected_pizza = None
        self.selected_beverage = None

    def select_pizza(self, pizza):
        self.selected_pizza = pizza

    def select_beverage(self, beverage):
        self.selected_beverage = beverage

    def get_total_price(self):
        total_price = 0
        if self.selected_pizza:
            total_price += self.selected_pizza.price
        if self.selected_beverage:
            total_price += self.selected_beverage.price
        return total_price

# Класс для интерфейса приложения
class PizzaOrderApp(App):
    def build(self):
        # Создаем экземпляр заказа
        self.order = Order()

        # Создаем главный макет
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопки для выбора пиццы
        pizza_btn1 = Button(text='Пепперони - 800 руб.')
        pizza_btn1.bind(on_press=lambda instance: self.order.select_pizza(Pizza("Пепперони", 800)))
        layout.add_widget(pizza_btn1)

        pizza_btn2 = Button(text='Маргарита - 750 руб.')
        pizza_btn2.bind(on_press=lambda instance: self.order.select_pizza(Pizza("Маргарита", 750)))
        layout.add_widget(pizza_btn2)

        pizza_btn3 = Button(text='Гавайская - 900 руб.')
        pizza_btn3.bind(on_press=lambda instance: self.order.select_pizza(Pizza("Гавайская", 900)))
        layout.add_widget(pizza_btn3)

        # Создаем кнопки для выбора напитка
        beverage_btn1 = Button(text='Кола - 150 руб.')
        beverage_btn1.bind(on_press=lambda instance: self.order.select_beverage(Beverage("Кола", 150)))
        layout.add_widget(beverage_btn1)

        beverage_btn2 = Button(text='Фанта - 150 руб.')
        beverage_btn2.bind(on_press=lambda instance: self.order.select_beverage(Beverage("Фанта", 150)))
        layout.add_widget(beverage_btn2)

        beverage_btn3 = Button(text='Сок - 200 руб.')
        beverage_btn3.bind(on_press=lambda instance: self.order.select_beverage(Beverage("Сок", 200)))
        layout.add_widget(beverage_btn3)

        # Кнопка для оформления заказа
        confirm_btn = Button(text='Оформить заказ')
        confirm_btn.bind(on_press=self.display_order)
        layout.add_widget(confirm_btn)

        return layout

    # Метод для отображения заказа
    def display_order(self, instance):
        total_price = self.order.get_total_price()
        order_summary = "Заказ:\n"
        if self.order.selected_pizza:
            order_summary += f"Пицца: {self.order.selected_pizza.name} - {self.order.selected_pizza.price} руб.\n"
        if self.order.selected_beverage:
            order_summary += f"Напиток: {self.order.selected_beverage.name} - {self.order.selected_beverage.price} руб.\n"
        order_summary += f"Общая стоимость заказа: {total_price} руб."

        # Очистка и добавление элементов на экран
        self.root.clear_widgets()
        self.root.add_widget(Label(text=order_summary))

# Создание экземпляра приложения
if __name__ == '__main__':
    PizzaOrderApp().run()
