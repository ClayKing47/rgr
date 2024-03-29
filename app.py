import flet as ft

def main(page: ft.Page):
    def btn(e):
        if not un.value or not psw.value:
            page.dialog=d
            d.open=True
            page.update()
        else:
            page.clean()
            page.add(ft.Text(f"Hello, {un.value}, {psw.value}!"))


    
    page.title = "Информационная система"
    page.bgcolor="blue"
    d=ft.AlertDialog(title=ft.Text("Пожалуйста введите логин или пароль",color="white"), bgcolor="pink")
   
    un=ft.TextField(
        label="Введите имя пользователя",
        hint_text="Логин",
        border_color="black",
        border_width=5,
        border_radius=50,
        width=300)
    psw=ft.TextField(
        label="Введите пароль",
        hint_text="Пароль",
        border_color="black",
        border_width=5,
        border_radius=50,
        width=200,
        password=True,
        can_reveal_password=True)
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    btn=ft.ElevatedButton(text="Войти", on_click=btn, icon=ft.icons.ANCHOR_OUTLINED)
    page.add(ft.Container(
        ft.Stack([
            ft.Container(content=un,top=20),
            ft.Container(content=psw,top=80),
            ft.Container(content=btn,top=140,left=175),],)
            ,width=450,height=200,bgcolor="white",border_radius=10))
    


ft.app(target=main)