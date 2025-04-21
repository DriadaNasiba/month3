import flet as ft

def main(page: ft.Page):
    expenses = []
    expenses_list_view = ft.Column(scroll=ft.ScrollMode.ALWAYS)  
    total_amount = ft.Text(value="Общая сумма: 0", weight=ft.FontWeight.BOLD)

    expense_name_input = ft.TextField(label="Название расхода", expand=True)  
    expense_amount_input = ft.TextField(label="Сумма расхода", width=150)  
    save_button = ft.ElevatedButton(text="Добавить", on_click=add_expense)

    input_row = ft.Row(controls=[expense_name_input, expense_amount_input, save_button])

    def update_expenses_list():
        expenses_list_view.controls.clear()
        for expense in expenses:
            expense_row = ft.Row(
                controls=[
                    ft.Text(expense['название'], expand=True),  
                    ft.Text(f"{expense['сумма']} сом", color=ft.colors.BLUE, width=100, text_align=ft.TextAlign.RIGHT),  # Сумма справа и синим цветом
                    ft.IconButton(ft.icons.EDIT),
                    ft.IconButton(ft.icons.DELETE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            expenses_list_view.controls.append(expense_row)
        page.update()

    def update_total_amount():
        total = sum(exp['сумма'] for exp in expenses)
        total_amount.value = f"Общая сумма: {total} сом"
        page.update()

    def add_expense(e):
        name = expense_name_input.value.strip()
        amount_str = expense_amount_input.value.strip()

        if name and amount_str.isdigit():
            amount = int(amount_str)
            expense = {"название": name, "сумма": amount}
            expenses.append(expense)

            update_expenses_list()
            update_total_amount()

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

    page.add(
        input_row,
        ft.Divider(),
        ft.Text("Список расходов:", weight=ft.FontWeight.BOLD),
        expenses_list_view,
        ft.Divider(),
        total_amount,
    )

if __name__ == "__main__":
    ft.app(target=main)