import flet as ft

def main(page: ft.Page):
    page.title = "Unión Senior SMA"
    page.scroll = "always"
    page.window_width = 450
    page.window_height = 800
    page.bgcolor = "white"
    page.padding = 10
    page.assets_dir = "assets"

    plantel = [
        "Silva, Facundo Lujan", "Navarro, Cesar Andres", "Figueroa, Pablo Martin",
        "Figueroa, Nicolas Matias", "Durbhan, Sergio Sebastian", "Castro, Fernando Ezequiel",
        "Soto, Pedro Dario", "Corso, Luis Andres", "Figueroa, Cristian Leonardo",
        "Egea, Rodrigo Ariel", "Soto, Adrian Ezequiel", "Barria, Jonatan David",
        "Jara Neira, Carlos", "Figueroa, Jorge Luis", "Salazar, Bruno",
        "Flores, Maximiliano Ricardo", "Villegas, Cesar Oscar", "Vilchez, Jorge Luis",
        "Flores, Facundo Emilio (DT)", "Di Sciascio, Darien Emanuel", "Oliva, Horacio Sebastian"
    ]

    # --- VISTA: FECHA ---
    def vista_partidos():
        return ft.Column(
            scroll="always",
            expand=True,
            horizontal_alignment="center",
            controls=[
                ft.Container(height=20), 
                ft.Text("PRÓXIMA FECHA", size=28, weight="bold", color="black"),
                
                # Bloque del Partido (Ancho fijo para evitar texto vertical)
                ft.Container(
                    width=380,
                    padding=20,
                    bgcolor="#f8f9fa",
                    border_radius=15,
                    border=ft.border.all(1, "#dddddd"),
                    content=ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon("sports_soccer", color="red", size=30),
                                title=ft.Text("Vs. Los Amigos FC", size=20, weight="bold", no_wrap=True),
                                subtitle=ft.Text("Sábado - 15:30hs", size=16),
                            ),
                            ft.Divider(height=1, color="#EEEEEE"),
                            ft.ListTile(
                                leading=ft.Icon("location_on", color="red", size=30),
                                title=ft.Text("Cancha Municipal", size=20, weight="bold", no_wrap=True),
                                subtitle=ft.Text("San Martín de los Andes", size=16),
                            ),
                        ]
                    )
                ),

                ft.Container(height=20),
                
                # Botones
                ft.Row(
                    alignment="center",
                    spacing=20,
                    controls=[
                        ft.ElevatedButton(
                            "MAPA", 
                            icon="map", # Solo el nombre entre comillas
                            style=ft.ButtonStyle(bgcolor="blue", color="white")
                        ),
                        ft.ElevatedButton(
                            "VOY", 
                            icon="check", # Solo el nombre entre comillas
                            style=ft.ButtonStyle(bgcolor="green", color="white")
                        ),
                    ]
                ),

                # --- SECCIÓN DE TABLA Y NOTICIAS ---
                ft.Container(height=30),
                ft.Text("TABLA Y NOTICIAS", size=18, weight="bold"),
                ft.Row(
                    scroll="auto",
                    spacing=15,
                    controls=[
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=300,
                            content=ft.Text("Posición en torneo: 3ro. Próximo rival directo.", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=300,
                            content=ft.Text("Goleador del equipo: Silva, Facundo con 5 goles.", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#F5F5F5", border_radius=10, width=300,
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
        for nombre in plantel:
            lista.controls.append(
                ft.Container(
                    content=ft.ListTile(leading=ft.Icon("person"), title=ft.Text(nombre)),
                    bgcolor="white", border_radius=10,
                    border=ft.border.all(1, "#EEEEEE")
                )
            )
        return ft.Column([
            ft.Container(padding=15, content=ft.Text("PLANTEL", size=25, weight="bold")),
            lista
        ], expand=True)

    contenedor_principal = ft.Container(content=vista_partidos(), expand=True)

    def cambio_tab(e):
        idx = e.control.selected_index
        contenedor_principal.content = vista_partidos() if idx == 0 else vista_plantel()
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
                ft.Text("UNIÓN", weight="bold", color="white", size=24),
                ft.Image(src="UnionEscudo.png", height=100, fit="contain"),
                ft.Text("San Martín\nde los Andes", color="white", size=18, weight="bold", text_align="center")
            ],
            alignment="center",
            vertical_alignment="center",
            spacing=15
        ),
        center_title=True,
        toolbar_height=120,
        bgcolor="red",
    )

    page.add(contenedor_principal)

if __name__ == "__main__":
    ft.run(main)