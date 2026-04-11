import cv2
import torch
import numpy as np
import os
import pandas as pd
from facenet_pytorch import MTCNN, InceptionResnetV1
from attendance import mark_attendance
from liveness import check_liveness


prev_frame = None

device = 'cuda' if torch.cuda.is_available() else 'cpu'

mtcnn = MTCNN(keep_all=True, device=device)
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)


# LOAD STUDENT DETAILS

if os.path.exists("students.csv"):
    students_df = pd.read_csv("students.csv")
else:
    students_df = pd.DataFrame(columns=["Name", "Department", "Semester", "Section"])


# LOAD ENCODINGS

known_faces = {}

for file in os.listdir("encodings"):
    name = file.replace(".npy", "")
    data = np.load(f"encodings/{file}")
    known_faces[name] = data

print("✅ Loaded known faces:", list(known_faces.keys()))


# GET STUDENT INFO

def get_student_info(name):
    student = students_df[students_df["Name"] == name]

    if not student.empty:
        row = student.iloc[0]
        return row
    return None


# RECOGNITION FUNCTION

def recognize_face(face_embedding):
    min_dist = float("inf")
    identity = "Unknown"

    for name, embeddings in known_faces.items():
        for emb in embeddings:
            dist = np.linalg.norm(emb - face_embedding)

            if dist < min_dist:
                min_dist = dist
                identity = name

    if min_dist < 0.8:
        return identity
    return "Unknown"


# CAMERA START

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not working")
    exit()

print("🎥 Starting recognition... Press ESC to exit")


# MAIN LOOP

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Liveness check
    is_live = check_liveness(prev_frame, frame)
    prev_frame = frame.copy()

    # Detect faces
    boxes, _ = mtcnn.detect(frame)

    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)

            # Draw box first
            color = (0,255,0) if is_live else (0,0,255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            if not is_live:
                cv2.putText(frame, "FAKE / NO MOVEMENT", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
                continue

            # Crop face
            face_img = frame[y1:y2, x1:x2]

            face = mtcnn(face_img)

            if face is not None:
                if face.ndim == 3:
                    face = face.unsqueeze(0)

                emb = model(face.to(device))
                emb = emb.detach().cpu().numpy()[0]

                # Recognize
                name = recognize_face(emb)

                if name != "Unknown":
                    mark_attendance(name)

                    # Get student details
                    student = get_student_info(name)

                    if student is not None:
                        # Multi-line display
                        y_offset = y1 - 40

                        cv2.putText(frame, f"{student['Name']}", (x1, y_offset),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                        cv2.putText(frame, f"{student['Department']}", (x1, y_offset+15),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                        cv2.putText(frame, f"Sem {student['Semester']} | Sec {student['Section']}",
                                    (x1, y_offset+30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                    else:
                        cv2.putText(frame, name, (x1, y1-10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

                else:
                    cv2.putText(frame, "Unknown", (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    # Show frame
    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()