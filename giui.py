import customtkinter as ctk
from main import main_download


def MyApp():
    # Wybór motywu
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Tworzenie okna głównego
    root = ctk.CTk()

    # Deklarowanie ustawień okna głównego
    root.geometry('600x400')
    root.title("Moja aplikacja")

    # Okno na link_frame oraz options_frame
    liopt_frame = ctk.CTkFrame(root)

    # Okno z linkiem
    link_frame = ctk.CTkFrame(liopt_frame)
    ctk.CTkLabel(link_frame, text="Link").grid(row=0, column=0, padx=10)
    link = ctk.StringVar(root)
    ctk.CTkEntry(link_frame, textvariable=link).grid(row=0, column=1, padx=10, pady=5)
    ctk.CTkLabel(link_frame, text="Check number of offerts").grid(row=1, column=0, padx=10)
    ctk.CTkEntry(link_frame).grid(row=1, column=1, padx=10, pady=5)
    # offerts_number = ctk.StringVar(root)
    ctk.CTkLabel(link_frame, text="Select file saving destination").grid(row=2, column=0, padx=10)
    saving_destination = ""
    def set_dest():
        saving_destination = ctk.filedialog.askdirectory()
        ctk.CTkLabel(link_frame, text="File will be saved at:").grid(row=3, columnspan=2, pady=10)
        ctk.CTkLabel(link_frame, text=saving_destination).grid(row=4, columnspan=2, pady=10)
    
    ctk.CTkButton(link_frame, text="Select", command=set_dest).grid(row=2, column=1, padx=10, pady=5)

    # Okno z opcjami pobrania
    options_frame = ctk.CTkFrame(liopt_frame)
    opt_title = ctk.BooleanVar(root)
    ctk.CTkCheckBox(options_frame, text=" Title", variable=opt_title).pack(padx=20, pady=5)
    opt_level = ctk.BooleanVar(root)
    ctk.CTkCheckBox(options_frame, text=" Level", variable=opt_level).pack(padx=20, pady=5)
    opt_pay = ctk.BooleanVar(root)
    ctk.CTkCheckBox(options_frame, text=" Pay", state="disabled", variable=opt_pay).pack(padx=20, pady=5)
    opt_requiments = ctk.BooleanVar(root)
    ctk.CTkCheckBox(options_frame, text=" Requiments", state="disabled", variable=opt_requiments).pack(padx=20, pady=5)
    opt_company = ctk.BooleanVar(root)
    ctk.CTkCheckBox(options_frame, text=" Company", variable=opt_company).pack(padx=20, pady=5)

    def process():
        main_download(link.get(), opt_title.get(), opt_level.get(), opt_pay.get(), opt_requiments.get(), opt_company.get(), saving_destination)
        ctk.CTkLabel(bottom_frame, text="").pack(pady=5)


    # Okno progresu oraz przycisku startu
    progress_frame = ctk.CTkFrame(root, height=100)
    ctk.CTkProgressBar(progress_frame, progress_color="red", width=400).pack(side="left", padx=20, pady=20)
    ctk.CTkButton(progress_frame, text="Start", command=process).pack(side="right", padx=20, pady=20)


    # Okno dolne informacji
    bottom_frame = ctk.CTkFrame(root)
    bottom_text = ctk.StringVar(root)
    ctk.CTkLabel(bottom_frame, text=saving_destination).pack()


    # Budowanie elementów aplikacji
    liopt_frame.pack(fill="x")
    link_frame.pack(side="left", expand=True, padx=30, pady=30)
    options_frame.pack(side="left", expand=True, padx=30, pady=30)
    progress_frame.pack(fill="x")
    bottom_frame.pack(fill="x")

    root.mainloop()

if __name__ == "__main__":
    MyApp()
    