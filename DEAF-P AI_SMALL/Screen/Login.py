import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence

# <editor-fold desc="CONFIGURATION">
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG_COLOR = "#000000"
INPUT_FIELD_COLOR = "#000000"
BUTTON_COLOR = "#3A7AFE"
HOVER_COLOR = "#4A8CFF"
ACCENT_COLOR = "#FF5555"
PANEL_DARKGRAY = "#333333"
PANEL_BLACK = "#000000"
# </editor-fold>

# <editor-fold desc="FUNCTIONS">
def on_closing():
    root.destroy()

def start_move(event):
    root._drag_start_x = event.x
    root._drag_start_y = event.y

def do_move(event):
    x = root.winfo_pointerx() - root._drag_start_x
    y = root.winfo_pointery() - root._drag_start_y
    root.geometry(f"+{x}+{y}")

def login_action():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Login attempt: {username}/{password}")

def resize_and_pad(image, target_size):
    """Resize while maintaining aspect ratio and pad to target size."""
    original_width, original_height = image.size
    target_width, target_height = target_size
    ratio = min(target_width / original_width, target_height / original_height)
    new_size = (int(original_width * ratio), int(original_height * ratio))
    resized = image.resize(new_size, Image.LANCZOS)
    new_image = Image.new("RGB", target_size, (0, 0, 0))
    paste_x = (target_width - new_size[0]) // 2
    paste_y = (target_height - new_size[1]) // 2
    new_image.paste(resized, (paste_x, paste_y))
    return new_image

def update_gif(frame_idx):
    frame = gif_frames[frame_idx]
    video_label.configure(image=frame)
    next_frame = (frame_idx + 1) % len(gif_frames)
    root.after(gif_delay, update_gif, next_frame)
# </editor-fold>

# <editor-fold desc="MAIN WINDOW">
root = ctk.CTk()
root.geometry("900x800")
root.overrideredirect(True)
root.resizable(False, False)
# </editor-fold>

# <editor-fold desc="TOP BAR">
top_bar = ctk.CTkFrame(root, height=40, corner_radius=0, fg_color=BG_COLOR)
top_bar.pack(side="top", fill="x")

top_bar_title = ctk.CTkLabel(
    top_bar,
    text="DEAF-P AI Login",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="white"
)
top_bar_title.pack(side="left", padx=15, pady=5)

close_button = ctk.CTkButton(
    top_bar,
    text="X",
    command=on_closing,
    width=30,
    height=30,
    fg_color="transparent",
    text_color="white",
    hover_color=ACCENT_COLOR,
    font=ctk.CTkFont(size=16, weight="bold")
)
close_button.pack(side="right", padx=5, pady=5)

top_bar.bind("<Button-1>", start_move)
top_bar.bind("<B1-Motion>", do_move)
# </editor-fold>

# <editor-fold desc="MAIN FLEX CONTAINER">
container = ctk.CTkFrame(root, fg_color=BG_COLOR)
container.pack(fill="both", expand=True)
# </editor-fold>

# <editor-fold desc="LEFT PANEL (Login Form)">
left_panel = ctk.CTkFrame(container, fg_color=PANEL_DARKGRAY, width=450)
left_panel.pack(side="left", fill="both", expand=True)

form_frame = ctk.CTkFrame(left_panel, fg_color=PANEL_DARKGRAY)
form_frame.place(relx=0.5, rely=0.5, anchor="center")

sign_label = ctk.CTkLabel(
    form_frame,
    text="Sign in",
    font=ctk.CTkFont(family="Helvetica Neue", size=28, weight="bold"),
    text_color="white"
)
sign_label.pack(pady=(0, 30))

username_entry = ctk.CTkEntry(
    form_frame,
    placeholder_text="Username",
    fg_color=INPUT_FIELD_COLOR,
    border_width=2,
    border_color="#000000",
    corner_radius=8,
    text_color="white",
    font=ctk.CTkFont(size=16),
    width=300
)
username_entry.pack(ipady=8, pady=(0, 20))

password_entry = ctk.CTkEntry(
    form_frame,
    placeholder_text="Password",
    fg_color=INPUT_FIELD_COLOR,
    border_width=2,
    border_color="#000000",
    corner_radius=8,
    show="*",
    text_color="white",
    font=ctk.CTkFont(size=16),
    width=300
)
password_entry.pack(ipady=8, pady=(0, 30))

login_button = ctk.CTkButton(
    form_frame,
    text="Login",
    command=login_action,
    width=300,
    height=45,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    font=ctk.CTkFont(size=16, weight="bold")
)
login_button.pack(pady=(0, 15))

cancel_button = ctk.CTkButton(
    form_frame,
    text="Cancel",
    command=on_closing,
    width=300,
    height=45,
    fg_color="transparent",
    border_width=2,
    border_color=ACCENT_COLOR,
    text_color=ACCENT_COLOR,
    hover_color=ACCENT_COLOR,
    font=ctk.CTkFont(size=16, weight="bold")
)
cancel_button.pack()
# </editor-fold>

# <editor-fold desc="RIGHT PANEL (GIF Background)">
right_panel = ctk.CTkFrame(container, fg_color=PANEL_BLACK, width=450)
right_panel.pack(side="left", fill="both", expand=True)

video_label = ctk.CTkLabel(right_panel, text="")
video_label.place(relx=0.5, rely=0.5, anchor="center")

title_label = ctk.CTkLabel(
    right_panel,
    text="DEAF-P AI",
    font=ctk.CTkFont(family="Helvetica Neue", size=28, weight="bold"),
    text_color="white",
    bg_color="transparent"
)
title_label.place(relx=0.5, rely=0.9, anchor="s")

gif = Image.open("placeholder6.gif")
gif_frames = []
gif_delay = gif.info.get("duration", 100)

for frame in ImageSequence.Iterator(gif):
    resized_padded = resize_and_pad(frame.copy().convert("RGB"), (400, 500))
    gif_frames.append(ImageTk.PhotoImage(resized_padded))

update_gif(0)
# </editor-fold>

# <editor-fold desc="MAIN LOOP">
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
# </editor-fold>
