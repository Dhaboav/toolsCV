from tkinter import Tk, Label, Button, Frame, Toplevel
from tkinter import filedialog, messagebox 


class ChoiceDialog:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.choice = None
        self.input_path = None
        self.create_popup()

    def create_popup(self):
        self.popup = Toplevel(self.root) # Set dialog
        self.popup.title('Label')

        # Set in center
        screen_width = self.popup.winfo_screenwidth()
        screen_height = self.popup.winfo_screenheight()
        x = (screen_width - 200) // 2
        y = (screen_height - 200) // 2
        self.popup.geometry(f"230x180+{x}+{y}")
        self.popup_component(GUI=self.popup)

    def popup_component(self, GUI):
        info = Label(GUI, text="Pilih Operasi Yang ingin dilakukan:")
        info.pack(pady=5)
        choices = ['Cek Label XML', 'Cek Label YOLO', 'Konversi XML ke YOLO', 'Train Rasio SSD Mobilenet']

        # button setting
        button_frame = Frame(GUI)
        button_frame.pack()
        for choice in choices:
            button = Button(button_frame, text=choice, width=25, bg='black', fg='white',command=lambda c=choice: self.button_click(c))
            button.pack(pady=2)  # Add space between buttons

            # Bind mouse enter event for hover effect
            button.bind("<Enter>", lambda event, b=button: b.config(bg='green', fg='white'))

            # Bind mouse leave event for normal state
            button.bind("<Leave>", lambda event, b=button: b.config(bg='black', fg='white'))

    def button_click(self, choice):
        self.choice = choice
        if choice:
            self.get_folder_path()
        self.popup.destroy()

    def get_folder_path(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.input_path = folder_path
        else:
            messagebox.showerror('Error', 'Masukan folder input!')
            exit() 


