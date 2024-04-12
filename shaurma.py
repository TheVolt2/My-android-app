import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ShaurmaOrderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        shaurma_btn1 = Button(text='Мясная - 450 руб.', on_press=lambda instance: self.select_item("Шаурма: Мясная - 450 руб."))
        shaurma_btn2 = Button(text='Цезарь - 350 руб.', on_press=lambda instance: self.select_item("Шаурма: Цезарь - 350 руб."))
        shaurma_btn3 = Button(text='Царская - 400 руб.', on_press=lambda instance: self.select_item("Шаурма: Царская - 400 руб."))

        beverage_btn1 = Button(text='Кола - 150 руб.', on_press=lambda instance: self.select_item("Напиток: Кола - 150 руб."))
        beverage_btn2 = Button(text='Фанта - 150 руб.', on_press=lambda instance: self.select_item("Напиток: Фанта - 150 руб."))
        beverage_btn3 = Button(text='Сок - 200 руб.', on_press=lambda instance: self.select_item("Напиток: Сок - 200 руб."))

        sauce_btn1 = Button(text='Чесночный - 50 руб.', on_press=lambda instance: self.select_item("Соус: Чесночный - 50 руб."))
        sauce_btn2 = Button(text='Ткемали - 40 руб.', on_press=lambda instance: self.select_item("Соус: Ткемали - 40 руб."))
        sauce_btn3 = Button(text='Сырный - 60 руб.', on_press=lambda instance: self.select_item("Соус: Сырный - 60 руб."))

        confirm_btn = Button(text='Показать покупки и сумму', on_press=self.show_summary)

        self.items = []

        layout.add_widget(shaurma_btn1)
        layout.add_widget(shaurma_btn2)
        layout.add_widget(shaurma_btn3)
        layout.add_widget(beverage_btn1)
        layout.add_widget(beverage_btn2)
        layout.add_widget(beverage_btn3)
        layout.add_widget(sauce_btn1)
        layout.add_widget(sauce_btn2)
        layout.add_widget(sauce_btn3)
        layout.add_widget(confirm_btn)

        return layout

    def select_item(self, item):
        self.items.append(item)

    def show_summary(self, instance):
        items_summary = "\n".join(self.items)
        total_price = sum([int(item.split(" - ")[-1].split()[0]) for item in self.items])
        items_summary += f"\n\nОбщая сумма: {total_price} руб."
        self.root.clear_widgets()
        self.root.add_widget(Button(text=items_summary, on_press=self.restart))

    def restart(self, instance):
        self.items = []
        self.build()

if __name__ == '__main__':
    ShaurmaOrderApp().run()
