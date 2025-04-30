import tkinter as tk
from tkinter import filedialog, messagebox, Menu, scrolledtext

class editor_texto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('Editor de Texto - Hecho por: Farita')
        self.resizable(0, 0)
        self.iconbitmap('icono.ico')
        
        self._archivo_abierto = None
        self._creacion_componentes()
        self._crear_menu()


    def _creacion_componentes(self):
        scroll_frame = tk.Frame(self, width=650, height=600, bg='#495057')
        scroll_frame.grid(row=0, column=1, sticky='nsew')
        
        self.scroll = scrolledtext.ScrolledText(scroll_frame, width=650, height=600)
        self.scroll.insert(tk.INSERT, 'Hola')
        
        self.scroll.grid(row=0, column=0)
        
        opciones_frame = tk.Frame(self, width=150, height=600, bg='#6c757d')
        opciones_frame.grid(row=0, column=0, ipadx=2, sticky='ns')
        opciones_frame.grid_propagate(False)
        
        boton_abrir = tk.Button(opciones_frame, text='Abrir', width=16, command=self._abrir)
        boton_abrir.grid(row=0, column=0, padx=20, pady=5)
        
        boton_guardar = tk.Button(opciones_frame, text='Guardar', width=16, command=self._guardar)
        boton_guardar.grid(row=1, column=0, padx=20, pady=5)
        
        boton_guardar_como = tk.Button(opciones_frame, text='Guardar Como', width=16, command=self._guardar_como)
        boton_guardar_como.grid(row=2, column=0, padx=20, pady=5)

    def _crear_menu(self):
        menu_principal = Menu(self)
        submenu_archivo = Menu(menu_principal, tearoff=0)
        submenu_archivo.add_command(label='Abrir', command=self._abrir)
        menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label='Guardar', command=self._guardar)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label='Guardar como', command=self._guardar_como)
        self.config(menu=menu_principal)


    def _abrir(self):
        archivo = filedialog.askopenfilename(
            title= 'Seleccione un archivo de texto',
            filetypes=[('Archivos de texto', '*.txt')]
        )
        if archivo:
            print(f'Archivo seleccionado: {archivo}')
            with open(archivo, 'r', encoding='utf-8') as file:
                contenido = file.read()
                self.scroll.delete(1.0, tk.END)
                self.scroll.insert(tk.INSERT, contenido)
                self.archivo_abierto = archivo
        else:
            messagebox.showinfo('Sin archivo', 'No se seleccionó ningún archivo.')

    def _guardar(self):
        if self.archivo_abierto:
            with open(self.archivo_abierto, 'w', encoding='utf-8') as file: 
                contenido = self.scroll.get(1.0, tk.END)
                file.write(contenido)
            messagebox.showinfo('Guardado', f'Archivo guardado en {self.archivo_abierto}')
        else:
            self._guardar_como()

    def _guardar_como(self):
        archivo = filedialog.asksaveasfilename(
            title='Guardar archivo como',
            defaultextension='.txt',
            filetypes=[('archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if archivo:
            with open(archivo, 'w', encoding='utf-8') as file:
                contenido = self.scroll.get(1.0, tk.END)
                file.write(contenido)
            self.archivo_abierto = archivo
            messagebox.showinfo('Guardado', f'Archivo guardado en: {archivo}')
        else:
            messagebox.showinfo('No se guardó', 'No se seleccionó un archivo a guardar')


if __name__ == '__main__':
    editor = editor_texto()
    editor.mainloop()
