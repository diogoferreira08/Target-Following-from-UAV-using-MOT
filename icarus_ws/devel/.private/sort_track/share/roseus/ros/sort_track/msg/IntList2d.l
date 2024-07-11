;; Auto-generated. Do not edit!


(when (boundp 'sort_track::IntList2d)
  (if (not (find-package "SORT_TRACK"))
    (make-package "SORT_TRACK"))
  (shadow 'IntList2d (find-package "SORT_TRACK")))
(unless (find-package "SORT_TRACK::INTLIST2D")
  (make-package "SORT_TRACK::INTLIST2D"))

(in-package "ROS")
;;//! \htmlinclude IntList2d.msg.html


(defclass sort_track::IntList2d
  :super ros::object
  :slots (_data2d ))

(defmethod sort_track::IntList2d
  (:init
   (&key
    ((:data2d __data2d) ())
    )
   (send-super :init)
   (setq _data2d __data2d)
   self)
  (:data2d
   (&rest __data2d)
   (if (keywordp (car __data2d))
       (send* _data2d __data2d)
     (progn
       (if __data2d (setq _data2d (car __data2d)))
       _data2d)))
  (:serialization-length
   ()
   (+
    ;; sort_track/IntList[] _data2d
    (apply #'+ (send-all _data2d :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sort_track/IntList[] _data2d
     (write-long (length _data2d) s)
     (dolist (elem _data2d)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sort_track/IntList[] _data2d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data2d (let (r) (dotimes (i n) (push (instance sort_track::IntList :init) r)) r))
     (dolist (elem- _data2d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get sort_track::IntList2d :md5sum-) "1d7b9704b92687ed27b85eeae87a237e")
(setf (get sort_track::IntList2d :datatype-) "sort_track/IntList2d")
(setf (get sort_track::IntList2d :definition-)
      "IntList[] data2d

================================================================================
MSG: sort_track/IntList
int32[] data

")



(provide :sort_track/IntList2d "1d7b9704b92687ed27b85eeae87a237e")


