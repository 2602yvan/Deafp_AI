import cv2
import mediapipe as mp
import numpy as np
from PIL import Image


def resize_and_pad(image, target_size):
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
def process_video_to_features(video_path):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5
    )
    # print(analyze_emotions_from_video(video_path))

    cap1 = cv2.VideoCapture(video_path)
    all_landmarks = []

    while True:
        ret, frame = cap1.read()
        if not ret:
            break

        # Auto-rotate if needed
        if frame.shape[0:2] == (240, 320):
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            frame_landmarks = []
            for lm in hand_landmarks.landmark:
                frame_landmarks.extend([lm.x, lm.y, lm.z])
            all_landmarks.append(frame_landmarks)

    cap1.release()
    hands.close()

    if not all_landmarks:
        raise ValueError("No hand landmarks detected!")

    landmarks_np = np.array(all_landmarks)
    mean = np.mean(landmarks_np, axis=0)
    std = np.std(landmarks_np, axis=0)
    min_ = np.min(landmarks_np, axis=0)
    max_ = np.max(landmarks_np, axis=0)
    feature_vector = np.concatenate([mean, std, min_, max_])

    return feature_vector