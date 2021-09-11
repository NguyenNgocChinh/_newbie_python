import cv2
import dlib

img = cv2.imread('img.png')

grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# load model face detector
face_detector = dlib.get_frontal_face_detector()

# load predictor
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# use detector to find face landmarks
faces = face_detector(grey_img)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(
        x2, y2), color=(0, 0, 255), thickness=2)

    face_feature = predictor(image=grey_img, box=face)
    # Loop throuht all 68 points
    for n in range(0, 68):
        x = face_feature.part(n).x
        y = face_feature.part(n).y
        # Draw a small circle
        cv2.circle(img=img, center=(x, y), color=(
            0, 255, 0), thickness=1, radius=2)

cv2.imshow(winname='Detect faces', mat=img)

cv2.waitKey()
