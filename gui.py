# import customtkinter

# # Theme
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# root = customtkinter.CTk()
# root.geometry("500x360")
# # root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')


# def submit():
#     print("Test Submit")


# def login():
#     print("Login")
#     filename = customtkinter.filedialog.askopenfilename(
#         initialdir="~/", title="Select a File", filetypes=[('image files', ('.png', 'jpg', 'jpeg'))])
#     print(filename)
#     # label_file_explorer.configure(text="File Opened: "+filename)


# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# label = customtkinter.CTkLabel(
#     master=frame, text="Encryption & decryption", font=("SF Pro", 24))
# label.pack(pady=12, padx=10)

# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)
# entry2 = customtkinter.CTkEntry(
#     master=frame, placeholder_text="Passowrd", show="*")
# entry2.pack(pady=12, padx=10)
# button = customtkinter.CTkButton(master=frame, text="login", command=login)
# button.pack(pady=12, padx=10)

# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)

# root.mainloop()

import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Encrypt and decrypt your images")
        self.geometry(f"{1100}x{580}")
        self.tabview = customtkinter.CTkTabview(self, width=1060, height=540)
        self.tabview.grid(row=0, column=0, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Encrypt")
        self.tabview.add("Decrypt")
        self.logo_label = customtkinter.CTkLabel(
            self.tabview.tab("Encrypt"), text="Image uploaded", font=customtkinter.CTkFont(family='SF Pro', size=12))
        self.logo_label.grid(row=0, column=0, padx=(
            10, 10), pady=0, sticky="NSW")
        self.logo_label.columnconfigure(0, minsize="300")
        self.deImage = customtkinter.CTkImage(
            dark_image=Image.open("./table.png"), size=(200, 200))
        self.disimg = customtkinter.CTkLabel(
            self, text="", height=200, width=200, image=self.deImage)
        self.disimg.grid(row=1, column=0, padx=(10, 10), pady=0, sticky="NSW")
        self.disimg.place(anchor=tkinter.CENTER, relx=.5, rely=.2)
        # my_image = customtkinter.CTkImage(dark_image=Image.open("~/Pictures/Wallpapers/table.png"),
        #                                   size=(30, 30))
        # originalimageplacehilder = customtkinter.CTkButton(
        #     self, image=my_image)
        # originalimageplacehilder.grid(
        #     row=0, column=0, padx=0, pady=0, sticky="NSEW")

        # self.logo_label2 = customtkinter.CTkLabel(
        # self.tabview.tab("Encrypt"), text="HELLO2", font=customtkinter.CTkFont(family='SF Pro', size=12))
        # self.logo_label2.grid(row=0, column=1, padx=20, pady=0, sticky="NSEW")
        self.getImageButton = customtkinter.CTkButton(
            self.tabview.tab('Encrypt'), text="Select Image", command=self.getImage, anchor=tkinter.CENTER)
        self.getImageButton.grid(row=0, column=1, pady=0,
                                 padx=(10, 10), sticky="NSE")
        self.getImageButton.columnconfigure(0, minsize="300")
        self.logo_label3 = customtkinter.CTkLabel(
            self.tabview.tab("Encrypt"), text="Encrypted image", font=customtkinter.CTkFont(family='SF Pro', size=12))
        self.logo_label3.grid(
            row=0, column=2, padx=(10, 10), pady=0, sticky="E")
        self.logo_label3.columnconfigure(0, minsize="300")
        # # configure grid layout (4x4)
        # # self.grid_columnconfigure(1, weight=1)
        # # self.grid_columnconfigure((2, 3), weight=0)
        # # self.grid_rowconfigure((0, 1, 2), weight=1)
        # # create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=1060)
        # self.tabview.grid(row=0, column=0, padx=(
        #     20, 20), pady=(20, 20), sticky="nsew")
        # self.tabview.add("Encrypt")
        # self.tabview.add("Decrypt")
        # self.tabview.tab("Encrypt").grid_columnconfigure(
        #     0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Decrypt").grid_columnconfigure(0, weight=1)
        # self.tabview.tab("Encrypt").grid(
        #     row=0, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        # self.logo_label = customtkinter.CTkLabel(
        #     self.tabview.tab("Encrypt"), text="HELLO", font=customtkinter.CTkFont(size=12))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.logo_label = customtkinter.CTkLabel(
        #     self.tabview.tab("Encrypt"), text="HELLO", font=customtkinter.CTkFont(size=12))
        # self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))
        # self.logo_label = customtkinter.CTkLabel(
        #     self.tabview.tab("Encrypt"), text="HELLO", font=customtkinter.CTkFont(size=12))
        # self.logo_label.grid(row=0, column=2, padx=20, pady=(20, 10))
        # # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Encrypt"), dynamic_resizing=False,
        # #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Encrypt"),
        # #                                             values=["Value 1", "Value 2", "Value Long....."])
        # # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Decrypt"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Decrypt"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))

    def getImage(self):
        filename = customtkinter.filedialog.askopenfilename(
            initialdir="~/Pictures/Wallpapers/", title="Select a File", filetypes=[('image files', ('.png', 'jpg', 'jpeg'))])
        deImage = customtkinter.CTkImage(
            dark_image=Image.open(filename), size=(200, 200))
        self.disimg.configure(image=deImage)


if __name__ == "__main__":
    app = App()
    app.mainloop()
