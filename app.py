import flet as ft
import pymssql

conn=pymssql.connect(server='M1503QA', user=None, password=None,autocommit=True, database='port')
cursor = conn.cursor()
class cargo():    
    def __init__(self,list,main):
        self.main=main
        self.list=list
    def main(page: ft.Page):
        def btn(e):
            if not un.value or not psw.value:
                page.dialog=d
                d.open=True
                page.update()
            else:
                cursor.execute("SELECT login, password FROM users WHERE login=%s AND password=%d",(un.value,psw.value))
                row=cursor.fetchone()
                if row:
                    if row[0]==un.value and row[1]==psw.value:
                        list()
                    conn.close()
                else:
                    page.dialog=b
                    b.open=True
                    page.update()


        page.title = "Информационная система"
        page.bgcolor="blue"
        d=ft.AlertDialog(title=ft.Text("Пожалуйста введите логин или пароль",color="white"), bgcolor="pink")
        b=ft.AlertDialog(title=ft.Text("Неверный логин или пароль",color="white"), bgcolor="pink")
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

        def list(page: ft.Page):
            page.title="main"
            page.bgcolor='blue'
            page.window_height=600
            page.window_width=800
            lv = ft.ListView(expand=True, spacing=3)
            cursor.execute("SELECT * FROM ORDERS")
            for row in cursor:
                lv.controls.append(ft.Container(ft.Text(f"{row[4]}, {row[2]}"),border=ft.border.all(2,'black')))
            page.add(ft.Row(controls=[ft.TextField(label="Вес"),ft.TextField(label="Страна происхождения")]),
                     ft.Row(controls=[ft.TextField(label="Дата", input_filter=ft.InputFilter(allow=True, regex_string=r"", replacement_string="")),ft.ElevatedButton(text="Добавить в базу",on_click=add_car)]),
                     ft.Container(content=lv,width=550,height=500,border=ft.border.all(3,'yellow'),border_radius=8))
            conn.close()
            page.update()
        
    
            def add_car(page: ft.Page,e):
                c=ft.AlertDialog(title=ft.Text("Данные добавлены",color="white"), bgcolor="pink")
                page.dialog=c
                c.open=True
                page.update()


ft.app(target=cargo.main)
