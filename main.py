import flet as ft
import csv
from datetime import datetime

def main(page: ft.Page):
    page.title = "Unión Senior SMA"
    page.scroll = "always"
    page.window_resizable = True
    page.bgcolor = "white"
    page.padding = 0
    page.assets_dir = "assets"

    def mostrar_snackbar(mensaje: str):
        page.snack_bar = ft.SnackBar(ft.Text(mensaje))
        page.snack_bar.open = True
        page.update()

    # Pestañas del dashboard
    tabs_menu = ft.Tabs(
        length=6,
        selected_index=0,
        on_change=lambda e: navegar_a(["fecha", "plantel", "tabla", "fixture", "notificaciones", "tercer_tiempo"][e.control.selected_index]),
        content=ft.TabBar(
            scrollable=True,
            tabs=[
                ft.Tab(icon=ft.Icons.HOME, label="Inicio"),
                ft.Tab(icon=ft.Icons.GROUPS, label="Plantel"),
                ft.Tab(icon=ft.Icons.LEADERBOARD, label="Tabla"),
                ft.Tab(icon=ft.Icons.SCHEDULE, label="Fixture"),
                ft.Tab(icon=ft.Icons.NOTIFICATIONS_ACTIVE, label="Notificaciones"),
                ft.Tab(icon=ft.Icons.SPORTS_BAR, label="Tercer Tiempo"),
            ]
        )
    )

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

    partidos_lista = []
    try:
        with open("partidos.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                partidos_lista.append({
                    "fecha": row["fecha"],
                    "hora": row["hora"],
                    "rival": row["rival"],
                    "cancha": row["cancha"],
                    "categoria": row["categoria"],
                    "resultado": row.get("resultado", "")
                })
    except FileNotFoundError:
        partidos_lista = []

    def obtener_proximo_partido():
        hoy = datetime.now().date()
        for partido in partidos_lista:
            fecha_partido = datetime.strptime(partido["fecha"], "%Y-%m-%d").date()
            if fecha_partido >= hoy:
                return {
                    "rival": partido["rival"],
                    "fecha": partido["fecha"],
                    "hora": partido["hora"],
                    "cancha": partido["cancha"],
                    "fecha_formateada": fecha_partido.strftime("%d/%m/%Y")
                }
        if partidos_lista:
            ultimo = partidos_lista[-1]
            fecha_ultimo = datetime.strptime(ultimo["fecha"], "%Y-%m-%d").date()
            return {
                "rival": ultimo["rival"],
                "fecha": ultimo["fecha"],
                "hora": ultimo["hora"],
                "cancha": ultimo["cancha"],
                "fecha_formateada": fecha_ultimo.strftime("%d/%m/%Y")
            }
        return {
            "rival": "Por confirmar",
            "fecha": "---",
            "hora": "---",
            "cancha": "---",
            "fecha_formateada": "---"
        }

    proximo_encuentro = obtener_proximo_partido()

    equipos_torneo = {
        "Zona A": ["Frontera", "Comunicaciones", "Las Rosas", "Arenal", "Velez", "Sarmiento", "Union", "Dinamo"],
        "Zona B": ["Chapelco", "Embajadores", "Patagonia", "Lacar", "El Barrio", "Old Boys", "Belgrano", "Dinosaurios"]
    }

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

    goleadores = sorted([j for j in plantel if j["goles"] > 0], key=lambda x: x["goles"], reverse=True)

    current_view = "fecha"

    def navegar_a(vista_nombre):
        nonlocal current_view
        current_view = vista_nombre
        vistas = {
            "fecha": vista_partidos,
            "plantel": vista_plantel,
            "tabla": vista_tabla_posiciones,
            "fixture": vista_fixture,
            "notificaciones": vista_notificaciones,
            "tercer_tiempo": vista_tercer_tiempo
        }
        if vista_nombre in vistas:
            contenedor_principal.content = vistas[vista_nombre]()
            page.update()

    # --- VISTA: INICIO ---
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

        return ft.Container(
            padding=ft.Padding(left=15, right=15, top=0, bottom=0),
            content=ft.Column([
                ft.Container(height=15),
                ft.Container(
                    padding=18, bgcolor="#FFEBEE", border_radius=16,
                    content=ft.Column([
                        ft.Row([
                            ft.Column([
                                ft.Text("PRÓXIMO ENCUENTRO", size=16, weight="bold"),
                                ft.Text("Duelos clave para el torneo", size=12, color="#B71C1C")
                            ]),
                            ft.Container(
                                width=50, height=50, border_radius=25, bgcolor="#B71C1C",
                                content=ft.Row([ft.Text("VS", color="white", size=14)],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER)
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Divider(thickness=1, color="#D81B60"),
                        ft.Text(f"{proximo_encuentro['rival']}", size=22, weight="bold", color="#B71C1C"),
                        ft.Text(f"{proximo_encuentro['fecha_formateada']} · {proximo_encuentro['hora']}", size=14),
                        ft.Text(f"Estadio: {proximo_encuentro['cancha']}", size=14),
                        ft.Container(height=10),
                        ft.Text("Asegurate de llegar a tiempo y llevar la camiseta blanca.", size=12, color="grey"),
                        ft.Container(height=5),
                        ft.FilledButton(
                            "Confirmar Asistencia",
                            icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                            style=ft.ButtonStyle(
                                bgcolor="#4CAF50",
                                color="black",
                                shape=ft.RoundedRectangleBorder(radius=8),
                            ),
                            on_click=lambda _: mostrar_snackbar("Asistencia confirmada")
                        )
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
                ft.Container(height=30)
            ], expand=True, scroll="always")
        )

    # --- VISTA: FIXTURE ---
    def vista_fixture():
        partidos_controls = []
        hoy = datetime.now().date()
        
        # Sort matches by date first
        partidos_ordenados = sorted(partidos_lista, key=lambda x: x["fecha"])
        
        # Group by date
        grupos_fecha = {}
        for partido in partidos_ordenados:
            try:
                fecha_obj = datetime.strptime(partido["fecha"], "%Y-%m-%d").date()
                dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
                meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
                fecha_formateada = f"{dias[fecha_obj.weekday()]}, {fecha_obj.day} de {meses[fecha_obj.month - 1]}"
            except ValueError:
                fecha_formateada = "Fecha por confirmar"
                fecha_obj = datetime.now().date()
            
            if fecha_formateada not in grupos_fecha:
                grupos_fecha[fecha_formateada] = []
            partido["fecha_obj"] = fecha_obj
            grupos_fecha[fecha_formateada].append(partido)
            
        for fecha_str, partidos in grupos_fecha.items():
            # Add Header for the Date
            partidos_controls.append(
                ft.Container(
                    bgcolor="#F5F5F5",
                    padding=ft.Padding(left=15, right=15, top=8, bottom=8),
                    content=ft.Text(fecha_str, weight="bold", size=13, color="#424242"),
                    border=ft.Border(bottom=ft.BorderSide(1, "#E0E0E0"))
                )
            )
            
            # Add matches for this date
            for partido in partidos:
                fecha_obj = partido["fecha_obj"]
                ya_se_jugo = fecha_obj < hoy
                tiene_resultado = partido.get("resultado", "").strip() != ""
                
                estado = "FINAL" if (ya_se_jugo and tiene_resultado) else partido["hora"]
                estado_color = "#B71C1C" if not (ya_se_jugo and tiene_resultado) else "#9E9E9E"
                
                if tiene_resultado and ya_se_jugo:
                    marcador = partido["resultado"]
                    bg_row = "#F5F5F5" # Gris clarito para jugados
                    texto_equipo_color = "#616161" # Texto atenuado
                else:
                    marcador = "v"
                    bg_row = "white"
                    texto_equipo_color = "black"
                
                row_content = ft.Row([
                    ft.Container(
                        width=55, 
                        content=ft.Text(estado, weight="bold", size=13, color=estado_color)
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Row([
                            ft.Text("UNIÓN SMA", size=14, color=texto_equipo_color, weight="bold" if bg_row == "white" else "normal"),
                            ft.Container(width=8),
                            ft.Container(
                                padding=ft.Padding(left=6, right=6, top=2, bottom=2),
                                bgcolor="#E0E0E0" if marcador != "v" else "transparent",
                                border_radius=4,
                                content=ft.Text(marcador, weight="bold", size=13, color="black")
                            ),
                            ft.Container(width=8),
                            ft.Text(partido["rival"].upper(), size=14, color=texto_equipo_color, weight="bold" if bg_row == "white" else "normal")
                        ], alignment=ft.MainAxisAlignment.START, wrap=True)
                    ),
                    ft.Container(
                        width=80,
                        content=ft.Text("Cancha I", size=12, color="grey", text_align=ft.TextAlign.RIGHT)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
                
                partidos_controls.append(
                    ft.Container(
                        padding=ft.Padding(left=15, right=15, top=15, bottom=15),
                        bgcolor=bg_row,
                        border=ft.Border(bottom=ft.BorderSide(1, "#EEEEEE")),
                        content=row_content
                    )
                )

        return ft.Container(
            padding=0,
            content=ft.Column([
                ft.Container(
                    padding=ft.Padding(left=15, right=15, top=15, bottom=5),
                    content=ft.Text("Fixture", size=22, weight="bold")
                ),
                ft.Column(spacing=0, scroll="always", expand=True, controls=partidos_controls),
            ], expand=True, spacing=0)
        )

    # --- VISTA: PLANTEL ---
    def vista_plantel():
        lista = ft.ListView(expand=True, spacing=10, padding=20)
        for jugador in plantel:
            stats = ft.Container(
                width=100,
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
                        leading=ft.CircleAvatar(bgcolor="#D32F2F", content=ft.Icon("person", color="white")),
                        title=ft.Text(jugador["nombre"], weight="bold"),
                        subtitle=ft.Text(jugador["posicion"], color="grey"),
                        trailing=stats
                    ),
                    bgcolor="white", border_radius=10
                )
            )
        return ft.Container(
            padding=ft.Padding(left=15, right=15, top=0, bottom=0),
            content=ft.Column([
                ft.Container(height=15),
                ft.Text("Plantel", size=22, weight="bold"),
                lista
            ], expand=True)
        )

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
                content=ft.Row(scroll="auto", wrap=False, controls=[tabla]),
                padding=5, bgcolor="white", border_radius=10
            )

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

        goleador_turno = ft.Container(
            padding=15, bgcolor="#FFEBEE", border_radius=10,
            content=ft.Text("GOLEADOR DE LA FECHA: Silva, Facundo con 5 goles", size=16, weight="bold", color="#D32F2F")
        )

        return ft.Container(
            padding=ft.Padding(left=15, right=15, top=0, bottom=0),
            content=ft.Column([
                ft.Container(height=15),
                ft.Text("Tabla General", size=22, weight="bold"),
                ft.Container(height=20),
                tabla_general(),
                ft.Container(height=30),
                ft.Text("GOLEADORES", size=18, weight="bold"),
                goleadores_lista,
                ft.Container(height=20),
                goleador_turno,
                ft.Container(height=50)
            ], expand=True, scroll="always")
        )

    # --- VISTA: NOTIFICACIONES ---
    def vista_notificaciones():
        return ft.Container(
            padding=ft.Padding(left=15, right=15, top=0, bottom=0),
            content=ft.Column([
                ft.Container(height=15),
                ft.Text("Notificaciones", size=22, weight="bold"),
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
                                    ft.Text("Próximo partido vs Dinamo el 19/04 a las 11:45", size=13, selectable=True)
                                ], spacing=2)
                            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START, wrap=True)
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
                            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START, wrap=True)
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
                            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START, wrap=True)
                        )
                    ]
                ),
                ft.Container(height=20)
            ], expand=True, scroll="always")
        )

    # --- VISTA: TERCER TIEMPO ---
    def vista_tercer_tiempo():
        import os
        
        # Rutas de fotos por defecto (la que enviaste)
        rutas_fotos = ["UnionPlantel.png"]
        
        # Intentamos leer la carpeta tercer_tiempo si existe
        try:
            for f in os.listdir("assets/tercer_tiempo"):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    rutas_fotos.append(f"tercer_tiempo/{f}")
        except FileNotFoundError:
            pass

        posts_controls = []
        
        for foto in rutas_fotos:
            post_card = ft.Card(
                margin=ft.Margin.only(bottom=20),
                elevation=2,
                bgcolor="white",
                content=ft.Column([
                    # Header del Post (Avatar + Nombre)
                    ft.Container(
                        padding=10,
                        content=ft.Row([
                            ft.CircleAvatar(
                                bgcolor="#B71C1C", 
                                content=ft.Text("US", color="white", size=12, weight="bold"),
                                radius=16
                            ),
                            ft.Text("union_sma_oficial", weight="bold", size=14),
                            ft.Container(expand=True),
                            ft.Icon(ft.Icons.MORE_VERT, color="grey")
                        ])
                    ),
                    # Imagen
                    ft.Image(
                        src=foto, 
                        fit="contain",
                        width=float("inf"),
                    ),
                    # Acciones (Like, Comment, Share)
                    ft.Container(
                        padding=ft.Padding(left=10, right=10, top=5, bottom=0),
                        content=ft.Row([
                            ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_size=28, icon_color="black"),
                            ft.IconButton(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, icon_size=26, icon_color="black"),
                            ft.IconButton(icon=ft.Icons.SEND_OUTLINED, icon_size=26, icon_color="black"),
                            ft.Container(expand=True),
                            ft.IconButton(icon=ft.Icons.BOOKMARK_BORDER, icon_size=28, icon_color="black")
                        ], spacing=0)
                    ),
                    # Likes y Comentarios
                    ft.Container(
                        padding=ft.Padding(left=14, right=14, top=0, bottom=15),
                        content=ft.Column([
                            ft.Text("Les gusta a 24 personas", weight="bold", size=13),
                            ft.Row([
                                ft.Text("union_sma_oficial", weight="bold", size=13),
                                ft.Text("¡Tercer tiempo banda! 🍻🥩", size=13),
                            ])
                        ], spacing=2)
                    )
                ], spacing=0)
            )
            posts_controls.append(post_card)

        # Si solo está la foto por defecto, mostramos aviso
        if len(rutas_fotos) == 1:
            posts_controls.insert(0, 
                ft.Container(
                    padding=15, bgcolor="#FFEBEE", border_radius=10, margin=ft.Margin.only(bottom=20, left=15, right=15),
                    content=ft.Column([
                        ft.Text("¡Puedes agregar más fotos guardándolas en la carpeta 'assets/tercer_tiempo'!", size=14, text_align="center"),
                    ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
                )
            )

        return ft.Container(
            padding=0,
            content=ft.Column([
                ft.Container(
                    padding=ft.Padding(left=15, right=15, top=15, bottom=5),
                    content=ft.Text("Tercer Tiempo", size=22, weight="bold")
                ),
                ft.Column(spacing=0, scroll="always", expand=True, controls=posts_controls)
            ], expand=True, spacing=0)
        )

    # --- LAYOUT PRINCIPAL ---
    contenedor_principal = ft.Container(content=vista_partidos(), expand=True)

    area_contenido = ft.Container(content=contenedor_principal, expand=True)

    def on_resize(e):
        navegar_a(current_view)

    page.on_resize = on_resize
    page.appbar = None

    custom_appbar = ft.Container(
        height=120,
        bgcolor="#B71C1C",
        padding=15,
        margin=0,
        content=ft.Row([
            ft.Column([
                ft.Text("UNIÓN", weight="bold", color="white", size=32),
                ft.Text("San Martín de los Andes", color="white", size=14),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
            ft.Container(expand=True),
            ft.Image(src="UnionEscudo.png", height=100, fit="contain"),
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )

    footer = ft.Container(
        padding=18,
        bgcolor="#424242",
        border_radius=0,
        expand=False,
        content=ft.Column([
            ft.Text("UNIÓN - San Martín de los Andes", size=14, weight="bold", color="white"),
            ft.Text("Liga de Veteranos de fútbol", size=12, color="white")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.Alignment.CENTER
    )

    main_layout = ft.Column([
        custom_appbar,
        tabs_menu,
        ft.Container(content=area_contenido, expand=True),
        footer
    ], expand=True, spacing=0, margin=0)

    page.add(main_layout)


if __name__ == "__main__":
    ft.run(main)