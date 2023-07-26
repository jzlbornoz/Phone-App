import tkinter as tk
 
 # Programa Telefono Celular 
 # Alumno Javier Albornoz 30372851

def on_alphanumeric_key_press(key):
    print("Presionaste la tecla #", key)

def on_asterisk_press():
    print("Presionaste la tecla del asterisco (*)")

def on_call_press():
    print("Iniciando llamada...")

def on_end_call_press():
    print("Terminando llamada...")

def on_clear_press():
    print("Limpiando la pantalla...")

def on_lock_press():
    print("El teclado esta bloqueado...")

def on_navigation_press(direction):
    print("Movimiento:", direction)

def create_key_button(root, text, command, row, column, columnspan=1):
    return tk.Button(root, text=text, width=10, height=3, command=command).grid(row=row, column=column, columnspan=columnspan)

def create_navigation_buttons(root):
    create_key_button(root, "↑", lambda: on_navigation_press("Arriba ↑"), 1, 2)
    create_key_button(root, "←", lambda: on_navigation_press("Izquierda ←"), 2, 1)
    create_key_button(root, "OK", lambda: on_navigation_press("OK (Seleccion)"), 2, 2)
    create_key_button(root, "→", lambda: on_navigation_press("Derecha →"), 2, 3)
    create_key_button(root, "↓", lambda: on_navigation_press("Abajo ↓"), 3, 2)

def create_keypad(root):
    create_navigation_buttons(root)
    create_key_button(root, "1", lambda: on_alphanumeric_key_press(1), 4, 1)
    create_key_button(root, "2", lambda: on_alphanumeric_key_press(2), 4, 2)
    create_key_button(root, "3", lambda: on_alphanumeric_key_press(3), 4, 3)
    create_key_button(root, "4", lambda: on_alphanumeric_key_press(4), 5, 1)
    create_key_button(root, "5", lambda: on_alphanumeric_key_press(5), 5, 2)
    create_key_button(root, "6", lambda: on_alphanumeric_key_press(6), 5, 3)
    create_key_button(root, "7", lambda: on_alphanumeric_key_press(7), 6, 1)
    create_key_button(root, "8", lambda: on_alphanumeric_key_press(8), 6, 2)
    create_key_button(root, "9", lambda: on_alphanumeric_key_press(9), 6, 3)
    create_key_button(root, "*", on_asterisk_press, 7, 1)
    create_key_button(root, "0", lambda: on_alphanumeric_key_press(0), 7, 2)
    create_key_button(root, "#", lambda: on_alphanumeric_key_press(""), 7, 3)
    create_key_button(root, "Llamar", on_call_press, 8, 1, 2)
    create_key_button(root, "Colgar", on_end_call_press, 8, 3)
    create_key_button(root, "Limp", on_clear_press, 9, 1, 2)
    create_key_button(root, "Bloq", on_lock_press, 9, 3)

def main():
    root = tk.Tk()
    root.title("Teclado de celular")
    
    create_keypad(root)

    root.mainloop()

if __name__ == "__main__":
    main()
