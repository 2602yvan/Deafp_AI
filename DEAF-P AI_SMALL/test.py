# <editor-fold desc="Imports">
import os
from math import cos , sin , pi
from tkinter import filedialog
import threading
import time
import customtkinter as ctk
import tkinter as tk
import cv2
import joblib
from PIL import Image, ImageTk


from ML import Classification as classification
from ML import Preprocessing as prep
from ML import generate_emotion_sentence as ge

# </editor-fold>
model = joblib.load("D:/UTILITAIRE POUR TRAVAIL/PROJECT/PythonProject/NLP_TEST/DEAF-P AI_SMALL/ML/knn_model.joblib")
le = joblib.load("D:/UTILITAIRE POUR TRAVAIL/PROJECT/PythonProject/NLP_TEST/DEAF-P AI_SMALL/ML/label_encoder.joblib")

# <editor-fold desc="Configuration">
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG_COLOR = "#000000"
INPUT_FIELD_COLOR = "#333333"
BUTTON_COLOR = "#3A7AFE"
HOVER_COLOR = "#4A8CFF"
ACCENT_COLOR = "#FF5555"

cap = None
playing_placeholder = True
# Define the iPhone-like font
FONT_REGULAR = ("Helvetica", 14)
FONT_BOLD = ("Helvetica", 16, "bold")
FONT_TITLE = ("Helvetica", 18, "bold")
FONT_LARGE_EMOJI = ("Helvetica", 24, "bold")
FONT_FOOTER = ("Helvetica", 12)

# </editor-fold>


# <editor-fold desc="GUI management">
def upload_video():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])

    if file_path:


        def process_video():
            try:
                # === Step 1: Extract Features ===
                start_time = time.time()
                features = prep.process_video_to_features(file_path)
                print(f"Feature extraction time: {time.time() - start_time:.2f}s")

                # === Step 2: Predict Class ===
                start_time = time.time()
                pred_idx = model.predict([features])[0]
                print(f"Prediction time: {time.time() - start_time:.2f}s")
                pred_label = le.inverse_transform([pred_idx])[0]
                print(pred_label)

                # === Step 3: Emotion Analysis ===
                start_time = time.time()
                emotion = classification.analyze_emotions_from_video(file_path)

                print(f"Emotion analysis time: {time.time() - start_time:.2f}s")

                # === Step 4: Get Final Text ===


                # === Step 5: Update GUI in Main Thread ===


            except Exception as e:
                print("Error during video processing:", e)


        # Start thread
        threading.Thread(target=process_video).start()

def generate_action():
    text_box.delete("1.0", "end")
    text_box.insert("1.0", "Processing video... \n\n[Generated text will appear here.]")
def update_frame():
    global cap, playing_placeholder

    if not cap or not cap.isOpened():
        return
    ret, frame = cap.read()
    if not ret:
        if playing_placeholder:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        else:
            return




    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = prep.resize_and_pad(img, (500, 400))
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(30, update_frame)
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
def speak_output():
    text = text_box.get("1.0", "end").strip()
    ge.speak_it(text)
    print("works")


# </editor-fold>

# <editor-fold desc="Main Window">
root = ctk.CTk()
root.geometry("900x800")
root.overrideredirect(True)
root.resizable(False, False)
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
    text="DEAF-P AI",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="white"
)
top_bar_title.pack(side="left", padx=15, pady=5)

close_button = ctk.CTkButton(
    top_bar,
    text="X",
    command=on_closing,
    width=30, height=30,
    fg_color="transparent",
    text_color="white",
    hover_color=ACCENT_COLOR,
    font=ctk.CTkFont(size=16, weight="bold")
)
close_button.pack(side="right", padx=5, pady=5)


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

# <editor-fold desc="Main Frame">
main_frame = ctk.CTkFrame(content_area, fg_color=BG_COLOR)

title_label = ctk.CTkLabel(
    main_frame,
    text="Everyone deserves to be understood 😇",
    font=ctk.CTkFont(family="Helvetica Neue", size=24, weight="bold"),
    text_color="white"
)
title_label.pack(pady=20)

video_frame = ctk.CTkFrame(
    main_frame,
    width=500, height=400,
    fg_color=INPUT_FIELD_COLOR,
    corner_radius=15
)
video_frame.pack(pady=10)
video_frame.pack_propagate(False)

video_label = ctk.CTkLabel(video_frame, text="")
video_label.pack(fill="both", expand=True)


cap = cv2.VideoCapture(
    "D:/UTILITAIRE POUR TRAVAIL/PROJECT/PythonProject/NLP_TEST/DEAF-P AI_SMALL/Screen/placeholder4.mp4")

update_frame()

upload_button = ctk.CTkButton(
    main_frame,
    text="Upload Video",
    command=upload_video,
    width=180, height=45,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    font=ctk.CTkFont(size=15, weight="bold")
)
upload_button.pack(pady=15)

text_output_container = ctk.CTkFrame(
    main_frame, height=150,
    fg_color=INPUT_FIELD_COLOR,
    corner_radius=15
)
text_output_container.pack(fill="x", padx=20, pady=(10, 20))
text_output_container.grid_rowconfigure(0, weight=1)
text_output_container.grid_columnconfigure(0, weight=1)

text_box = ctk.CTkTextbox(
    text_output_container, height=120,
    fg_color=INPUT_FIELD_COLOR,
    text_color="white",
    font=ctk.CTkFont(size=14),
    wrap="word",

)
speak_button = ctk.CTkButton(
    text_output_container,
    text="🔊 Speak",
    command=speak_output,
    width=100, height=35,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    font=ctk.CTkFont(size=14, weight="bold")
)
speak_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="se")

text_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
text_box.insert("1.0", "Transcript/Translation Output:\n\nWaiting for input...")
#
# generate_button = ctk.CTkButton(
#     text_output_container,
#     text="Generate",
#     command=generate_action,
#     width=100, height=35,
#     fg_color=BUTTON_COLOR,
#     hover_color=HOVER_COLOR,
#     font=ctk.CTkFont(size=14, weight="bold")
# )
# generate_button.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky="se")
# </editor-fold>

# <editor-fold desc="Speak Frame">
speak_frame = ctk.CTkFrame(content_area, fg_color=BG_COLOR)
speak_label = ctk.CTkLabel(
    speak_frame,
    text="Speak Text Feature Coming Soon!",
    font=ctk.CTkFont(size=20),
    text_color="white"
)
speak_label.pack(pady=200)
# </editor-fold>

# <editor-fold desc="Live Frame">
Live_translation_frame = ctk.CTkFrame(content_area, fg_color="black")
Live_translation_frame.pack(expand=True, fill="both")

container = ctk.CTkFrame(Live_translation_frame, fg_color="black")
container.pack(expand=True, fill="both", pady=30, padx=30)

# === Left View ===
left_view = ctk.CTkFrame(container, fg_color="#1f1f1f", corner_radius=12)
left_view.pack(side="left", expand=True, fill="both", padx=(0, 20), pady=15)

inner_left_view = ctk.CTkFrame(left_view, fg_color="gray25", corner_radius=10)
inner_left_view.place(relx=0.5, rely=0.05, relwidth=0.95, relheight=0.9, anchor="n")

ctk.CTkLabel(inner_left_view, text="Live Video Feed", text_color="#aaaaaa", font=FONT_BOLD).place(relx=0.5, rely=0.5, anchor="center")
ctk.CTkLabel(inner_left_view, text="● LIVE", text_color="red", font=FONT_REGULAR).place(relx=0.05, rely=0.05, anchor="nw")

# === Right View ===
right_view = ctk.CTkFrame(container, fg_color="#1f1f1f", corner_radius=12)
right_view.pack(side="right", expand=True, fill="both", padx=(20, 0), pady=15)

# Top Section
top_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
top_section.place(relx=0.5, rely=0.04, relwidth=0.92, relheight=0.3, anchor="n")

ctk.CTkLabel(top_section, text="Primary Translation", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.1, anchor="n")
ctk.CTkLabel(top_section, text="[Translated Text Appears Here]", text_color="#ffffff", font=FONT_TITLE).place(relx=0.5, rely=0.5, anchor="center")

# Middle Section
middle_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
middle_section.place(relx=0.5, rely=0.36, relwidth=0.92, relheight=0.3, anchor="n")

ctk.CTkLabel(middle_section, text="Emotion", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.1, anchor="n")
ctk.CTkLabel(middle_section, text="[Original Emotion Appears Here]", text_color="#ffffff", font=FONT_REGULAR).place(relx=0.5, rely=0.4, anchor="center")
emotion_label = ctk.CTkLabel(middle_section, text="😊 Happy", text_color="#ffffff", font=FONT_LARGE_EMOJI)
emotion_label.place(relx=0.5, rely=0.75, anchor="center")

# Bottom Section

bottom_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
bottom_section.place(relx=0.5, rely=0.68, relwidth=0.92, relheight=0.3, anchor="n")

ctk.CTkLabel(bottom_section, text="Depression Analysis", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.08, anchor="n")

# Embed a raw tkinter Canvas inside the customtkinter frame
canvas_container = tk.Canvas(bottom_section, width=220, height=120, bg="gray25", highlightthickness=0)
canvas_container.place(relx=0.5, rely=0.55, anchor="center")

def draw_depression_meter(canvas, score=2):
    canvas.delete("all")
    cx, cy = 110, 110
    r = 80
    width = 15
    segments = 300

    for i in range(segments):
        angle_deg = 180 + (i * 180 / segments)
        angle_rad = angle_deg * pi / 180
        x0 = cx + r * cos(angle_rad)
        y0 = cy + r * sin(angle_rad)
        x1 = cx + (r - width) * cos(angle_rad)
        y1 = cy + (r - width) * sin(angle_rad)

        # Gradient from green to red
        t = i / (segments - 1)
        if t < 0.5:
            r_val = int(255 * (2 * t))
            g_val = 255
        else:
            r_val = 255
            g_val = int(255 * (2 - 2 * t))
        color = f"#{r_val:02x}{g_val:02x}00"

        canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

    angle_step = pi / 4
    angle = pi + score * angle_step
    pointer_len = r - width - 5
    px = cx + pointer_len * cos(angle)
    py = cy + pointer_len * sin(angle)
    canvas.create_line(cx, cy, px, py, fill="white", width=4)
    canvas.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill="white", outline="gray")

# Draw once with default score (e.g., 2)
draw_depression_meter(canvas_container, score=2)


# Footer
footer_label = ctk.CTkLabel(Live_translation_frame, text="Tip: Ensure good lighting for better recognition 🔆", text_color="#666666", font=FONT_FOOTER)
footer_label.pack(side="bottom", pady=5)
# </editor-fold>

# <editor-fold desc="Initialize & Mainloop">
show_frame(main_frame)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
# </editor-fold>
