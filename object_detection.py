import cv2
import tensorflow as tf
import numpy as np
import time

detection_graph = tf.Graph()

colors = [
  (0, 0, 255),
  (0, 64, 255),
  (0, 128, 255),
  (0, 192, 255),
  (0, 255, 255),
  (0, 255, 192),
  (0, 255, 128),
  (0, 255, 64),
  (0, 255, 0),
  (64, 255, 0),
  (128, 255, 0),
  (192, 255, 0),
  (255, 255, 0),
  (255, 192, 0),
  (255, 128, 0),
  (255, 64, 0),
  (255, 0, 0),
  (255, 0, 64),
  (255, 0, 128),
  (255, 0, 192),
  (255, 0, 255),
  (192, 0, 255),
  (128, 0, 255),
  (64, 0, 255),
]

def load_graph():
  with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile("./ssdlite_mobilenet_v2_coco_2018_05_09/frozen_inference_graph.pb", 'rb') as fid:
      serialized_graph = fid.read()
      od_graph_def.ParseFromString(serialized_graph)
      tf.import_graph_def(od_graph_def, name='')
    return detection_graph

def run_inference_for_single_image(image, graph):
  # Run inference
  output_dict = tf_sess.run(tensor_dict,
                          feed_dict={image_tensor: image})

  # all outputs are float32 numpy arrays, so convert types as appropriate
  output_dict['num_detections'] = int(output_dict['num_detections'][0])
  output_dict['detection_classes'] = output_dict[
      'detection_classes'][0].astype(np.int64)
  output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
  output_dict['detection_scores'] = output_dict['detection_scores'][0]
  return output_dict

def main():
    camera_stream = cv2.VideoCapture(0)
    labels = ['blank']
    with open("coco-labels-paper.txt",'r') as f:
        for line in f:
            labels.append(line.rstrip())
    count = 0
    count_max = 0

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        count += 1
        if count > count_max:
            count = 0
            img_bgr = cv2.resize(img, (640, 640))
            # convert bgr to rgb
            image_np = img_bgr[:,:,::-1]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            start = time.time()
            output_dict = run_inference_for_single_image(image_np_expanded, detection_graph)
            elapsed_time = time.time() - start

            for i in range(output_dict['num_detections']):
                class_id = output_dict['detection_classes'][i]
                if class_id < len(labels):
                    label = labels[class_id]
                else:
                    label = 'unknown'

                detection_score = output_dict['detection_scores'][i]

                if detection_score > 0.5:
                    # Define bounding box
                    h, w, c = img.shape
                    box = output_dict['detection_boxes'][i] * np.array( \
                    [h, w,  h, w])
                    box = box.astype(np.int)

                    speed_info = '%s: %.3f' % ('fps', 1.0/elapsed_time)
                    cv2.putText(img, speed_info, (10,50), \
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

                    class_id = class_id % len(colors)
                    color = colors[class_id]

                    # Draw bounding box
                    cv2.rectangle(img, \
                    (box[1], box[0]), (box[3], box[2]), color, 3)

                    # Put label near bounding box
                    information = '%s: %.1f%%' % (label, output_dict['detection_scores'][i] * 100.0)
                    cv2.putText(img, information, (box[1] + 15, box[2] - 15), \
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)

        cv2.imshow('object detection', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tf_sess.close()
    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Loading graph")
    detection_graph = load_graph()
    print("Graph loaded")
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True
    with detection_graph.as_default():
        tf_sess = tf.Session(config = tf_config)
        ops = tf.get_default_graph().get_operations()
        all_tensor_names = {output.name for op in ops for output in op.outputs}
        tensor_dict = {}
        for key in [
            'num_detections', 'detection_boxes', 'detection_scores',
            'detection_classes', 'detection_masks'
        ]:
            tensor_name = key + ':0'
            if tensor_name in all_tensor_names:
                tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
                    tensor_name)

        image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

    main()
