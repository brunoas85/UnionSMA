import flet as ft

def main(page: ft.Page):
    page.title = "Unión Senior SMA"
    page.scroll = "always"
    page.window_width = 450
    page.window_height = 800
    page.window_resizable = True
    page.bgcolor = "white"
    page.padding = 10
    page.assets_dir = "assets"

    plantel = [
        {"nombre": "Silva, Facundo Lujan", "posicion": "Delantero", "goles": 5, "amarillas": 1},
        {"nombre": "Navarro, Cesar Andres", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Figueroa, Pablo Martin", "posicion": "Defensor", "goles": 1, "amarillas": 2},
        {"nombre": "Figueroa, Nicolas Matias", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Durbhan, Sergio Sebastian", "posicion": "Defensor", "goles": 0, "amarillas": 1},
        {"nombre": "Castro, Fernando Ezequiel", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Soto, Pedro Dario", "posicion": "Defensor", "goles": 0, "amarillas": 0},
        {"nombre": "Corso, Luis Andres", "posicion": "Defensor", "goles": 0, "amarillas": 0},
        {"nombre": "Figueroa, Cristian Leonardo", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Egea, Rodrigo Ariel", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Soto, Adrian Ezequiel", "posicion": "Defensor", "goles": 0, "amarillas": 0},
        {"nombre": "Barria, Jonatan David", "posicion": "Delantero", "goles": 0, "amarillas": 0},
        {"nombre": "Jara Neira, Carlos", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Figueroa, Jorge Luis", "posicion": "Defensor", "goles": 0, "amarillas": 0},
        {"nombre": "Salazar, Bruno", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Flores, Maximiliano Ricardo", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Villegas, Cesar Oscar", "posicion": "Defensor", "goles": 0, "amarillas": 0},
        {"nombre": "Vilchez, Jorge Luis", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Flores, Facundo Emilio", "posicion": "Director Técnico", "goles": 0, "amarillas": 0},
        {"nombre": "Di Sciascio, Darien Emanuel", "posicion": "Mediocampista", "goles": 0, "amarillas": 0},
        {"nombre": "Oliva, Horacio Sebastian", "posicion": "Arquero", "goles": 0, "amarillas": 0}
    ]

    # --- VISTA: FECHA ---
    def vista_partidos():
        return ft.Column(
            scroll="always",
            expand=True,
            horizontal_alignment="center", # Usamos texto entre comillas, no ft.alignment
            controls=[
                # La card de Próxima Fecha ha sido removida

                # --- BOTÓN DIRECTO AL PLANTEL ---
                ft.Container(height=30),
                ft.FilledButton(
                    "Plantel y Perfiles",
                    icon="groups",
                    style=ft.ButtonStyle(
                        bgcolor="#1E88E5", 
                        color="white", 
                        padding=20,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    on_click=lambda _: ir_a_plantel()
                ),

                # --- SECCIÓN DE TABLA Y NOTICIAS ---
                ft.Container(height=30),
                ft.Text("TABLA Y NOTICIAS", size=18, weight="bold"),
                ft.Row(
                    scroll="auto",
                    wrap=True,
                    spacing=15,
                    run_spacing=15,
                    controls=[
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=260,
                            content=ft.Text("Posición en torneo: 3ro. Próximo rival directo.", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=260,
                            content=ft.Text("Goleador del equipo: Silva, Facundo con 5 goles.", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=260,
                            content=ft.Text("Llevar camiseta alternativa (blanca) por si acaso.", size=14)
                        ),
                    ]
                ),
                ft.Container(height=50) 
            ]
        )

    # --- VISTA: PLANTEL ---
    def vista_plantel():
        lista = ft.ListView(expand=True, spacing=10, padding=20)
        for jugador in plantel:
            stats = ft.Container(
                width=100, # Esto evita que aplaste al texto de la izquierda
                content=ft.Row(
                    spacing=3,
                    controls=[
                        ft.Icon("sports_soccer", size=16, color="black"),
                        ft.Text(str(jugador["goles"]) + "  ", size=14, weight="bold"),
                        ft.Icon("square", size=16, color="#FDD835"),
                        ft.Text(str(jugador["amarillas"]), size=14, weight="bold"),
                    ]
                )
            )
            
            lista.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.CircleAvatar(content=ft.Icon("person")), 
                        title=ft.Text(jugador["nombre"], weight="bold"),
                        subtitle=ft.Text(jugador["posicion"], color="grey"),
                        trailing=stats
                    ),
                    bgcolor="white", border_radius=10
                )
            )
        cabecera = ft.Row(
            controls=[
                ft.FilledButton(
                    "",
                    icon="home",
                    icon_color="black",
                    bgcolor="#E0E0E0",
                    width=44,
                    height=44,
                    on_click=lambda _: volver_a_inicio()
                ),
                ft.Text("PLANTEL Y PERFILES", size=22, weight="bold")
            ],
            alignment="start",
            vertical_alignment="center",
            spacing=10
        )
        return ft.Column([
            ft.Container(padding=15, content=cabecera),
            lista
        ], expand=True)

    contenedor_principal = ft.Container(content=vista_partidos(), expand=True)

    def cambio_tab(e):
        idx = e.control.selected_index
        contenedor_principal.content = vista_partidos() if idx == 0 else vista_plantel()
        page.update()

    def ir_a_plantel():
        page.navigation_bar.selected_index = 1
        contenedor_principal.content = vista_plantel()
        page.update()

    def volver_a_inicio():
        page.navigation_bar.selected_index = 0
        contenedor_principal.content = vista_partidos()
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="calendar_month", label="Fecha"),
            ft.NavigationBarDestination(icon="groups", label="Equipo"),
        ],
        on_change=cambio_tab,
    )

    page.appbar = ft.AppBar(
        title=ft.Row(
            controls=[
                ft.Text("UNIÓN", weight="bold", color="white", size=40),
                ft.Image(src="UnionEscudo.png", height=150, fit="contain"),
                ft.Text("San Martín\nde los Andes", color="white", size=18, weight="bold", text_align="center")
            ],
            alignment="center",
            vertical_alignment="center",
            spacing=10,
            wrap=True
        ),
        center_title=True,
        toolbar_height=120,
        bgcolor="red",
    )

    page.add(contenedor_principal)

if __name__ == "__main__":
    ft.run(main)