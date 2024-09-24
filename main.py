import flet as ft


def main(page: ft.Page):
    page.title = "Hello World App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter = ft.Ref[ft.Text]()
    count = 0

    def on_button_click(e):
        nonlocal count
        count += 1
        counter.current.value = f"Counter: {count}"
        counter.current.update()

    hello_text = ft.Text(value="Hello, World!", size=40)
    counter_text = ft.Text(ref=counter, value=f"Counter: {count}", size=30)
    increment_button = ft.ElevatedButton(text="Increment", on_click=on_button_click)

    page.add(hello_text, counter_text, increment_button)


ft.app(target=main)
