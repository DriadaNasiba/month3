import flet as ft
from database import ExpenseDatabase

db = ExpenseDatabase()

def main(page: ft.Page):
    page.title = "Учёт расходов"
    page.scroll = "AUTO"

    expense_list_area = ft.Column()

    
    desc_field = ft.TextField(label="Описание")
    amount_field = ft.TextField(label="Сумма")

    def add_expense(e):
        try:
            description = desc_field.value.strip()
            amount = float(amount_field.value)
            if description and amount > 0:
                db.add_expense(description, amount)
                desc_field.value = ""
                amount_field.value = ""
                refresh_expenses()
                page.update()
        except Va

    def delete_expense(e):
        expense_id = e.control.data
        db.delete_expense(expense_id)
        refresh_expenses()
        page.update()

    def build_rows():
        rows = []
        for expense in db.get_all_expenses():
            rows.append(
                ft.Row([
                    ft.Text(expense[3]),             
                    ft.Text(expense[1]),             
                    ft.Text(f"{expense[2]:.2f} руб."),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINED,
                        icon_color=ft.colors.RED,
                        icon_size=20,
                        on_click=delete_expense,
                        data=expense[0],  
                    )
                ])
            )
        return rows

    def refresh_expenses():
        expense_list_area.controls = build_rows()
        total = db.get_total_expenses()
        total_label.value = f"Общая сумма: {total:.2f} сом."

    total_label = ft.Text("Общая сумма: 0.00 сом.", weight=ft.FontWeight.BOLD)

    page.add(
        ft.Column([
            desc_field,
            amount_field,
            ft.ElevatedButton("Добавить", on_click=add_expense),
            total_label,
            expense_list_area
        ])
    )

    refresh_expenses()

ft.app(target=main)
