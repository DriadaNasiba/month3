from expense_db import ExpenseDatabase

def main():
    db = ExpenseDatabase()

    while True:
        print("\n=== Меню расходов ===")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Общая сумма расходов")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            desc = input("Описание: ")
            try:
                amount = float(input("Сумма: "))
                db.add_expense(desc, amount)
                print("✅ Расход добавлен.")
            except ValueError:
                print("❌ Ошибка: сумма должна быть числом.")
        elif choice == "2":
            expenses = db.get_all_expenses()
            if expenses:
                print("\nID | Описание | Сумма | Дата")
                for e in expenses:
                    print(f"{e[0]} | {e[1]} | {e[2]} | {e[3]}")
            else:
                print("Нет данных.")
        elif choice == "3":
            total = db.get_total_expenses()
            print(f"💰 Общая сумма расходов: {total}")
        elif choice == "4":
            db.close()
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
