import cv2
# index of video camera
cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 2nd arg is a fourcc code that is used to specify the video codec.
# For more info about fourcc, visit www.fourcc.org
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    # if there are frames
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # starts recording/writing video stops when q key is pressed
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
