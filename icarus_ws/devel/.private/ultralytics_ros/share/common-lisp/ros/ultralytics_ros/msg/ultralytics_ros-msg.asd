
(cl:in-package :asdf)

(defsystem "ultralytics_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
               :vision_msgs-msg
)
  :components ((:file "_package")
    (:file "YoloResult" :depends-on ("_package_YoloResult"))
    (:file "_package_YoloResult" :depends-on ("_package"))
  ))