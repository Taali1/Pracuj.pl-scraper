import customtkinter as ctk


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
    offerts_number = f"Number of offerts: {2141}"
    ctk.CTkLabel(link_frame, text = offerts_number).grid(row=2, columnspan=2, pady=20)

    # Okno z opcjami pobrania
    options_frame = ctk.CTkFrame(liopt_frame)
    ctk.CTkCheckBox(options_frame, text=" Title").pack(padx=20, pady=5)
    ctk.CTkCheckBox(options_frame, text=" Level").pack(padx=20, pady=5)
    ctk.CTkCheckBox(options_frame, text=" Pay", state="disabled").pack(padx=20, pady=5)
    ctk.CTkCheckBox(options_frame, text=" Requiments", state="disabled").pack(padx=20, pady=5)
    ctk.CTkCheckBox(options_frame, text=" Company").pack(padx=20, pady=5)

    # Okno progresu oraz przycisku startu
    progress_frame = ctk.CTkFrame(root, height=100)
    ctk.CTkProgressBar(progress_frame, progress_color="red", width=400).pack(side="left", padx=20, pady=20)
    ctk.CTkButton(progress_frame, text="Start").pack(side="right", padx=20, pady=20)


    # Okno dolne informacji
    bottom_frame = ctk.CTkFrame(root, width=600, height=100)

    # Budowanie elementów aplikacji
    liopt_frame.pack(fill="x")
    link_frame.pack(side="left", expand=True, padx=30, pady=30)
    options_frame.pack(side="left", expand=True, padx=30, pady=30)
    progress_frame.pack(fill="x")
    bottom_frame.pack(fill="x")

    root.mainloop()


if __name__ == "__main__":
    MyApp()