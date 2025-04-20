import flet as ft

def main(page: ft.Page):
    friends = []  

    first_name_input = ft.TextField(label="Имя друга")
    last_name_or_age_input = ft.TextField(label="Фамилия/Возраст")

    def add_friend(e):
        first_name = first_name_input.value.strip()
        last_name_or_age = last_name_or_age_input.value.strip()

        if first_name:
            new_friend = {"имя": first_name, "дополнительно": last_name_or_age}
            friends.append(new_friend)
            print(f"Добавлен друг: {new_friend}")
            first_name_input.value = ""
            last_name_or_age_input.value = ""
            page.update()

    add_button = ft.ElevatedButton(text="Добавить друга", on_click=add_friend)

    page.add(
        first_name_input,
        last_name_or_age_input,
        add_button
    )

if __name__ == "__main__":
    ft.app(target=main)