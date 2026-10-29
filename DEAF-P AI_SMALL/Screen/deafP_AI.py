import threading

# <editor-fold desc="Imports">


import customtkinter as ctk


from menu_screen import create_main_frame, create_speak_frame, create_live_translation_frame


# </editor-fold>


# <editor-fold desc="Configuration">
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG_COLOR = "#000000"
INPUT_FIELD_COLOR = "#333333"
BUTTON_COLOR = "#3A7AFE"
HOVER_COLOR = "#4A8CFF"
ACCENT_COLOR = "#FF5555"

cap = None

# Define the iPhone-like font
FONT_REGULAR = ("Helvetica", 14)
FONT_BOLD = ("Helvetica", 16, "bold")
FONT_TITLE = ("Helvetica", 18, "bold")
FONT_LARGE_EMOJI = ("Helvetica", 24, "bold")
FONT_FOOTER = ("Helvetica", 12)

# </editor-fold>


# <editor-fold desc="GUI management">

def on_closing():
    if cap and cap.isOpened():
        cap.release()
    root.destroy()
def show_frame(frame):
    for f in [main_frame, speak_frame, Live_translation_frame]:
        f.pack_forget()
    frame.pack(fill="both", expand=True)
def toggle_menu():
    if side_menu.winfo_ismapped():
        side_menu.pack_forget()
        menu_button.configure(text="☰ Menu")
    else:
        side_menu.pack(side="left", fill="y")
        menu_button.configure(text="✕ Close")

# </editor-fold>

# <editor-fold desc="Main Window">
root = ctk.CTk()
root.geometry("900x850")
# root.overrideredirect(True)
# root.resizable(False, False)
  # 0 (fully transparent) to 1 (fully opaque)


# </editor-fold>

# <editor-fold desc="Top Bar">
top_bar = ctk.CTkFrame(root, height=40, corner_radius=0, fg_color=BG_COLOR)
top_bar.pack(side="top", fill="x")

menu_button = ctk.CTkButton(
    top_bar,
    text="☰ Menu",
    command=toggle_menu,
    width=80, height=30,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    font=ctk.CTkFont(size=13, weight="bold")
)
menu_button.pack(side="left", padx=(5, 0))

top_bar_title = ctk.CTkLabel(
    top_bar,
    text="",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="white"
)
top_bar_title.pack(side="left", padx=15, pady=5)



# </editor-fold>

# <editor-fold desc="Top Bar Dragging Support">
def start_move(event):
    root._drag_start_x = event.x
    root._drag_start_y = event.y


def do_move(event):
    x = root.winfo_pointerx() - root._drag_start_x
    y = root.winfo_pointery() - root._drag_start_y
    root.geometry(f"+{x}+{y}")


top_bar.bind("<Button-1>", start_move)
top_bar.bind("<B1-Motion>", do_move)
# </editor-fold>

# <editor-fold desc="Main Container">
main_container = ctk.CTkFrame(root, fg_color=BG_COLOR)
main_container.pack(fill="both", expand=True)
# </editor-fold>

# <editor-fold desc="Side Menu">
side_menu = ctk.CTkFrame(main_container, width=120, fg_color=INPUT_FIELD_COLOR)

btn_main = ctk.CTkButton(
    side_menu,
    text="Main",
    command=lambda: show_frame(main_frame),
    fg_color="transparent",
    hover_color=HOVER_COLOR,
    text_color="white",
    font=ctk.CTkFont(family="Helvetica Neue", size=16, weight="bold")
)
btn_main.pack(fill="x", pady=(10, 0), padx=10)

btn_speak = ctk.CTkButton(
    side_menu,
    text="Speak",
    command=lambda: show_frame(speak_frame),
    fg_color="transparent",
    hover_color=HOVER_COLOR,
    text_color="white",
    font=ctk.CTkFont(family="Helvetica Neue", size=16, weight="bold")
)
btn_speak.pack(fill="x", pady=(10, 0), padx=10)

btn_live = ctk.CTkButton(
    side_menu,
    text="Live Translation",
    command=lambda: show_frame(Live_translation_frame),
    fg_color="transparent",
    hover_color=HOVER_COLOR,
    text_color="white",
    font=ctk.CTkFont(family="Helvetica Neue", size=16, weight="bold")
)
btn_live.pack(fill="x", pady=(10, 0), padx=10)

side_menu.pack_forget()
# </editor-fold>

# <editor-fold desc="Main Content Area">
content_area = ctk.CTkFrame(main_container, fg_color=BG_COLOR)
content_area.pack(side="right", fill="both", expand=True)
# </editor-fold>

main_frame = create_main_frame(content_area)
speak_frame = create_speak_frame(content_area)
Live_translation_frame = create_live_translation_frame(content_area)

# <editor-fold desc="Initialize & Mainloop">

show_frame(main_frame)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

# </editor-fold>
