#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
from std_msgs.msg import String

class ObjectDetector:

    def __init__(self):
        rospy.init_node('object_detector', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/stereo_camera/left/image_raw', Image, self.image_callback)
        self.detected = rospy.Publisher("/isStairDetect",String, queue_size=10)
        self.classifier = cv2.CascadeClassifier('/home/gursel/catkin_ws/src/darwin_control/scripts/cascade.xml')

    def image_callback(self, msg):
        self.cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        self.objects = self.classifier.detectMultiScale(self.gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in self.objects:

            cv2.putText(img=self.cv_image, text="detected", org=(450,45), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 70, 0),thickness=1)
            cv2.rectangle(self.cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img=self.cv_image, text="stairs", org=(x, y-10), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 128, 0),thickness=2)

            self.algiladiMi = String()
            self.algiladiMi.data = "stairs detected"
            self.detected.publish(self.algiladiMi)
        cv2.imshow('Object Detection', self.cv_image)
        cv2.waitKey(3)

if __name__ == '__main__':
    detector = ObjectDetector()
    rospy.spin()
