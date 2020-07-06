import cv2
import time

def main():
    camera_stream = cv2.VideoCapture(0)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.2}

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        start = time.time()
        human, r = hog.detectMultiScale(img, **hogParams)
        elapsed_time = time.time() - start
        speed_info = '%s: %.3f' % ('fps', 1.0/elapsed_time)
        cv2.putText(img, speed_info, (10,50), \
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        for (x, y, w, h) in human:
            cv2.rectangle(img, (x, y),(x+w, y+h),(0,50,255), 3)
        cv2.imshow('human detection', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
