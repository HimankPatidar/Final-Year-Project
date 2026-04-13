import cv2
import torch
import numpy as np
import os
from facenet_pytorch import MTCNN, InceptionResnetV1

device = 'cuda' if torch.cuda.is_available() else 'cpu'

mtcnn = MTCNN(keep_all=False, device=device)
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)


# CHECK DUPLICATE FACE
def is_duplicate(new_embedding, threshold=0.8):
    if not os.path.exists("encodings"):
        return False

    for file in os.listdir("encodings"):
        data = np.load(f"encodings/{file}")

        for emb in data:
            dist = np.linalg.norm(emb - new_embedding)
            if dist < threshold:
                return True

    return False



# ENROLL FUNCTION
def enroll(name):
    cap = cv2.VideoCapture(0)

    embeddings = []
    count = 0
    max_samples = 20

    while count < max_samples:
        ret, frame = cap.read()
        if not ret:
            print("Camera error")
            break

        # Convert BGR -> RGB (IMPORTANT for MTCNN)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face = mtcnn(rgb_frame)

        if face is not None:
            if face.ndim == 3:
                face = face.unsqueeze(0)

            emb = model(face.to(device))
            emb = emb.detach().cpu().numpy()[0]

            # Duplicate check only once
            if count == 0:
                if is_duplicate(emb):
                    cap.release()
                    cv2.destroyAllWindows()
                    return "duplicate"

            embeddings.append(emb)
            count += 1

            # Show progress
            cv2.putText(frame, f"Captured: {count}/{max_samples}",
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        else:
            # Show warning if no face
            cv2.putText(frame, "No Face Detected",
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

        cv2.imshow("Registering Face", frame)

        if cv2.waitKey(1) == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

    if len(embeddings) == 0:
        return "no_face"

    embeddings = np.vstack(embeddings)

    # Create folder if not exists
    if not os.path.exists("encodings"):
        os.makedirs("encodings")

    np.save(f"encodings/{name}.npy", embeddings)

    return "success"