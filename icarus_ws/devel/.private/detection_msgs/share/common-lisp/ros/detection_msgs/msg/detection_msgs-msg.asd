
(cl:in-package :asdf)

(defsystem "detection_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBox" :depends-on ("_package_BoundingBox"))
    (:file "_package_BoundingBox" :depends-on ("_package"))
    (:file "BoundingBoxes" :depends-on ("_package_BoundingBoxes"))
    (:file "_package_BoundingBoxes" :depends-on ("_package"))
    (:file "PublishData" :depends-on ("_package_PublishData"))
    (:file "_package_PublishData" :depends-on ("_package"))
    (:file "Publish_Data" :depends-on ("_package_Publish_Data"))
    (:file "_package_Publish_Data" :depends-on ("_package"))
  ))