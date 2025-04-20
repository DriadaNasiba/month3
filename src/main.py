
import flet as ft

def main(page: ft.Page):
    expenses = []  
    expenses_list_view = ft.Column()  
    total_amount = ft.Text(value="Общая сумма: 0", weight=ft.FontWeight.BOLD)

    expense_name_input = ft.TextField(label="Название расхода")
    expense_amount_input = ft.TextField(label="Сумма расхода")

    def add_expense(e):
        name = expense_name_input.value.strip()
        amount_str = expense_amount_input.value.strip()

        if name and amount_str.isdigit():
            amount = int(amount_str)
            expense = {"название": name, "сумма": amount}
            expenses.append(expense)

            
            expenses_list_view.controls.append(ft.Text(f"{expense['название']}: {expense['сумма']} сом"))

           
            total = sum(exp['сумма'] for exp in expenses)
            total_amount.value = f"Общая сумма: {total} сом"

            expense_name_input.value = ""
            expense_amount_input.value = ""
            page.update()
        else:
            page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Пожалуйста, введите название расхода и корректную сумму."),
                    open=True,
                )
            )

    save_button = ft.ElevatedButton(text="Добавить расход", on_click=add_expense)

    page.add(
        expense_name_input,
        expense_amount_input,
        save_button,
        ft.Divider(),
        ft.Text("Список расходов:", weight=ft.FontWeight.BOLD),
        expenses_list_view,
        ft.Divider(),
        total_amount,
    )

if __name__ == "__main__":
    ft.app(target=main)
    