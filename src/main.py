import flet as ft
from database import ExpenseDatabase

db = ExpenseDatabase()

def main(page: ft.Page):
    page.title = "Учёт расходов"
    page.scroll = "AUTO"

    expense_list_area = ft.Column()
    desc_field = ft.TextField(label="Описание")
    amount_field = ft.TextField(label="Сумма")
    total_label = ft.Text("Общая сумма: 0.00 сом.", weight=ft.FontWeight.BOLD)

    # === Удаление через диалог ===
    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Удалить расход?"),
        actions=[],
    )

    # === Редактирование через диалог ===
    edit_desc_field = ft.TextField(label="Новое описание")
    edit_amount_field = ft.TextField(label="Новая сумма")
    edit_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Редактировать расход"),
        content=ft.Column([edit_desc_field, edit_amount_field]),
        actions=[],
    )

    def open_delete_dialog(e):
        expense_id = e.control.data
        confirm_dialog.actions = [
            ft.TextButton("Отмена", on_click=lambda e: page.dialog.close()),
            ft.TextButton("Удалить", on_click=lambda e: confirm_delete(expense_id)),
        ]
        page.dialog = confirm_dialog
        page.dialog.open = True
        page.update()

    def confirm_delete(expense_id):
        db.delete_expense(expense_id)
        page.dialog.open = False
        refresh_expenses()
        page.update()

    def open_edit_dialog(e):
        expense = e.control.data  # (id, description, amount)
        edit_desc_field.value = expense[1]
        edit_amount_field.value = str(expense[2])
        page.dialog = edit_dialog

        def save_changes(ev):
            try:
                new_desc = edit_desc_field.value.strip()
                new_amount = float(edit_amount_field.value)
                db.update_expense(expense[0], new_desc, new_amount)
                page.dialog.open = False
                refresh_expenses()
                page.update()
            except ValueError:
                pass  # можно показать сообщение об ошибке

        edit_dialog.actions = [
            ft.TextButton("Отмена", on_click=lambda e: page.dialog.close()),
            ft.TextButton("Сохранить", on_click=save_changes),
        ]
        page.dialog.open = True
        page.update()

    def build_rows():
        rows = []
        for expense in db.get_all_expenses():
            rows.append(
                ft.Row([
                    ft.Text(expense[3]),               
                    ft.Text(expense[1]),               
                    ft.Text(f"{expense[2]:.2f} сом"),  
                    ft.IconButton(
                        icon=ft.icons.EDIT_OUTLINED,
                        icon_color=ft.colors.BLUE,
                        icon_size=20,
                        on_click=open_edit_dialog,
                        data=expense  # Передаём (id, desc, amount)
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINED,
                        icon_color=ft.colors.RED,
                        icon_size=20,
                        on_click=open_delete_dialog,
                        data=expense[0],  # ID
                    ),
                ])
            )
        return rows

    def refresh_expenses():
        expense_list_area.controls = build_rows()
        total = db.get_total_expenses()
        total_label.value = f"Общая сумма: {total:.2f} сом"

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
        except ValueError:
            pass  

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
