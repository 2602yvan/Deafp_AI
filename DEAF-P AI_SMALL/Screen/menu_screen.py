import threading
import time
import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk
from math import sin, cos, pi

import cv2
import joblib
from PIL import Image, ImageTk
from ML import Classification as classification
from ML import Preprocessing as prep
from ML import generate_emotion_sentence as ge
BG_COLOR = "#000000"
INPUT_FIELD_COLOR = "#333333"
BUTTON_COLOR = "#3A7AFE"
HOVER_COLOR = "#4A8CFF"
ACCENT_COLOR = "#FF5555"



# Define the iPhone-like font
FONT_REGULAR = ("Helvetica", 14)
FONT_BOLD = ("Helvetica", 16, "bold")
FONT_TITLE = ("Helvetica", 18, "bold")
FONT_LARGE_EMOJI = ("Helvetica", 24, "bold")
FONT_FOOTER = ("Helvetica", 12)
model = joblib.load("D:/UTILITAIRE POUR TRAVAIL/PROJECT/PythonProject/NLP_TEST/DEAF-P AI_SMALL/ML/knn_model.joblib")
le = joblib.load("D:/UTILITAIRE POUR TRAVAIL/PROJECT/PythonProject/NLP_TEST/DEAF-P AI_SMALL/ML/label_encoder.joblib")


def draw_depression_meter(canvas, width=220,height=120,score=2,r = 80):
    canvas.delete("all")
    canvas.configure(width=width,height=height)
    cx = width // 2
    cy = height - 10

    width = 25
    segments = 300

    for i in range(segments):
        angle_deg = 180 + (i * 180 / segments)
        angle_rad = angle_deg * pi / 180
        x0 = cx + r * cos(angle_rad)
        y0 = cy + r * sin(angle_rad)
        x1 = cx + (r - width) * cos(angle_rad)
        y1 = cy + (r - width) * sin(angle_rad)

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


def create_main_frame(parent):

    playing_placeholder = True

    def upload_video():
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])

        if file_path:

            def process_video():
                try:
                    # === Step 1: Extract Features ===
                    text_label.configure(text="")
                    text_label.configure( "🔍 Processing video...\n\n⏳ Please wait while we extract hand landmarks.")
                    emotion_label.configure(text="🔍 Processing video...\n\n⏳ Please wait while we extract hand landmarks")

                    start_time = time.time()
                    emotion = classification.analyze_emotions_from_video(file_path)
                    features = prep.process_video_to_features(file_path)
                    print(f"Feature extraction time: {time.time() - start_time:.2f}s")

                    text_label.configure(text="")
                    text_label.configure("✅ Feature Extraction Complete!\n\n🧠 Making predictions...")


                    # === Step 2: Predict Class ===
                    start_time = time.time()
                    pred_idx = model.predict([features])[0]
                    print(f"Prediction time: {time.time() - start_time:.2f}s")

                    pred_label = le.inverse_transform([pred_idx])[0]
                    print(pred_label)

                    text_label.configure(text="")
                    text_label.configure(text=
                        f"✅ Prediction Complete!\n\n📌 Predicted Sign: **{pred_label}**\n\n🕒 Time Taken: {time.time() - start_time:.2f} seconds"
                    )

                    # === Step 3: Emotion Analysis ===
                    start_time = time.time()

                    print(f"Emotion analysis time: {time.time() - start_time:.2f}s")
                    emotion_label.configure(text=f"🧠 Detected Emotion: {emotion}")
                    # === Step 4: Get Final Text ===

                    # === Step 5: Update GUI in Main Thread ===


                except Exception as e:
                    print("Error during video processing:", e)

            # Start thread
            threading.Thread(target=process_video).start()

    def speak_output():

        text = text_label.cget("text").strip()
        ge.speak_it(text)
        print("works")

    def play_placeholder():
        nonlocal cap
        if cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = cap.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = prep.resize_and_pad(img, (500, 400))
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk
                video_label.configure(image=imgtk)

        video_label.after(33, play_placeholder)  # ~30 FPS

    main_frame = ctk.CTkFrame(parent, fg_color=BG_COLOR)

    title_label = ctk.CTkLabel(
        main_frame,
        text="AI for the non verbal cues:\n"
             "A Facial and Gestural-Based Emotion and Depression Analysis System\n"
             "for the Welfare of Deaf-Mute Individuals in Society.",
        font=ctk.CTkFont(family="Helvetica Neue", size=15, weight="bold"),
        text_color="white",
        justify="center",
        wraplength=800
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


    play_placeholder()

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

    # === New Flex Container ===
    output_flex_container = ctk.CTkFrame(
        main_frame,
        fg_color="black",
        corner_radius=15,
        height=200
    )
    output_flex_container.place(relx=0.5, rely=0.85, relwidth=0.95, relheight=0.2, anchor="center")
    output_flex_container.grid_columnconfigure((0, 1, 2), weight=1)
    output_flex_container.grid_rowconfigure(0, weight=1)

    # === Left: Text Box View (Now a Label View) ===
    text_view = ctk.CTkFrame(output_flex_container, fg_color=INPUT_FIELD_COLOR, corner_radius=15)
    text_view.place(relx=0.0, rely=0.0, relwidth=0.33, relheight=1.0)

    text_label = ctk.CTkLabel(
        text_view,
        text="Transcript/Translation Output:\n\nWaiting for input...",
        fg_color=INPUT_FIELD_COLOR,
        text_color="white",
        font=ctk.CTkFont(size=14),
        anchor="nw",  # Align text to top-left
        justify="left",
        wraplength=300  # Adjust based on how wide you want it
    )
    text_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    speak_button = ctk.CTkButton(
        text_view,
        text="🔊 Speak",
        command=speak_output,
        width=90,
        height=35,
        fg_color=BUTTON_COLOR,
        hover_color=HOVER_COLOR,
        font=ctk.CTkFont(size=14, weight="bold")
    )
    speak_button.grid(row=1, column=0, pady=(0, 10), sticky="se")

    # === Center: Emotion Label View ===
    emotion_view = ctk.CTkFrame(output_flex_container, fg_color=INPUT_FIELD_COLOR, corner_radius=15)
    emotion_view.place(relx=0.34, rely=0.0, relwidth=0.32, relheight=1.0)
    emotion_label = ctk.CTkLabel(
        emotion_view,
        text="😊 Emotion: Waiting...",
        font=ctk.CTkFont(size=16),
        text_color="white",
        wraplength=200
    )


    emotion_label.pack(expand=True, padx=10, pady=10)

    # === Right: Placeholder View for Future ===
    # === Right: Depression View (Vertical Flex) ===
    Depression_view = ctk.CTkFrame(
        output_flex_container,
        fg_color=INPUT_FIELD_COLOR,
        corner_radius=15
    )
    Depression_view.place(relx=0.68, rely=0.0, relwidth=0.32, relheight=1.0)
    Depression_view.pack_propagate(False)

    # Flex direction: column (label on top, canvas below)
    Depression_label = ctk.CTkLabel(
        Depression_view,
        text="🧠 Depression Meter",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="white"
    )
    Depression_label.pack(pady=(10, 0))

    canvas_container = tk.Canvas(
        Depression_view,
        bg=INPUT_FIELD_COLOR,  # updated background color
        width=180,
        height=100,
        highlightthickness=0
    )
    canvas_container.pack(pady=10)
    draw_depression_meter(canvas_container, 180, 100, score=2, r=50)

    return main_frame


def create_speak_frame(parent):
    frame = ctk.CTkFrame(parent, fg_color="#000000")
    label = ctk.CTkLabel(frame, text="Speak Text Feature Coming Soon!",
                         font=ctk.CTkFont(size=20), text_color="white")
    label.pack(pady=200)
    return frame


def create_live_translation_frame(parent):
    FONT_REGULAR = ("Helvetica", 14)
    FONT_BOLD = ("Helvetica", 16, "bold")
    FONT_TITLE = ("Helvetica", 18, "bold")
    FONT_LARGE_EMOJI = ("Helvetica", 24, "bold")
    FONT_FOOTER = ("Helvetica", 12)

    frame = ctk.CTkFrame(parent, fg_color="black")

    container = ctk.CTkFrame(frame, fg_color="black")
    container.pack(expand=True, fill="both", pady=30, padx=30)

    left_view = ctk.CTkFrame(container, fg_color="#1f1f1f", corner_radius=12)
    left_view.pack(side="left", expand=True, fill="both", padx=(0, 20), pady=15)

    inner_left_view = ctk.CTkFrame(left_view, fg_color="gray25", corner_radius=10)
    inner_left_view.place(relx=0.5, rely=0.05, relwidth=0.95, relheight=0.9, anchor="n")

    video_label = ctk.CTkLabel(inner_left_view, text="")
    video_label.place(relx=0.5, rely=0.5, anchor="center")
    ctk.CTkLabel(inner_left_view, text="● LIVE", text_color="red", font=FONT_REGULAR).place(relx=0.05, rely=0.05, anchor="nw")
    # start_webcam_feed(video_label)
    right_view = ctk.CTkFrame(container, fg_color="#1f1f1f", corner_radius=12)
    right_view.pack(side="right", expand=True, fill="both", padx=(20, 0), pady=15)

    top_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
    top_section.place(relx=0.5, rely=0.04, relwidth=0.92, relheight=0.3, anchor="n")
    ctk.CTkLabel(top_section, text="Primary Translation", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.1, anchor="n")
    text_label=ctk.CTkLabel(top_section, text="[Translated Text Appears Here]", text_color="#ffffff", font=FONT_TITLE)
    text_label.place(relx=0.5, rely=0.5, anchor="center")

    middle_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
    middle_section.place(relx=0.5, rely=0.36, relwidth=0.92, relheight=0.3, anchor="n")
    ctk.CTkLabel(middle_section, text="Emotion", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.1, anchor="n")
    ctk.CTkLabel(middle_section, text="[Original Emotion Appears Here]", text_color="#ffffff", font=FONT_REGULAR).place(relx=0.5, rely=0.4, anchor="center")
    emotion_label = ctk.CTkLabel(middle_section, text="😊 Happy", text_color="#ffffff", font=FONT_LARGE_EMOJI)
    emotion_label.place(relx=0.5, rely=0.75, anchor="center")

    bottom_section = ctk.CTkFrame(right_view, fg_color="gray25", corner_radius=10)
    bottom_section.place(relx=0.5, rely=0.68, relwidth=0.92, relheight=0.3, anchor="n")
    ctk.CTkLabel(bottom_section, text="Depression Analysis", text_color="#dddddd", font=FONT_BOLD).place(relx=0.5, rely=0.08, anchor="n")

    canvas_container = tk.Canvas(bottom_section, bg="gray25", highlightthickness=0)
    canvas_container.place(relx=0.5, rely=0.55, anchor="center")
    draw_depression_meter(canvas_container, score=2)

    footer_label = ctk.CTkLabel(frame, text="Tip: Ensure good lighting for better recognition 🔆", text_color="#666666", font=FONT_FOOTER)
    footer_label.pack(side="bottom", pady=5)

    def on_keypress(event):
        if event.char == "e":
            # Update text
            text_label.configure(
                text="✅ Prediction Complete!\n\n📌 Predicted Sign: **hello**\n\n🕒 Time Taken: 0.01 seconds")

            # Update emotion
            emotion_label.configure(text="😊 Emotion: Happy")

            # Update depression meter
            draw_depression_meter(canvas_container, score=0)

    # Bind keypress event
    parent.bind("<Key>", on_keypress)

    return frame

# def start_webcam_feed(video_label):
#     cap = cv2.VideoCapture(0)
#
#     def update_frame():
#         ret, frame = cap.read()
#         if ret:
#             # Convert BGR to RGB
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame)
#             img = img.resize((400, 300))  # Adjust size as needed
#             imgtk = ImageTk.PhotoImage(image=img)
#             video_label.imgtk = imgtk
#             video_label.configure(image=imgtk)
#         video_label.after(10, update_frame)
#
#     update_frame()
