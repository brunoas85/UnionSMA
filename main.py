import flet as ft

def main(page: ft.Page):
    page.title = "Unión Senior SMA"
    page.scroll = "always" 
    page.window_width = 450
    page.window_height = 800
    page.bgcolor = "#F5F5F5"
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
            controls=[
                ft.Text("PRÓXIMA FECHA", size=30, weight="bold"),
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        width=380, # Mantiene el ancho forzado para que el texto NO se vuelva vertical
                        content=ft.Column(
                            controls=[
                                ft.ListTile(
                                    leading=ft.Icon("sports_soccer", color="red"),
                                    title=ft.Text("Vs. Los Amigos FC", size=20, weight="bold"),
                                    subtitle=ft.Text("Sábado - 15:30hs"),
                                ),
                                ft.Divider(),
                                ft.ListTile(
                                    leading=ft.Icon("location_on", color="red"),
                                    title=ft.Text("Cancha Municipal"),
                                    subtitle=ft.Text("San Martín de los Andes"),
                                ),
                                ft.Container(height=5),
                                
                                # BOTÓN A PRUEBA DE BALAS (Container clickeable)
                                ft.Container(
                                    content=ft.Text("¿CÓMO LLEGAR?", color="white", weight="bold"),
                                    bgcolor="red",
                                    alignment="center",
                                    width=300,
                                    height=50,
                                    border_radius=5,
                                    ink=True, # Efecto visual de "onda" al hacer click
                                    on_click=lambda e: print("Acá abriremos el mapa") 
                                )
                            ],
                            horizontal_alignment="center"
                        )
                    )
                ),
                # SCROLL HORIZONTAL
                ft.Row(
                    scroll="always",
                    controls=[
                        ft.Container(
                            width=600, 
                            height=120, 
                            bgcolor="white",
                            border_radius=10,
                            padding=20,
                            content=ft.Text("TABLA DE POSICIONES (Deslizá a la derecha para ver más detalles) -->", size=16)
                        )
                    ]
                )
            ]
        )

    # --- VISTA: PLANTEL ---
    def vista_plantel():
        lista = ft.ListView(expand=True, spacing=10, padding=20)
        for nombre in plantel:
            lista.controls.append(
                ft.Container(
                    content=ft.ListTile(leading=ft.Icon("person"), title=ft.Text(nombre)),
                    bgcolor="white", border_radius=10
                )
            )
        return ft.Column([
            ft.Text("PLANTEL", size=25, weight="bold"),
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
        leading=ft.Image(src="UnionEscudo.png", fit="contain"),
        leading_width=50, 
        title=ft.Text("UNIÓN SENIOR SMA", color="white", weight="bold"),
        bgcolor="red",
        center_title=True,
    )

    page.add(contenedor_principal)

if __name__ == "__main__":
    ft.run(main)