import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
turn = True
while turn:
    face_id = input('\n enter user id ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite(r'C:\Users\Emax Raka\PycharmProjects\Faces Recognition\FacialRecognitionProject\dataset\User.' + str(face_id) + r'.' + str(count) + r'.jpg', gray[y:y+h, x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break
    print('Face Scanning successful!')
    print('Do You want to scan another face?')
    answer = input('\nYes or no\n')
    if answer.lower() == 'yes' or answer.lower() == 'y':
        turn = True
        print('Continuing Program')
    else:
        turn = False
        print('Preaparing to exit the Program')


print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()
