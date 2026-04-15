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

    def mostrar_snackbar(mensaje: str):
        page.snack_bar = ft.SnackBar(ft.Text(mensaje))
        page.snack_bar.open = True
        page.update()

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

    proximo_encuentro = {
        "rival": "Chapelco",
        "fecha": "18/04/2026",
        "hora": "16:00",
        "cancha": "San Martín de los Andes"
    }

    equipos_torneo = {
        "Zona A": ["Frontera", "Comunicaciones", "Las Rosas", "Arenal", "Velez", "Sarmiento", "Union", "Dinamo"],
        "Zona B": ["Chapelco", "Embajadores", "Patagonia", "Lacar", "El Barrio", "Old Boys", "Belgrano", "Dinosaurios"]
    }

    # Datos ficticios de tabla de posiciones (para demo)
    tabla_posiciones = [
        {"equipo": "Union", "pj": 8, "pg": 6, "pe": 1, "pp": 1, "gf": 18, "gc": 8, "pts": 19},
        {"equipo": "Chapelco", "pj": 8, "pg": 5, "pe": 2, "pp": 1, "gf": 16, "gc": 9, "pts": 17},
        {"equipo": "Frontera", "pj": 8, "pg": 5, "pe": 1, "pp": 2, "gf": 15, "gc": 10, "pts": 16},
        {"equipo": "Comunicaciones", "pj": 8, "pg": 4, "pe": 2, "pp": 2, "gf": 14, "gc": 11, "pts": 14},
        {"equipo": "Las Rosas", "pj": 8, "pg": 4, "pe": 1, "pp": 3, "gf": 13, "gc": 12, "pts": 13},
        {"equipo": "Embajadores", "pj": 8, "pg": 3, "pe": 3, "pp": 2, "gf": 12, "gc": 13, "pts": 12},
        {"equipo": "Patagonia", "pj": 8, "pg": 3, "pe": 2, "pp": 3, "gf": 11, "gc": 14, "pts": 11},
        {"equipo": "Arenal", "pj": 8, "pg": 3, "pe": 1, "pp": 4, "gf": 10, "gc": 15, "pts": 10},
        {"equipo": "Velez", "pj": 8, "pg": 2, "pe": 3, "pp": 3, "gf": 9, "gc": 16, "pts": 9},
        {"equipo": "Lacar", "pj": 8, "pg": 2, "pe": 2, "pp": 4, "gf": 8, "gc": 17, "pts": 8},
        {"equipo": "Sarmiento", "pj": 8, "pg": 2, "pe": 1, "pp": 5, "gf": 7, "gc": 18, "pts": 7},
        {"equipo": "El Barrio", "pj": 8, "pg": 1, "pe": 3, "pp": 4, "gf": 6, "gc": 19, "pts": 6},
        {"equipo": "Old Boys", "pj": 8, "pg": 1, "pe": 2, "pp": 5, "gf": 5, "gc": 20, "pts": 5},
        {"equipo": "Belgrano", "pj": 8, "pg": 1, "pe": 1, "pp": 6, "gf": 4, "gc": 21, "pts": 4},
        {"equipo": "Dinamo", "pj": 8, "pg": 0, "pe": 2, "pp": 6, "gf": 3, "gc": 22, "pts": 2},
        {"equipo": "Dinosaurios", "pj": 8, "pg": 0, "pe": 1, "pp": 7, "gf": 2, "gc": 23, "pts": 1}
    ]

    # Goleadores ordenados por goles
    goleadores = sorted([j for j in plantel if j["goles"] > 0], key=lambda x: x["goles"], reverse=True)

    # --- VISTA: FECHA ---
    def vista_partidos():
        cards = [
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
            )
        ]

        equipos_controls = []
        for zona, equipos in equipos_torneo.items():
            equipos_controls.append(
                ft.Container(
                    padding=15, bgcolor="#E3F2FD", border_radius=10, width=260,
                    content=ft.Column([
                        ft.Text(zona, size=16, weight="bold"),
                        ft.Divider(thickness=1, color="#1976D2"),
                        *[ft.Text(f"• {equipo}", size=14) for equipo in equipos]
                    ], spacing=4)
                )
            )

        return ft.Column(
            scroll="always",
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=20),
                ft.Container(
                    padding=18, bgcolor="#FFEBEE", border_radius=16, width=340,
                    content=ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text("PRÓXIMO ENCUENTRO", size=16, weight="bold"),
                                ft.Text("Duelos clave para el torneo", size=12, color="#B71C1C")
                            ]),
                            ft.Container(
                                width=50, height=50, border_radius=25, bgcolor="#B71C1C",
                                content=ft.Row([
                                    ft.Text("VS", color="white", size=14)], alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Divider(thickness=1, color="#D81B60"),
                        ft.Text(f"{proximo_encuentro['rival']}", size=22, weight="bold", color="#B71C1C"),
                        ft.Text(f"{proximo_encuentro['fecha']} · {proximo_encuentro['hora']}", size=14),
                        ft.Text(f"Estadio: {proximo_encuentro['cancha']}", size=14),
                        ft.Container(height=10),
                        ft.Text("Asegurate de llegar a tiempo y llevar la camiseta blanca.", size=12, color="grey")
                    ], spacing=8)
                ),
                ft.Container(height=20),
                ft.Row(
                    scroll="auto",
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=cards
                ),
                ft.Container(height=30),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.FilledButton(
                            "Plantel y Perfiles",
                            icon="groups",
                            icon_color="white",
                            style=ft.ButtonStyle(
                                bgcolor="#C62828",
                                color="white",
                                padding=20,
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda _: ir_a_plantel()
                        ),
                        ft.Container(width=20),
                        ft.FilledButton(
                            "Tabla de Posiciones",
                            icon="leaderboard",
                            icon_color="#C62828",
                            style=ft.ButtonStyle(
                                bgcolor="white",
                                color="#C62828",
                                padding=20,
                                side=ft.BorderSide(width=1, color="#C62828"),
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda _: ir_a_tabla()
                        )
                    ]
                ),
                ft.Container(height=30),
                ft.Text("EQUIPOS DEL TORNEO", size=18, weight="bold"),
                ft.Row(
                    scroll="auto",
                    wrap=True,
                    spacing=15,
                    run_spacing=15,
                    controls=equipos_controls
                ),
                ft.Container(height=30),
                ft.Text("NOTIFICACIONES", size=18, weight="bold"),
                ft.Column(
                    spacing=10,
                    controls=[
                        ft.Container(
                            padding=15, bgcolor="#FFF3E0", border_radius=10,
                            content=ft.Text("Recordatorio: Próximo partido vs Chapelco el 18/04 a las 16:00", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#E8F5E8", border_radius=10,
                            content=ft.Text("Felicitaciones al equipo por la victoria en el último partido!", size=14)
                        ),
                        ft.Container(
                            padding=15, bgcolor="#FFEBEE", border_radius=10,
                            content=ft.Text("Importante: Llevar camiseta alternativa blanca.", size=14)
                        )
                    ]
                ),
                ft.Container(height=30),
                ft.Text("TERCER TIEMPO", size=18, weight="bold"),
                ft.Container(
                    padding=15, bgcolor="#FFEBEE", border_radius=10,
                    content=ft.Column([
                        ft.Text("Comparte fotos del post-partido, el asado y la camaradería del club", size=14),
                        ft.FilledButton(
                            "Subir Foto",
                            icon="photo_camera",
                            icon_color="white",
                            style=ft.ButtonStyle(
                                bgcolor="#C62828",
                                color="white"
                            ),
                            on_click=lambda _: mostrar_snackbar("Función de subir foto próximamente disponible")
                        )
                    ], spacing=10)
                ),
                ft.Container(height=20)
            ]
        )

    # --- VISTA: PLANTEL ---
    def vista_plantel():
        lista = ft.ListView(expand=True, spacing=10, padding=20)
        for jugador in plantel:
            stats = ft.Container(
                width=100, # Esto evita que aplaste al texto de la izquierda
                padding=6,
                bgcolor="white",
                border_radius=8,
                content=ft.Row(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon("sports_soccer", size=18, color="#4CAF50"),
                        ft.Text(str(jugador["goles"]), size=14, weight="bold"),
                        ft.Icon("square", size=18, color="#FF9800"),
                        ft.Text(str(jugador["amarillas"]), size=14, weight="bold"),
                    ]
                )
            )
            
            lista.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.CircleAvatar(
                            bgcolor="#D32F2F",
                            content=ft.Icon("person", color="white")
                        ), 
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
                    icon_color="#1976D2",
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

    # --- VISTA: TABLA DE POSICIONES ---
    def vista_tabla_posiciones():
        def tabla_general():
            tabla = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Pos", weight="bold")),
                    ft.DataColumn(ft.Text("Equipo", weight="bold")),
                    ft.DataColumn(ft.Text("PJ", weight="bold")),
                    ft.DataColumn(ft.Text("PG", weight="bold")),
                    ft.DataColumn(ft.Text("PE", weight="bold")),
                    ft.DataColumn(ft.Text("PP", weight="bold")),
                    ft.DataColumn(ft.Text("GF", weight="bold")),
                    ft.DataColumn(ft.Text("GC", weight="bold")),
                    ft.DataColumn(ft.Text("Pts", weight="bold")),
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(str(i+1))),
                        ft.DataCell(ft.Text(equipo["equipo"])),
                        ft.DataCell(ft.Text(str(equipo["pj"]))),
                        ft.DataCell(ft.Text(str(equipo["pg"]))),
                        ft.DataCell(ft.Text(str(equipo["pe"]))),
                        ft.DataCell(ft.Text(str(equipo["pp"]))),
                        ft.DataCell(ft.Text(str(equipo["gf"]))),
                        ft.DataCell(ft.Text(str(equipo["gc"]))),
                        ft.DataCell(ft.Text(str(equipo["pts"]))),
                    ]) for i, equipo in enumerate(tabla_posiciones)
                ],
                border=ft.Border.all(1, "#E0E0E0"),
                border_radius=10,
                heading_row_height=40,
                data_row_min_height=35,
                width=900,
            )

            return ft.Container(
                content=ft.Row(
                    scroll="auto",
                    wrap=False,
                    controls=[tabla]
                ),
                padding=5,
                bgcolor="white",
                border_radius=10
            )

        # Goleadores
        goleadores_lista = ft.Column(
            spacing=5,
            controls=[
                ft.Container(
                    padding=10, bgcolor="#FFF3E0", border_radius=8,
                    content=ft.Row([
                        ft.Text(f"{i+1}. {g['nombre']}", size=14, weight="bold"),
                        ft.Container(width=10),
                        ft.Text(f"{g['goles']} goles", size=14),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ) for i, g in enumerate(goleadores)
            ]
        )

        # Mención al goleador de turno
        goleador_turno = ft.Container(
            padding=15, bgcolor="#FFEBEE", border_radius=10,
            content=ft.Text("GOLEADOR DE TURNO: Silva, Facundo con 5 goles", size=16, weight="bold", color="#D32F2F")
        )

        cabecera = ft.Row(
            controls=[
                ft.FilledButton(
                    "",
                    icon="home",
                    icon_color="#1976D2",
                    bgcolor="#E0E0E0",
                    width=44,
                    height=44,
                    on_click=lambda _: volver_a_inicio()
                ),
                ft.Text("TABLA DE POSICIONES", size=22, weight="bold")
            ],
            alignment="start",
            vertical_alignment="center",
            spacing=10
        )

        return ft.Column([
            ft.Container(padding=15, content=cabecera),
            ft.Container(height=20),
            ft.Text("TABLA GENERAL", size=18, weight="bold"),
            tabla_general(),
            ft.Container(height=30),
            ft.Text("GOLEADORES", size=18, weight="bold"),
            goleadores_lista,
            ft.Container(height=20),
            goleador_turno,
            ft.Container(height=50)
        ], expand=True, scroll="always")

    contenedor_principal = ft.Container(content=vista_partidos(), expand=True)
    current_view = "fecha"

    def on_resize(e):
        if current_view == "fecha":
            contenedor_principal.content = vista_partidos()
        elif current_view == "plantel":
            contenedor_principal.content = vista_plantel()
        elif current_view == "tabla":
            contenedor_principal.content = vista_tabla_posiciones()
        page.update()

    page.on_resize = on_resize

    def cambio_tab(e):
        nonlocal current_view
        idx = e.control.selected_index
        if idx == 0:
            current_view = "fecha"
            contenedor_principal.content = vista_partidos()
        else:
            current_view = "plantel"
            contenedor_principal.content = vista_plantel()
        page.update()

    def ir_a_plantel():
        nonlocal current_view
        current_view = "plantel"
        page.navigation_bar.selected_index = 1
        contenedor_principal.content = vista_plantel()
        page.update()

    def ir_a_tabla():
        nonlocal current_view
        current_view = "tabla"
        contenedor_principal.content = vista_tabla_posiciones()
        page.update()

    def volver_a_inicio():
        nonlocal current_view
        current_view = "fecha"
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
                ft.Column([
                    ft.Text("UNIÓN", weight="bold", color="white", size=36),
                    ft.Text("San Martín de los Andes", color="white", size=16)
                ], spacing=4),
                ft.Image(src="UnionEscudo.png", height=120, fit="contain")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            wrap=True
        ),
        center_title=True,
        toolbar_height=120,
        bgcolor="#B71C1C",
    )

    footer = ft.Container(
        padding=18,
        bgcolor="#424242",
        border_radius=0,
        content=ft.Column([
            ft.Text("Unión San Martín de los Andes - Unidos por la camiseta", size=14, weight="bold", color="white"),
            ft.Text("Liga de Veteranos", size=12, color="white")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.Alignment.CENTER
    )

    page.add(contenedor_principal, footer)

if __name__ == "__main__":
    ft.run(main)