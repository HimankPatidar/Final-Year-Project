import cv2
import torch
import numpy as np
import os
from facenet_pytorch import MTCNN, InceptionResnetV1

device = 'cuda' if torch.cuda.is_available() else 'cpu'

mtcnn = MTCNN(keep_all=False, device=device)
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)

# Check duplicate
def is_duplicate(new_embedding, threshold=0.8):
    for file in os.listdir("encodings"):
        data = np.load(f"encodings/{file}")

        for emb in data:
            dist = np.linalg.norm(emb - new_embedding)
            if dist < threshold:
                return True

    return False

def enroll(name):
    cap = cv2.VideoCapture(0)

    embeddings = []
    count = 0

    while count < 20:
        ret, frame = cap.read()
        if not ret:
            break

        face = mtcnn(frame)

        if face is not None:
            if face.ndim == 3:
                face = face.unsqueeze(0)

            emb = model(face.to(device))
            emb = emb.detach().cpu().numpy()[0]

            # Check duplicate BEFORE saving
            if count == 0:
                if is_duplicate(emb):
                    cap.release()
                    cv2.destroyAllWindows()
                    return "duplicate"

            embeddings.append(emb)
            count += 1

        cv2.imshow("Registering Face", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    embeddings = np.vstack(embeddings)

    if not os.path.exists("encodings"):
        os.makedirs("encodings")

    np.save(f"encodings/{name}.npy", embeddings)

    return "success"