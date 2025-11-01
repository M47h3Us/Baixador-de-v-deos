import tkinter as tk

root = tk.Tk()

var = tk.BooleanVar()  # True ou False

check = tk.Checkbutton(root, text="Marque aqui", variable=var)
check.pack()

# Para pegar o valor:
def mostrar_valor():
    print(var.get())

botao = tk.Button(root, text="Mostrar valor", command=mostrar_valor)
botao.pack()

root.mainloop()