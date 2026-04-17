import flet as ft

def vista_notificaciones():
    return ft.Column([
        ft.Row(
            controls=[
                ft.Icon("notifications_active", size=28, color="#B71C1C"),
                ft.Text("NOTIFICACIONES", size=20, weight="bold")
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Container(height=20),
        ft.Column(
            spacing=12,
            controls=[
                ft.Container(
                    padding=15, bgcolor="#FFF9E6", border_radius=12,
                    border=ft.Border.all(2, "#FFB74D"),
                    content=ft.Row([
                        ft.Icon("info", size=24, color="#FF6F00"),
                        ft.Column([
                            ft.Text("Recordatorio", size=13, weight="bold", color="#FF6F00"),
                            ft.Text("Próximo partido vs Dinamo el 19/04 a las 11:45", size=13)
                        ], spacing=2)
                    ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START)
                ),
                ft.Container(
                    padding=15, bgcolor="#E8F5E9", border_radius=12,
                    border=ft.Border.all(2, "#66BB6A"),
                    content=ft.Row([
                        ft.Icon("celebration", size=24, color="#2E7D32"),
                        ft.Column([
                            ft.Text("¡Bien hecho!", size=13, weight="bold", color="#2E7D32"),
                            ft.Text("Excelente performance en el último partido", size=13)
                        ], spacing=2)
                    ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START)
                ),
                ft.Container(
                    padding=15, bgcolor="#FFEBEE", border_radius=12,
                    border=ft.Border.all(2, "#EF5350"),
                    content=ft.Row([
                        ft.Icon("warning", size=24, color="#C62828"),
                        ft.Column([
                            ft.Text("Importante", size=13, weight="bold", color="#C62828"),
                            ft.Text("Llevar camiseta alternativa blanca para el próximo partido", size=13)
                        ], spacing=2)
                    ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START)
                )
            ]
        )
    ], expand=True, scroll="always")