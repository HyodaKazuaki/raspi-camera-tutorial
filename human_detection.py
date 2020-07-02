import cv2

def main(kernel=(5, 5)):
    camera_stream = cv2.VideoCapture(0)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.2}

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        human, r = hog.detectMultiScale(img, **hogParams)
        for (x, y, w, h) in human:
            cv2.rectangle(img, (x, y),(x+w, y+h),(0,50,255), 3)
        cv2.imshow('human detection', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kernel = (41, 41)
    main(kernel=kernel)
