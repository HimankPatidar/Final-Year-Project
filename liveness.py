import cv2

def check_liveness(prev_frame, current_frame):
    if prev_frame is None:
        return True

    
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    
    diff = cv2.absdiff(prev_gray, curr_gray)
    score = diff.mean()

    
    if score > 2:
        return True

    return False