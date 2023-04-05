import cv2 as cv

capture = cv.VideoCapture('Video/A$AP Ferg - Floor Seats (Official Video).mp4')

running = True


def frame_resize(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimenstions = (width, height)

    return cv.resize(frame, dimenstions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    capture.set(3, width)
    capture.set(4, height)


while running:
    is_true, frame = capture.read()
    frame_resized = frame_resize(frame, 2)
    # cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
