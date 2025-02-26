import dlib
import cv2

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

image = cv2.imread("/your image path")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for face in faces:
    landmarks = predictor(gray, face)
    for n in range(0, 68):  
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 5, (0,0,255), -1)

cv2.imshow("Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
