import cv2
import time

def main(threshold=100):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        start = time.time()
        result, img_binarization = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        elapsed_time = time.time() - start
        speed_info = '%s: %.3f' % ('fps', 1.0/elapsed_time)
        cv2.putText(img_binarization, speed_info, (10,50), \
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('binarization image', img_binarization)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    threshold = 100
    main(threshold=threshold)
