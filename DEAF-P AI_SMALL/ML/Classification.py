import os
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from tqdm import tqdm

# ===========================
# PATHS (your folders)
# ===========================
DATA_PATH = r"D:/archive/ISL_CSLRT_Corpus/ISL_CSLRT_Corpus/Frames_Word_Level"
SAVE_PATH = r"D:/archive/ISL_CSLRT_Corpus/ISL_CSLRT_Corpus/image_data"
os.makedirs(SAVE_PATH, exist_ok=True)

# ===========================
# SETUP MEDIAPIPE HANDS
# ===========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)

# ===========================
# HAND LANDMARK EXTRACTION
# ===========================
def extract_hand_landmarks(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert back to RGB for MediaPipe processing
    rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    results = hands.process(rgb)

    if not results.multi_hand_landmarks:
        return None

    # Extract 21 (x, y, z) landmarks = 63 values
    landmarks = []
    for lm in results.multi_hand_landmarks[0].landmark:
        landmarks.extend([lm.x, lm.y, lm.z])

    return np.array(landmarks, dtype=np.float32)

# ===========================
# MAIN LOOP
# ===========================
all_files = []
all_labels = []
labels = os.listdir(DATA_PATH)

for label in tqdm(labels, desc="Processing labels"):
    label_path = os.path.join(DATA_PATH, label)
    if not os.path.isdir(label_path):
        continue

    save_label_dir = os.path.join(SAVE_PATH, label)
    os.makedirs(save_label_dir, exist_ok=True)

    for file in os.listdir(label_path):
        file_path = os.path.join(label_path, file)
        if not (file.lower().endswith(".jpg") or file.lower().endswith(".png")):
            continue

        landmarks = extract_hand_landmarks(file_path)
        if landmarks is not None:
            save_name = os.path.splitext(file)[0] + ".npy"
            np.save(os.path.join(save_label_dir, save_name), landmarks)
            all_files.append(save_name)
            all_labels.append(label)

# ===========================
# SAVE LABEL MAPPING
# ===========================
df = pd.DataFrame({"filename": all_files, "label": all_labels})
df.to_csv(os.path.join(SAVE_PATH, "labels.csv"), index=False)

hands.close()
print("✅ Preprocessing complete!")
print(f"Saved data to: {SAVE_PATH}")
print(f"Total processed images: {len(all_files)}")
