;; Auto-generated. Do not edit!


(when (boundp 'sort_track::IntList)
  (if (not (find-package "SORT_TRACK"))
    (make-package "SORT_TRACK"))
  (shadow 'IntList (find-package "SORT_TRACK")))
(unless (find-package "SORT_TRACK::INTLIST")
  (make-package "SORT_TRACK::INTLIST"))

(in-package "ROS")
;;//! \htmlinclude IntList.msg.html


(defclass sort_track::IntList
  :super ros::object
  :slots (_data ))

(defmethod sort_track::IntList
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; int32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-long (elt _data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get sort_track::IntList :md5sum-) "563b27884d008b0d2adff54dc1f9e4f5")
(setf (get sort_track::IntList :datatype-) "sort_track/IntList")
(setf (get sort_track::IntList :definition-)
      "int32[] data

")



(provide :sort_track/IntList "563b27884d008b0d2adff54dc1f9e4f5")


