import customtkinter as ctk
import tkinter as tk
import time
from PIL import Image, ImageTk

# Appearance Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Custom Colors
BG_COLOR = "#000000"
INPUT_FIELD_COLOR = "#333333"
BUTTON_COLOR = "#3A7AFE"
HOVER_COLOR = "#4A8CFF"
ACCENT_COLOR = "#FF5555"

# === Create Splash Window ===
splash = ctk.CTk()
splash.geometry("900x700")
splash.configure(fg_color=BG_COLOR)
splash.overrideredirect(True)
splash.resizable(False, False)

# === Center Content ===
frame = ctk.CTkFrame(splash, fg_color=BG_COLOR)
frame.pack(expand=True)

# === Title Label (centered & wrapped) ===
title_text = (
    "AI for the Voiceless:\n"
    "A Facial and Gestural-Based Emotion and Depression Analysis System\n"
    "for the Welfare of Deaf-Mute Individuals in Society."
)

title_label = ctk.CTkLabel(
    frame,
    text=title_text,
    font=("Helvetica", 20, "bold"),
    text_color=BUTTON_COLOR,
    wraplength=750,
    justify="center"
)
title_label.pack(pady=(80, 40))

# === (Optional) Logo Image ===
# logo_img = Image.open("logo.png")  # Add your logo path here
# logo_img = logo_img.resize((120, 120))
# logo = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(logo_img), text="")
# logo.pack(pady=(0, 20))

# === Progress Text or Loading Indicator ===
progress_label = ctk.CTkLabel(
    frame,
    text="Loading modules...",
    font=("Helvetica", 14),
    text_color="#888888"
)
progress_label.pack()

# === Splash Close Delay ===
def launch_main_app():
    splash.destroy()
    # Import or launch your main GUI here
    # import main_app
    # main_app.run()
    print("Main app would launch here.")

 # Show splash for 3 seconds
