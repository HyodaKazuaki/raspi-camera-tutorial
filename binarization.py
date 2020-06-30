import cv2

def main(threshold=100):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        result, img_binarization = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        cv2.imshow('binarization image', img_binarization)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    threshold = 100
    main(threshold=threshold)
