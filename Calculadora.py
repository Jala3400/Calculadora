import tkinter as tk
import math

# Todo: ================================================== Calculadora normal ==================================================

# * Interfaz de la calculadora básica ==================================================


def Calculadora_normal():

    global root
    root.title("Calculadora")

    global backg
    backg = "grey96"

    global backg2
    backg2 = "white"

    global foreg
    foreg = "black"

    global frame
    frame = tk.LabelFrame(root, bg="grey96", relief="ridge", borderwidth=10)
    frame.pack(side=tk. LEFT, pady=20, padx=20)

    # Parte de arriba ==================================================

    global entry_operacion
    entry_operacion = tk.Entry(frame, justify=tk.RIGHT, textvariable=tk.StringVar(
        root, value=""), borderwidth=5, bg="cyan")

    global c_button
    c_button = tk.Button(frame, text="C", command=c,
                         bg="red", width=3, activebackground="red2")

    global d_button
    d_button = tk.Button(frame, text="<--", command=borrar,
                         bg="red", width=3, activebackground="red2")

    # Números ==================================================

    _1 = tk.Button(frame, text="1", command=lambda: poner_simbolo(
        "1"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _2 = tk.Button(frame, text="2", command=lambda: poner_simbolo(
        "2"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _3 = tk.Button(frame, text="3", command=lambda: poner_simbolo(
        "3"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _4 = tk.Button(frame, text="4", command=lambda: poner_simbolo(
        "4"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _5 = tk.Button(frame, text="5", command=lambda: poner_simbolo(
        "5"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _6 = tk.Button(frame, text="6", command=lambda: poner_simbolo(
        "6"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _7 = tk.Button(frame, text="7", command=lambda: poner_simbolo(
        "7"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _8 = tk.Button(frame, text="8", command=lambda: poner_simbolo(
        "8"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _9 = tk.Button(frame, text="9", command=lambda: poner_simbolo(
        "9"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    _0 = tk.Button(frame, text="0", command=lambda: poner_simbolo(
        "0"), bg="lightgreen", width=3, activebackground="SpringGreen2")

    global pi
    pi = tk.Button(frame, text="π", command=lambda: poner_simbolo(
        str(math.pi)), bg="dodgerblue3", width=3, activebackground="dodgerblue")

    pts = tk.Button(frame, text="( )", command=lambda: poner_simbolo(
        "()", 1), bg="green2", width="3", activebackground="limegreen")

    global punto
    punto = tk.Button(frame, text=".", command=lambda: poner_simbolo(
        "."), bg="lightgreen", width=3, activebackground="SpringGreen2")

    e = tk.Button(frame, text="e", command=lambda: poner_simbolo(
        str(math.e)), bg="dodgerblue3", width=3, activebackground="limegreen")

    fin = tk.Button(frame, text="Fin", command=lambda: entry_operacion.icursor(
        tk.END), bg="yellow", width=3, activebackground="yellow2")

    # Operaciones ==================================================

    igual = tk.Button(frame, text="=", command=igual_,
                      bg="purple", width=3, activebackground="darkviolet")

    sumar = tk.Button(frame, text="+", command=lambda: poner_simbolo("+"),
                      bg="green2", width=3, activebackground="limegreen")

    restar = tk.Button(frame, text="-", command=lambda: poner_simbolo("-"),
                       bg="green2", width=3, activebackground="limegreen")

    multiplicar = tk.Button(frame, text="*", command=lambda: poner_simbolo("*"),
                            bg="green2", width=3, activebackground="limegreen")

    dividir = tk.Button(frame, text="/", command=lambda: poner_simbolo("/"),
                        bg="green2", width=3, activebackground="limegreen")

    cuadrado = tk.Button(frame, text="x²", command=lambda: poner_simbolo(
        "**()", 1), bg="green2", width=3, activebackground="limegreen")

    raiz_cuadrada = tk.Button(frame, text="√x", command=lambda: poner_simbolo(
        "**(1/)", 1), bg="green2", width=3, activebackground="limegreen")

    # Memoria ==================================================

    global memoria1
    memoria1 = tk.Entry(frame, textvariable=tk.StringVar(
        root, value=""), state="readonly", justify=tk.RIGHT, width=12)

    m1 = tk.Button(frame, text="m1", command=lambda: _m(
        memoria1.get()), bg="goldenrod", width=4, activebackground="gold")

    m1_in = tk.Button(frame, text="m1 in", command=lambda: _m_in(
        memoria1), bg="goldenrod", width=4, activebackground="gold")

    global memoria2
    memoria2 = tk.Entry(frame, textvariable=tk.StringVar(
        root, value=""), state="readonly", justify=tk.RIGHT,  width=12)

    m2 = tk.Button(frame, text="m2", command=lambda: _m(
        memoria2.get()), bg="goldenrod", width=4, activebackground="gold")

    m2_in = tk.Button(frame, text="m2 in", command=lambda: _m_in(
        memoria2), bg="goldenrod", width=4, activebackground="gold")

    # Historial ==================================================

    global h_frame
    h_frame = tk.Frame(root, relief="ridge", borderwidth=5, bg=backg)
    h_frame.pack(side=tk.RIGHT, fill=tk.Y)

    global yscroll_history
    yscroll_history = tk.Scrollbar(h_frame, bg=backg)
    yscroll_history.pack(side=tk.RIGHT, padx=5, fill=tk.Y)

    global history_title
    history_title = tk.Label(h_frame, text="Historial",
                             bg=backg, fg="goldenrod")
    history_title.pack(side=tk.TOP)

    global history
    history = tk.Listbox(
        h_frame, yscrollcommand=yscroll_history.set, fg="goldenrod", bg=backg2, width=30)
    history.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)

    # Teclas del teclado ==================================================

    root.bind("<Control-BackSpace>", lambda _: c())
    root.bind("f", lambda _: entry_operacion.icursor(tk.END))
    root.bind("c", lambda _: c())
    root.bind("<Return>", lambda _: igual_())
    root.bind("<Control-p>", lambda _: poner_simbolo(str(math.pi)))
    root.bind("<Control-e>", lambda _: poner_simbolo(str(math.e)))
    root.bind("<Control-8>", lambda _: poner_simbolo("()", 1))
    root.bind("<Control-*>", lambda _: poner_simbolo("**()", 1))
    root.bind("<Control-/>", lambda _: poner_simbolo("**(1/)", 1))
    root.bind("<Shift-0>", lambda _: igual_())

    # Errores ==================================================

    alargada_l1 = [_1, _2, _3, sumar,
                   multiplicar, cuadrado, c_button, d_button]
    alargada_l2 = [_4, _5, _6, restar, dividir, raiz_cuadrada, pts, fin]
    alargada_l3 = [_7, _8, _9, pi]
    alargada_l4 = [punto, _0, igual, e, m1, m1_in, m2, m2_in]
    global alargada
    alargada = [alargada_l1, alargada_l2, alargada_l3, alargada_l4]

    normal_l1 = [_1, _2, _3, pts, fin]
    normal_l2 = [_4, _5, _6, sumar, restar]
    normal_l3 = [_7, _8, _9, multiplicar, dividir]
    normal_l4 = [punto, _0, igual, cuadrado, raiz_cuadrada]
    global normal_l6
    normal_l6 = [m1, m1_in, m2, m2_in, e]
    global normal
    normal = [normal_l1, normal_l2, normal_l3, normal_l4, normal_l6]

    distribucion_normal()
    menus()

# * Back end calculadora básica ==================================================

# Borrar ==================================================


def c():

    entry_operacion["textvariable"] = tk.StringVar(value="")


def borrar():

    contenido = entry_operacion.get()
    cursor = entry_operacion.index(tk.INSERT)
    try:
        if contenido[cursor - 1] == "(" and contenido[cursor] == ")":
            entry_operacion.delete(cursor - 1, cursor + 1)

        else:
            entry_operacion.delete(cursor - 1, cursor)

    except Exception:
        pass

# Operaciones ==================================================


def igual_():

    expresion = entry_operacion.get()

    if expresion == "":
        entry_operacion["textvariable"] = tk.StringVar(
            value="Introduce una operación")

    else:
        resultado = parsear(expresion, entry_operacion)
        history.insert(0, expresion, resultado)


def poner_simbolo(simbolo, cursor_=0):

    entry_operacion.insert(entry_operacion.index(tk.INSERT), simbolo)
    entry_operacion.icursor(entry_operacion.index(tk.INSERT) - cursor_)

# Memoria ==================================================


def _m_in(m):

    _m1_ = entry_operacion.get()

    if _m1_.strip() == "":
        entry_operacion["textvariable"] = tk.StringVar(
            value="No hay nada en la pantalla")

    else:
        m["textvariable"] = tk.StringVar(value=_m1_)


def _m(m_):

    if m_ == "":
        entry_operacion["textvariable"] = tk.StringVar(
            value="No hay nada en esa memoria")

    else:
        entry_operacion["textvariable"] = tk.StringVar(value=m_)

# Todo: ================================================== Teorema de Pitágoras ==================================================

# * Interfaz de Pitágoras ==================================================


def pitagoras():

    global pitagoras_wind
    pitagoras_wind = tk.Toplevel(bg=backg2)
    pitagoras_wind.title("Pitágoras")

    global p_frame
    p_frame = tk.LabelFrame(pitagoras_wind, bg=backg)
    p_frame.pack(pady=20, padx=20)

    global instrucciones_p
    instrucciones_p = tk.Label(p_frame, text="Introduce el valor de los dos catetos y la hipotenusa,\ndejando en blanco el lado desconocido.\nAdemás, si rellenas todos los campos, obtienes de\nqué tipo de triángulo se trata. El lado más largo\ntiene que ir en la hipotenusa", bg=backg, fg=foreg, justify=tk.LEFT)
    instrucciones_p.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

    global cateto_1
    cateto_1 = tk.Label(p_frame, text="Cateto 1: ", bg=backg, fg=foreg)
    cateto_1.grid(row=1, column=0, pady=5, padx=5)

    global entry_cateto_1
    entry_cateto_1 = tk.Entry(p_frame)
    entry_cateto_1.grid(row=1, column=1, pady=5, padx=5)

    global cateto_2
    cateto_2 = tk.Label(p_frame, text="Cateto 2: ", bg=backg, fg=foreg)
    cateto_2.grid(row=2, column=0, pady=5, padx=5)

    global entry_cateto_2
    entry_cateto_2 = tk.Entry(p_frame)
    entry_cateto_2.grid(row=2, column=1, pady=5, padx=5)

    global hipotenusa
    hipotenusa = tk.Label(p_frame, text="Hipotenusa", bg=backg, fg=foreg)
    hipotenusa.grid(row=3, column=0, pady=5, padx=5)

    global entry_hipotenusa
    entry_hipotenusa = tk.Entry(p_frame)
    entry_hipotenusa.grid(row=3, column=1, pady=5, padx=5)

    global sol_p_button
    sol_p_button = tk.Button(p_frame, text="Solucionar", command=id_p_incognita,
                             bg="dodgerblue", activebackground="deepskyblue")
    sol_p_button.grid(row=4, column=0, sticky=tk.W + tk.E, pady=5, padx=5)

    global solucion_pitagoras
    solucion_pitagoras = tk.Entry(
        p_frame, state="readonly", textvariable=tk.StringVar(value=""))
    solucion_pitagoras.grid(row=4, column=1, pady=5, padx=5)

    global componentes_pitagoras_backg
    componentes_pitagoras_backg = [
        p_frame, instrucciones_p, cateto_1, cateto_2, hipotenusa]

# Teclas ==================================================

    pitagoras_wind.bind("<Return>", lambda _: id_p_incognita())
    pitagoras_wind.bind("<Shift-0>", lambda _: id_p_incognita())

# * Back end Pitágoras ==================================================


def id_p_incognita():

    c1 = entry_cateto_1.get().strip()
    c2 = entry_cateto_2.get().strip()
    h = entry_hipotenusa.get().strip()

    if (h == "" and c1 == "") or (c1 == "" and c2 == "") or (c2 == "" and h == ""):
        entry_hipotenusa["textvariable"] = tk.StringVar(
            value="Datos insuficientes")

    elif h == "":
        c1 = parsear(c1, entry_cateto_1)
        c2 = parsear(c2, entry_cateto_2)

        if type(c1) != str or type(c2) != str:

            solucion = (c1**2 + c2**2)**(1/2)
            lados_triangulo = (f"c1 = {c1}, c2 = {c2}, h = x")
            entry_hipotenusa["textvariable"] = tk.StringVar(
                root, value=solucion)
            history.insert(0, lados_triangulo, solucion)

    elif c1 == "":
        h = parsear(h, entry_hipotenusa)
        c2 = parsear(c2, entry_cateto_2)

        if type(h) != str or type(c2) != str:
            sol_pitagoras(h, c2, entry_cateto_1)

    elif c2 == "":
        h = parsear(h, entry_hipotenusa)
        c1 = parsear(c1, entry_cateto_1)

        if type(h) != str or type(c1) != str:
            sol_pitagoras(h, c1, entry_cateto_2)

    else:
        id_triangulo(c1, c2, h)


def sol_pitagoras(n1, n2, posicion):

    solucion = (n1**2 - n2**2)**(1/2)
    lados_triangulo = (f"c1 = {n1}, c2 = x, h = {n2}")
    posicion["textvariable"] = tk.StringVar(root, value=solucion)
    history.insert(0, lados_triangulo, solucion)


def id_triangulo(c1_, c2_, h_):

    try:
        c1_ = parsear(c1_, entry_cateto_1)
        c2_ = parsear(c2_, entry_cateto_2)
        h_ = parsear(h_, entry_hipotenusa)

        if type(c1_) != str and type(c2_) != str and type(h_) != str:

            if c1_ - c2_ >= h_ or c2_ - c1_ >= h_:
                solucion = "El triángulo no exsiste"

            elif c1_ == c2_ and c2_ == h_:
                solucion = "Equilatero"

            elif c1_ == c2_ and c2_ != h_:
                solucion = "Isósceles"

            else:
                solucion = "Escaleno"

            lados_triangulo = (f"c1 = {c1_}, c2 = {c2_}, h = {h_}")
            solucion_pitagoras["textvariable"] = tk.StringVar(value=solucion)
            history.insert(0, lados_triangulo, solucion)

        else:
            solucion_pitagoras["textvariable"] = tk.StringVar(
                value="El triángulo no existe")

    except:
        pass

# Todo: ================================================== Ecuaciones de segundo grado ==================================================

# * Interfaz de ecuaciones de segundo grado ==================================================


def ecuacion_2º_grado():

    global ecuaciones_2º_wind
    ecuaciones_2º_wind = tk.Toplevel(bg=backg2)
    ecuaciones_2º_wind.title("Ecuaciones 2º grado")

    global e2_frame
    e2_frame = tk.LabelFrame(ecuaciones_2º_wind, bg=backg)
    e2_frame.pack(pady=20, padx=20)

    global instrucciones_e2
    instrucciones_e2 = tk.Label(
        e2_frame, text="Introduce el valor de \"a\", \"b\" y \"c\"en :\nax² + (bx) + (c)\nSi falta algún dato, pon un 0", bg=backg, fg=foreg, justify=tk.LEFT)
    instrucciones_e2.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

    global e2_a
    e2_a = tk.Label(e2_frame, text="a: ", bg=backg, fg=foreg)
    e2_a.grid(row=1, column=0, pady=5, padx=5)

    global entry_e2_a
    entry_e2_a = tk.Entry(e2_frame)
    entry_e2_a.grid(row=1, column=1, pady=5, padx=5)
    entry_e2_a.focus()

    global e2_b
    e2_b = tk.Label(e2_frame, text="b: ", bg=backg, fg=foreg)
    e2_b.grid(row=2, column=0, pady=5, padx=5)

    global entry_e2_b
    entry_e2_b = tk.Entry(e2_frame)
    entry_e2_b.grid(row=2, column=1, pady=5, padx=5)

    global e2_c
    e2_c = tk.Label(e2_frame, text="c: ", bg=backg, fg=foreg)
    e2_c.grid(row=3, column=0, pady=5, padx=5)

    global entry_e2_c
    entry_e2_c = tk.Entry(e2_frame)
    entry_e2_c.grid(row=3, column=1, pady=5, padx=5)

    global sol_e2_button
    sol_e2_button = tk.Button(e2_frame, text="Solucionar", command=sol_e2,
                              bg="dodgerblue", activebackground="deepskyblue")
    sol_e2_button.grid(row=4, column=0, columnspan=2,
                       sticky=tk.W + tk.E, pady=5, padx=5)

    global solucion_mas_e2
    solucion_mas_e2 = tk.Entry(
        e2_frame, state="readonly", textvariable=tk.StringVar(value=""))
    solucion_mas_e2.grid(row=5, column=0, pady=5, padx=5)

    global solucion_menos_e2
    solucion_menos_e2 = tk.Entry(
        e2_frame, state="readonly", textvariable=tk.StringVar(value=""))
    solucion_menos_e2.grid(row=5, column=1, pady=5, padx=5)

    global componentes_e2_backg
    componentes_e2_backg = [e2_frame, instrucciones_e2, e2_a, e2_b, e2_c]

# Teclas ==================================================

    ecuaciones_2º_wind.bind("<Return>", lambda _: sol_e2())
    ecuaciones_2º_wind.bind("<Shift-0>", lambda _: igual_)

# * Back end ecuaciones de segundo grado ==================================================


def sol_e2():

    e2_a = entry_e2_a.get().strip()
    e2_b = entry_e2_b.get().strip()
    e2_c = entry_e2_c.get().strip()

    if e2_a == "" or e2_b == "" or e2_c == "":
        solucion_mas_e2["textvariable"] = tk.StringVar(
            value="Datos insuficientes")

    else:
        e2_a = parsear(e2_a, entry_e2_a)
        e2_b = parsear(e2_b, entry_e2_b)
        e2_c = parsear(e2_c, entry_e2_c)

        if type(e2_a) != str and type(e2_b) != str and type(e2_c) != str:

            raiz_e2 = e2_b**2 - 4 * e2_a * e2_c

            if raiz_e2 >= 0:

                e2_b = float(e2_b)
                resultado_mas_e2 = (-e2_b + (raiz_e2)**(1/2))/2*e2_a
                resultado_menos_e2 = (-e2_b - (raiz_e2)**(1/2))/2*e2_a

                solucion_mas_e2["textvariable"] = tk.StringVar(
                    value=resultado_mas_e2)
                solucion_menos_e2["textvariable"] = tk.StringVar(
                    value=resultado_menos_e2)

            else:
                solucion_mas_e2["textvariable"] = tk.StringVar(
                    value="No existe")
                solucion_menos_e2["textvariable"] = tk.StringVar(
                    value="No existe")

# Todo: ================================================== Teorema de Tales ==================================================

# * Interfaz del teorema de Tales ==================================================


def tales():

    global tales_wind
    tales_wind = tk.Toplevel(bg=backg2)
    tales_wind.title("Tales")

    global t_frame
    t_frame = tk.LabelFrame(tales_wind, bg=backg)
    t_frame.pack(pady=20, padx=20)

    global instrucciones_t
    instrucciones_t = tk.Label(
        t_frame, text="Introduce los valores de los lados de los triángulos\nen su lugar, dejando en blanco la incógnita.\n(Se moverá a fracciones)", bg=backg, fg=foreg, justify=tk.LEFT)
    instrucciones_t.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

    global entry_t_a
    entry_t_a = tk.Entry(t_frame)
    entry_t_a.grid(row=1, column=0, pady=5, padx=5)
    entry_t_a.focus()

    global entry_t_b
    entry_t_b = tk.Entry(t_frame)
    entry_t_b.grid(row=1, column=1, pady=5, padx=5)

    global tales_linea_division
    tales_linea_division = tk.Label(
        t_frame, text="——————————   =   ——————————", bg=backg, fg=foreg)
    tales_linea_division.grid(row=2, column=0, pady=5, padx=5, columnspan=2)

    global entry_t_A
    entry_t_A = tk.Entry(t_frame)
    entry_t_A.grid(row=3, column=0, pady=5, padx=5)

    global entry_t_B
    entry_t_B = tk.Entry(t_frame)
    entry_t_B.grid(row=3, column=1, pady=5, padx=5)

    global sol_t_button
    sol_t_button = tk.Button(t_frame, text="Solucionar", command=id_t_incognita,
                             bg="dodgerblue", activebackground="deepskyblue")
    sol_t_button.grid(row=4, column=0, columnspan=2,
                      sticky=tk.W + tk.E, pady=5, padx=5)

    global componentes_tales_backg
    componentes_tales_backg = [t_frame, instrucciones_t, tales_linea_division]

# Teclas ==================================================

    tales_wind.bind("<Return>", lambda _: id_t_incognita())
    tales_wind.bind("<Shift-0>", lambda _: id_t_incognita())

# * Back end teorema de tales ==================================================


def id_t_incognita():

    global t_a, t_b, t_A, t_B
    t_a = entry_t_a.get().strip()
    t_b = entry_t_b.get().strip()
    t_A = entry_t_A.get().strip()
    t_B = entry_t_B.get().strip()

    if (t_a == "" and t_b == "") or (t_a == "" and t_A == "") or (t_a == "" and t_B == "") or (t_b == "" and t_A == "") or (t_b == "" and t_B == "") or (t_A == "" and t_B == ""):
        entry_t_B["textvariable"] = tk.StringVar(value="Datos insuficientes")

    elif t_a != "" and t_b != "" and t_A != "" and t_B != "":
        entry_t_B["textvariable"] = tk.StringVar(value="Demasiados datos")

    elif t_a == "":
        t_b = parsear(t_b, entry_t_b)
        t_A = parsear(t_A, entry_t_A)
        t_B = parsear(t_B, entry_t_B)
        t_a = "x"

        if type(t_b) != str and type(t_A) != str and type(t_B) != str():
            sol_tales(entry_t_a, t_A, t_b, t_B)

        else:
            entry_t_a["textvariable"] = tk.StringVar(value="No existe")

    elif t_b == "":
        t_a = parsear(t_a, entry_t_a)
        t_A = parsear(t_A, entry_t_A)
        t_B = parsear(t_B, entry_t_B)
        t_b = "x"

        if type(t_a) != str and type(t_A) != str and type(t_B) != str:
            sol_tales(entry_t_b, t_A, t_a, t_B)

        else:
            entry_t_b["textvariable"] = tk.StringVar(value="No existe")

    elif t_A == "":
        t_b = parsear(t_b, entry_t_b)
        t_a = parsear(t_a, entry_t_a)
        t_B = parsear(t_B, entry_t_B)
        t_A = "x"

        if type(t_b) != str and type(t_A) != str and type(t_B) != str:
            sol_tales(entry_t_A, t_B, t_b, t_a)

        else:
            entry_t_A["textvariable"] = tk.StringVar(value="No existe")

    elif t_B == "":
        t_b = parsear(t_b, entry_t_b)
        t_A = parsear(t_A, entry_t_A)
        t_a = parsear(t_a, entry_t_a)
        t_B = "x"

        if type(t_a) != str and type(t_A) != str and type(t_b) != str:
            sol_tales(entry_t_B, t_A, t_b, t_a)

        else:
            entry_t_B["textvariable"] = tk.StringVar(value="No existe")


def sol_tales(entry, arriba1, arriba2, abajo):

    solucion = (arriba1 * arriba2) / abajo
    entry["textvariable"] = tk.StringVar(value=solucion)
    lados_triangulo = (f"a = {t_a}, A = {t_A}, b = {t_b}, B = {t_B}")
    history.insert(0, lados_triangulo, solucion)

# Todo: ================================================== Configuración ==================================================

# * Distribuciones ==================================================

# Ditribución alargada (solo colculadora normal) ==================================================


def distribucion_alargada():

    x = 0
    y = 1

    entry_operacion.grid(columnspan=8)
    entry_operacion.focus()

    for lista in alargada:
        for item in lista:
            item.grid(row=y, column=x)
            x += 1
        x = 0
        y += 1

    memoria1.grid(row=3, column=4)
    memoria2.grid(row=3, column=6)
    root.maxsize(650, 240)
    root.minsize(650, 240)

# Ditribución normal (solo calculadora normal) ==================================================


def distribucion_normal():

    x = 0
    y = 1

    entry_operacion.grid(row=0, column=0, columnspan=3,
                         pady=5, padx=5, sticky=tk.W + tk.E)
    entry_operacion.focus()
    c_button.grid(row=0, column=3, pady=5, padx=5)
    d_button.grid(row=0, column=4, pady=5, padx=5)

    memoria1.grid(row=5, column=0, pady=5, padx=5, columnspan=2)
    memoria2.grid(row=5, column=2, pady=5, padx=5, columnspan=2)
    pi.grid(row=5, column=4, pady=5, padx=5)

    for lista in normal:
        if lista == normal_l6:
            y += 1

        for item in lista:
            item.grid(row=y, column=x, pady=5, padx=5)

            x += 1

        x = 0
        y += 1
    root.maxsize(525, 315)
    root.minsize(525, 315)

# * Temas ==================================================


def temas(colorb, colorb2, colorf):

    global backg
    backg = colorb

    global backg2
    backg2 = colorb2

    global foreg
    foreg = colorf

    # Calculadora normal ==================================================

    root.configure(bg=backg2)
    frame.configure(bg=backg, fg=foreg)
    h_frame.configure(bg=backg)
    history_title.configure(bg=backg)
    yscroll_history.configure(bg=backg)
    history.configure(bg=backg2)

    # Pitagoras ==================================================

    try:
        pitagoras_wind.configure(bg=backg2)

        for componente in componentes_pitagoras_backg:
            componente.configure(bg=backg, fg=foreg)

    except:
        pass

    # Ecuaciones 2º grado ==================================================

    try:
        ecuaciones_2º_wind.configure(bg=backg2)

        for componente in componentes_e2_backg:
            componente.configure(bg=backg, fg=foreg)

    except:
        pass

    # Tales ==================================================

    try:
        tales_wind.configure(bg=backg2)

        for componente in componentes_tales_backg:
            componente.configure(bg=backg, fg=foreg)

    except:
        pass

# * Menus ==================================================


def menus():

    menu = tk.Menu(root)
    root.configure(bg="white", menu=menu)

    ecuaciones = tk.Menu(menu, tearoff=0)
    teoremas = tk.Menu(menu, tearoff=0)
    configuracion = tk.Menu(menu, tearoff=0)
    distribucion = tk.Menu(configuracion, tearoff=0)
    tema = tk.Menu(configuracion, tearoff=0)

    ecuaciones.add_command(label="2º grado", command=ecuacion_2º_grado)

    teoremas.add_command(label="Pitagoras", command=pitagoras)
    teoremas.add_command(label="Tales", command=tales)

    configuracion.add_cascade(label="Distribución", menu=distribucion)
    configuracion.add_cascade(label="Tema", menu=tema)

    distribucion.add_radiobutton(
        label="Distribución normal", command=distribucion_normal)
    distribucion.add_radiobutton(
        label="Distribución alargada", command=distribucion_alargada)

    tema.add_radiobutton(label="Modo luminoso",
                         command=lambda: temas("grey96", "white", "black"))
    tema.add_radiobutton(label="Modo oscuro",
                         command=lambda: temas("blue4", "navy", "white"))

    menu.add_cascade(label="Ecuaciones", menu=ecuaciones)
    menu.add_cascade(label="Teoremas", menu=teoremas)
    menu.add_command(label="Fracciones", state="disabled")
    menu.add_cascade(label="Configuración", menu=configuracion)

# * Parsear ==================================================


def parsear(expresion, posicion):

    try:
        resultado = eval(expresion)

    except SyntaxError:
        resultado = "Syntaxt error"

    except ValueError:
        resultado = "No se admiten letras"

    except NameError:
        resultado = "No se admiten letras"

    except ZeroDivisionError:
        resultado = "División entre cero"

    except:
        resultado = "Error"

    finally:
        posicion["textvariable"] = tk.StringVar(value=resultado)
        return resultado


if __name__ == "__main__":
    root = tk.Tk()
    Calculadora_normal()
    root.mainloop()
