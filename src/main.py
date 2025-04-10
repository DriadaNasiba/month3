import flet as ft


def main(page: ft.Page):
    text_field = ft.TextField(label="Введите текст", autofocus=True)
    page.add(text_field)

ft.app(target=main)


import flet as ft

def main(page: ft.Page):
    friends = ["Марина", "Алексей", "Петр", "Анна", "Дмитрий"]

    
    def on_text_change(e):
        entered_text = text_field.value
        if entered_text in friends:
            print(f"Имя '{entered_text}' найдено в списке друзей!")
        else:
            print(f"Имя '{entered_text}' не найдено в списке.")


    text_field = ft.TextField(label="Введите имя", autofocus=True)
    text_field.on_change = on_text_change 


    page.add(text_field)

ft.app(target=main)


