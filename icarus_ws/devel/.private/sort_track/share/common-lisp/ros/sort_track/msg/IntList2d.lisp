; Auto-generated. Do not edit!


(cl:in-package sort_track-msg)


;//! \htmlinclude IntList2d.msg.html

(cl:defclass <IntList2d> (roslisp-msg-protocol:ros-message)
  ((data2d
    :reader data2d
    :initarg :data2d
    :type (cl:vector sort_track-msg:IntList)
   :initform (cl:make-array 0 :element-type 'sort_track-msg:IntList :initial-element (cl:make-instance 'sort_track-msg:IntList))))
)

(cl:defclass IntList2d (<IntList2d>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IntList2d>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IntList2d)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sort_track-msg:<IntList2d> is deprecated: use sort_track-msg:IntList2d instead.")))

(cl:ensure-generic-function 'data2d-val :lambda-list '(m))
(cl:defmethod data2d-val ((m <IntList2d>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:data2d-val is deprecated.  Use sort_track-msg:data2d instead.")
  (data2d m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IntList2d>) ostream)
  "Serializes a message object of type '<IntList2d>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data2d))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'data2d))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IntList2d>) istream)
  "Deserializes a message object of type '<IntList2d>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data2d) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data2d)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sort_track-msg:IntList))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IntList2d>)))
  "Returns string type for a message object of type '<IntList2d>"
  "sort_track/IntList2d")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IntList2d)))
  "Returns string type for a message object of type 'IntList2d"
  "sort_track/IntList2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IntList2d>)))
  "Returns md5sum for a message object of type '<IntList2d>"
  "1d7b9704b92687ed27b85eeae87a237e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IntList2d)))
  "Returns md5sum for a message object of type 'IntList2d"
  "1d7b9704b92687ed27b85eeae87a237e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IntList2d>)))
  "Returns full string definition for message of type '<IntList2d>"
  (cl:format cl:nil "IntList[] data2d~%~%================================================================================~%MSG: sort_track/IntList~%int32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IntList2d)))
  "Returns full string definition for message of type 'IntList2d"
  (cl:format cl:nil "IntList[] data2d~%~%================================================================================~%MSG: sort_track/IntList~%int32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IntList2d>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data2d) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IntList2d>))
  "Converts a ROS message object to a list"
  (cl:list 'IntList2d
    (cl:cons ':data2d (data2d msg))
))
