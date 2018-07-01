from imageai.Detection import ObjectDetection
import os


def recognize(root, src, dst) 
  detector = ObjectDetection()
  detector.setModelTypeAsRetinaNet()
  detector.setModelPath( os.path.join(root, "resnet50_coco_best_v2.0.1.h5"))
  detector.loadModel()
  detections = detector.detectObjectsFromImage(input_image=os.path.join(root, src), output_image_path=os.path.join(root, dst))

  detected_objects = []
  for eachObject in detections:
    detected_objects.append(eachObject)

  return detected_objects