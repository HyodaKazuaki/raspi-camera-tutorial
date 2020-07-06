import cv2
import time

def main(threshold1=100, threshold2=120):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        start = time.time()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_edge = cv2.Canny(img_gray, threshold1, threshold2)
        elapsed_time = time.time() - start
        speed_info = '%s: %.3f' % ('fps', 1.0/elapsed_time)
        cv2.putText(img_edge, speed_info, (10,50), \
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('edge detected image', img_edge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    threshold1 = 30
    threshold2 = 120
    main(threshold1=threshold1, threshold2=threshold2)
