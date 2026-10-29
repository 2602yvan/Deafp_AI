import os
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.utils import to_categorical

# === CONFIGURATION ===
MP4_DIR = "/path/to/your/mp4/videos"
CSV_DIR = "/path/to/your/label/csv"
CSV_FILE = "labels.csv"
MAX_FRAMES_PER_VIDEO = 30  # Adjust based on your video length and memory
FRAME_HEIGHT = 64
FRAME_WIDTH = 64

# === DATA LOADING ===
csv_path = os.path.join(CSV_DIR, CSV_FILE)

try:
    df = pd.read_csv(csv_path)
    uid_to_label = dict(zip(df["uid"], df["label"]))
except FileNotFoundError:
    print(f"Error: The label CSV file at '{csv_path}' was not found.")
    exit()


def process_video_frames(video_path, max_frames, height, width):
    """
    Loads a video, resizes frames, and pads/truncates to a consistent length.
    Returns a 4D numpy array of shape (max_frames, height, width, 3).
    """
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame and normalize pixel values
        resized_frame = cv2.resize(frame, (width, height))
        normalized_frame = resized_frame / 255.0  # Normalize to [0, 1]
        frames.append(normalized_frame)

    cap.release()

    # Handle videos with more or fewer frames than max_frames
    if len(frames) > max_frames:
        frames = frames[:max_frames]  # Truncate
    elif len(frames) < max_frames:
        # Pad with black frames if too short
        num_padding = max_frames - len(frames)
        black_frame = np.zeros((height, width, 3), dtype=np.float32)
        frames.extend([black_frame] * num_padding)

    return np.array(frames)


X, y = [], []
count = 0
filtered_count = 0

for fname in os.listdir(MP4_DIR):
    if count >= LIMIT:
        break
    count += 1

    if not fname.endswith(".mp4"):
        continue

    uid = os.path.splitext(fname)[0]  # Get uid without extension
    if uid not in uid_to_label:
        filtered_count += 1
        continue

    video_path = os.path.join(MP4_DIR, fname)

    try:
        video_data = process_video_frames(video_path, MAX_FRAMES_PER_VIDEO, FRAME_HEIGHT, FRAME_WIDTH)
        X.append(video_data)
        y.append(uid_to_label[uid])
    except Exception as e:
        print(f"⚠️ Error processing {fname}: {e}")

print(f"\nDone. Loaded {len(X)} samples.")
print(f"Files with no matching UID or wrong format: {filtered_count}")

# Convert lists to final NumPy arrays
X = np.array(X)
y = np.array(y)

print("\n--- Final Data Shape ---")
print(f"Shape of X (video data): {X.shape}")
print(f"Shape of y (labels): {y.shape}")