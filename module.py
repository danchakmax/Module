import pandas as pd
import matplotlib.pyplot as plt


class  Clients:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Імя клієнта","Номер замовлення","Дата замовлення","Сума замовлення","Статус"])


    def load_from_csv_file(self, filename):
        try:

            self.df = pd.read_csv(filename)

            if not all(self.df.columns == ["Імя клієнта", "Номер замовлення", "Дата замовлення", "Сума замовлення", 'Статус']):
                raise ValueError('Wrong format CSV-File')
            print("Data loaded successfully")
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_csv_file(self, filename):
        try:
            self.df.to_csv(filename, index=False)
            print("Data saved successfully")
        except Exception as e:
            print(f"Error saving file: {e}")


    def add_order(self, name, number, date, price, status):
        if name in self.df["Імя клієнта"].values:
            raise ValueError("Order is already exists")
        new_student=pd.DataFrame([[name, number, date, price, status]], columns=self.df.columns)
        self.df = pd.concat([self.df, new_student], ignore_index=True)


    def change_order(self,name, number, date, price, status):
        if name not in self.df["Імя клієнта"].values:
            raise ValueError("We can't find this student")
        self.df.loc[self.df["Імя клієнта"] == name, ["Номер замовлення", "Дата замовлення", "Сума замовлення", 'Статус']] = [name, number, date, price, status]

    def delete_order(self, name):
        if name not in self.df["Імя клієнта"].values:
            raise ValueError("Order not found")
        self.df = self.df[self.df["Імя клієнта"] != name]

    def get_all_order(self):
        return self.df


    def all_order_and_total_sum(self):
        total = self.df["Сума замовлення"].sum()
        all_order = len(self.df)
        return total, all_order


    def max_sum_order(self):
        max_sum = self.df.loc[self.df["Сума замовлення"].idxmax()]
        return max_sum


    def diagram(self):
        category_counts = self.df["Статус"].value_counts()
        plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        plt.title("Частки виконаних і невиконаних замовлень")
        plt.show()


    def histogram(self):
        plt.hist(self.df["Дата замовлення"], bins=10, edgecolor='black')
        plt.xlabel("Дата замовлення")
        plt.ylabel("Кількість замовлень")
        plt.title("Гістограма дат замовлень")
        plt.show()




def Console_menu():

    main = Clients()

    def print_menu():
        print('Menu')
        print('1. Завантажити дані з CSV')
        print('2. Зберегти дані в  CSV')
        print('3. Показати всі замовлення')
        print('4. Додати нове замовлення')
        print('5.Видалити замовлення')
        print('6. Редагувати інформацію про замовлення')
        print("7. Виведення усіх замовлень")
        print('8. Підрахунок загальної кількості замовлень і їх сумарної вартості.')
        print('9. Аналіз замовлень за статусом (виконано/в процесі).')
        print('10. Пошук замовлення з найбільшою сумою.')
        print('11. Побудова кругової діаграми частки виконаних і невиконаних замовлень.')
        print('12. Побудова гістограми кількості замовлень за датами.')
        print('0. Вихід')



    while True:
        print_menu()
        choice = input('Виберіть опцію:')

        try:
            if choice == '1':
                filename = input("Enter CSV-file name: ")
                main.load_from_csv_file(filename)
                print("Successful load")

            elif choice == '2':
                filename = input("Enter CSV-file name: ")
                main.save_to_csv_file(filename)
                print("Successful saving")
            elif choice == '3':
                clients = main.get_all_order()
                if not clients.empty:
                    print("Students: ")
                    print(clients)
                else:
                    print("No students available")

            elif choice=='4':
                name = input("Ім'я клієнта:")
                num = input('Номер замовлення: ')
                date = input("Дата замовлення: ")
                sum = float(input('Сума замовлення: '))
                status = input('Статус: ')

            elif choice == '5':
                name = input("Name to delete: ")
                main.delete_order(name)

            elif choice == '6':
                name = input("Ім'я щоб змінити інформацію: ")
                num = input('Номер замовлення: ')
                date = input("Дата замовлення: ")
                sum = float(input('Сума замовлення: '))
                status = input('Статус: ')
                main.change_order(name,num,date,sum,status)

            elif choice == '7':
                print(main.get_all_order())

            elif choice =='8':

                total, all_order = main.all_order_and_total_sum()
                print(f"Загальна кількість замовлень: {all_order}, Загальна сума: {total}")

            elif choice == '9':
                category_counts = main.df["Статус"].value_counts()
                print(f"Аналіз замовлень за статусом:\n{category_counts}")

            elif choice == '10':
                max_order = main.max_sum_order()
                print(f"Замовлення з найбільшою сумою: {max_order}")

            elif choice=='11':
                main.diagram()

            elif choice == '12':
                main.histogram()

            elif choice == '0':
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    Console_menu()























