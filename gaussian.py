import cv2
import time

def main(kernel=(5, 5)):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        start = time.time()
        img_gaussian = cv2.GaussianBlur(img, kernel, 0)
        elapsed_time = time.time() - start
        speed_info = '%s: %.3f' % ('fps', 1.0/elapsed_time)
        cv2.putText(img_gaussian, speed_info, (10,50), \
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('gaussian image', img_gaussian)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kernel = (41, 41)
    main(kernel=kernel)
