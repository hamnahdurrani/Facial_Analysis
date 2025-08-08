import threading
import cv2
from deepface import DeepFace

#OpenCV webcam set up

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_found = False
analysis = {"age" : "", "gender" : "", "race" : "", "emotion" : ""}

#Extracting facial analysis
def face_analysis(frame):
    global face_found, analysis
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    try:
        facial_analysis = DeepFace.analyze(img_path= rgb_frame, actions=['age', 'gender', 'race', 'emotion'], enforce_detection=True)
        analysis["age"] = facial_analysis[0]["age"]
        analysis["gender"] = facial_analysis[0]["dominant_gender"]
        analysis["race"] = facial_analysis[0]["dominant_race"]
        analysis["emotion"] = facial_analysis[0]["dominant_emotion"]
        face_found = True
    except ValueError:
        pass

while True:
    #Reading Camera 
    ret, frame = cap.read()
    if ret:
        if counter % 60 == 0:
            try:
                threading.Thread(target = face_analysis, args =(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if face_found:
            text = f"Age: {analysis['age']}  Gender: {analysis['gender']}  Race: {analysis['race']}  Emotion: {analysis['emotion']}"
            cv2.putText(frame, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)
            cv2.putText(frame, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        else :
            analysis = {"age" : "", "gender" : "", "race" : "", "emotion" : ""}
            cv2.putText(frame, "Face Not Detected", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 4)
            cv2.putText(frame, "Face Not Detected", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    #Closing window prompt
    if key == ord('q'):
        break
cv2.destroyAllWindows()