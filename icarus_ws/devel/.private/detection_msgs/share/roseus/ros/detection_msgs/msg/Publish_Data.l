;; Auto-generated. Do not edit!


(when (boundp 'detection_msgs::Publish_Data)
  (if (not (find-package "DETECTION_MSGS"))
    (make-package "DETECTION_MSGS"))
  (shadow 'Publish_Data (find-package "DETECTION_MSGS")))
(unless (find-package "DETECTION_MSGS::PUBLISH_DATA")
  (make-package "DETECTION_MSGS::PUBLISH_DATA"))

(in-package "ROS")
;;//! \htmlinclude Publish_Data.msg.html


(defclass detection_msgs::Publish_Data
  :super ros::object
  :slots (_id _real_distance _estimated_distance _depth _depth_distance _use_depth _center_x _center_y _error_heading _error_altitude _altitude _controller_error _control_output _target_lost _target_detected _distance_cnst _distance_imm _distance_singer _target_x _target_y _uav_x _uav_y _real_target_x _real_target_y _estimated_target_x _estimated_target_y _Vx _Vy _Vz _Hdg_rate _mode _horizontal_distance ))

(defmethod detection_msgs::Publish_Data
  (:init
   (&key
    ((:id __id) 0)
    ((:real_distance __real_distance) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:estimated_distance __estimated_distance) 0.0)
    ((:depth __depth) 0.0)
    ((:depth_distance __depth_distance) 0.0)
    ((:use_depth __use_depth) nil)
    ((:center_x __center_x) 0.0)
    ((:center_y __center_y) 0.0)
    ((:error_heading __error_heading) 0.0)
    ((:error_altitude __error_altitude) 0.0)
    ((:altitude __altitude) 0.0)
    ((:controller_error __controller_error) 0.0)
    ((:control_output __control_output) 0.0)
    ((:target_lost __target_lost) nil)
    ((:target_detected __target_detected) nil)
    ((:distance_cnst __distance_cnst) 0.0)
    ((:distance_imm __distance_imm) 0.0)
    ((:distance_singer __distance_singer) 0.0)
    ((:target_x __target_x) 0.0)
    ((:target_y __target_y) 0.0)
    ((:uav_x __uav_x) 0.0)
    ((:uav_y __uav_y) 0.0)
    ((:real_target_x __real_target_x) 0.0)
    ((:real_target_y __real_target_y) 0.0)
    ((:estimated_target_x __estimated_target_x) 0.0)
    ((:estimated_target_y __estimated_target_y) 0.0)
    ((:Vx __Vx) 0.0)
    ((:Vy __Vy) 0.0)
    ((:Vz __Vz) 0.0)
    ((:Hdg_rate __Hdg_rate) 0.0)
    ((:mode __mode) 0)
    ((:horizontal_distance __horizontal_distance) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _real_distance __real_distance)
   (setq _estimated_distance (float __estimated_distance))
   (setq _depth (float __depth))
   (setq _depth_distance (float __depth_distance))
   (setq _use_depth __use_depth)
   (setq _center_x (float __center_x))
   (setq _center_y (float __center_y))
   (setq _error_heading (float __error_heading))
   (setq _error_altitude (float __error_altitude))
   (setq _altitude (float __altitude))
   (setq _controller_error (float __controller_error))
   (setq _control_output (float __control_output))
   (setq _target_lost __target_lost)
   (setq _target_detected __target_detected)
   (setq _distance_cnst (float __distance_cnst))
   (setq _distance_imm (float __distance_imm))
   (setq _distance_singer (float __distance_singer))
   (setq _target_x (float __target_x))
   (setq _target_y (float __target_y))
   (setq _uav_x (float __uav_x))
   (setq _uav_y (float __uav_y))
   (setq _real_target_x (float __real_target_x))
   (setq _real_target_y (float __real_target_y))
   (setq _estimated_target_x (float __estimated_target_x))
   (setq _estimated_target_y (float __estimated_target_y))
   (setq _Vx (float __Vx))
   (setq _Vy (float __Vy))
   (setq _Vz (float __Vz))
   (setq _Hdg_rate (float __Hdg_rate))
   (setq _mode (round __mode))
   (setq _horizontal_distance (float __horizontal_distance))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:real_distance
   (&optional __real_distance)
   (if __real_distance (setq _real_distance __real_distance)) _real_distance)
  (:estimated_distance
   (&optional __estimated_distance)
   (if __estimated_distance (setq _estimated_distance __estimated_distance)) _estimated_distance)
  (:depth
   (&optional __depth)
   (if __depth (setq _depth __depth)) _depth)
  (:depth_distance
   (&optional __depth_distance)
   (if __depth_distance (setq _depth_distance __depth_distance)) _depth_distance)
  (:use_depth
   (&optional (__use_depth :null))
   (if (not (eq __use_depth :null)) (setq _use_depth __use_depth)) _use_depth)
  (:center_x
   (&optional __center_x)
   (if __center_x (setq _center_x __center_x)) _center_x)
  (:center_y
   (&optional __center_y)
   (if __center_y (setq _center_y __center_y)) _center_y)
  (:error_heading
   (&optional __error_heading)
   (if __error_heading (setq _error_heading __error_heading)) _error_heading)
  (:error_altitude
   (&optional __error_altitude)
   (if __error_altitude (setq _error_altitude __error_altitude)) _error_altitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:controller_error
   (&optional __controller_error)
   (if __controller_error (setq _controller_error __controller_error)) _controller_error)
  (:control_output
   (&optional __control_output)
   (if __control_output (setq _control_output __control_output)) _control_output)
  (:target_lost
   (&optional (__target_lost :null))
   (if (not (eq __target_lost :null)) (setq _target_lost __target_lost)) _target_lost)
  (:target_detected
   (&optional (__target_detected :null))
   (if (not (eq __target_detected :null)) (setq _target_detected __target_detected)) _target_detected)
  (:distance_cnst
   (&optional __distance_cnst)
   (if __distance_cnst (setq _distance_cnst __distance_cnst)) _distance_cnst)
  (:distance_imm
   (&optional __distance_imm)
   (if __distance_imm (setq _distance_imm __distance_imm)) _distance_imm)
  (:distance_singer
   (&optional __distance_singer)
   (if __distance_singer (setq _distance_singer __distance_singer)) _distance_singer)
  (:target_x
   (&optional __target_x)
   (if __target_x (setq _target_x __target_x)) _target_x)
  (:target_y
   (&optional __target_y)
   (if __target_y (setq _target_y __target_y)) _target_y)
  (:uav_x
   (&optional __uav_x)
   (if __uav_x (setq _uav_x __uav_x)) _uav_x)
  (:uav_y
   (&optional __uav_y)
   (if __uav_y (setq _uav_y __uav_y)) _uav_y)
  (:real_target_x
   (&optional __real_target_x)
   (if __real_target_x (setq _real_target_x __real_target_x)) _real_target_x)
  (:real_target_y
   (&optional __real_target_y)
   (if __real_target_y (setq _real_target_y __real_target_y)) _real_target_y)
  (:estimated_target_x
   (&optional __estimated_target_x)
   (if __estimated_target_x (setq _estimated_target_x __estimated_target_x)) _estimated_target_x)
  (:estimated_target_y
   (&optional __estimated_target_y)
   (if __estimated_target_y (setq _estimated_target_y __estimated_target_y)) _estimated_target_y)
  (:Vx
   (&optional __Vx)
   (if __Vx (setq _Vx __Vx)) _Vx)
  (:Vy
   (&optional __Vy)
   (if __Vy (setq _Vy __Vy)) _Vy)
  (:Vz
   (&optional __Vz)
   (if __Vz (setq _Vz __Vz)) _Vz)
  (:Hdg_rate
   (&optional __Hdg_rate)
   (if __Hdg_rate (setq _Hdg_rate __Hdg_rate)) _Hdg_rate)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:horizontal_distance
   (&optional __horizontal_distance)
   (if __horizontal_distance (setq _horizontal_distance __horizontal_distance)) _horizontal_distance)
  (:serialization-length
   ()
   (+
    ;; int64 _id
    8
    ;; float64[] _real_distance
    (* 8    (length _real_distance)) 4
    ;; float64 _estimated_distance
    8
    ;; float64 _depth
    8
    ;; float64 _depth_distance
    8
    ;; bool _use_depth
    1
    ;; float64 _center_x
    8
    ;; float64 _center_y
    8
    ;; float64 _error_heading
    8
    ;; float64 _error_altitude
    8
    ;; float64 _altitude
    8
    ;; float64 _controller_error
    8
    ;; float64 _control_output
    8
    ;; bool _target_lost
    1
    ;; bool _target_detected
    1
    ;; float64 _distance_cnst
    8
    ;; float64 _distance_imm
    8
    ;; float64 _distance_singer
    8
    ;; float64 _target_x
    8
    ;; float64 _target_y
    8
    ;; float64 _uav_x
    8
    ;; float64 _uav_y
    8
    ;; float64 _real_target_x
    8
    ;; float64 _real_target_y
    8
    ;; float64 _estimated_target_x
    8
    ;; float64 _estimated_target_y
    8
    ;; float64 _Vx
    8
    ;; float64 _Vy
    8
    ;; float64 _Vz
    8
    ;; float64 _Hdg_rate
    8
    ;; int64 _mode
    8
    ;; float64 _horizontal_distance
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _id) (= (length (_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_id . bv) 0) 0) s)
              (write-long (ash (elt (_id . bv) 1) -1) s))
             ((and (class _id) (= (length (_id . bv)) 1)) ;; big1
              (write-long (elt (_id . bv) 0) s)
              (write-long (if (>= _id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _id s)(write-long (if (>= _id 0) 0 #xffffffff) s)))
     ;; float64[] _real_distance
     (write-long (length _real_distance) s)
     (dotimes (i (length _real_distance))
       (sys::poke (elt _real_distance i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _estimated_distance
       (sys::poke _estimated_distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _depth
       (sys::poke _depth (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _depth_distance
       (sys::poke _depth_distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _use_depth
       (if _use_depth (write-byte -1 s) (write-byte 0 s))
     ;; float64 _center_x
       (sys::poke _center_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _center_y
       (sys::poke _center_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _error_heading
       (sys::poke _error_heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _error_altitude
       (sys::poke _error_altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _controller_error
       (sys::poke _controller_error (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _control_output
       (sys::poke _control_output (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _target_lost
       (if _target_lost (write-byte -1 s) (write-byte 0 s))
     ;; bool _target_detected
       (if _target_detected (write-byte -1 s) (write-byte 0 s))
     ;; float64 _distance_cnst
       (sys::poke _distance_cnst (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distance_imm
       (sys::poke _distance_imm (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distance_singer
       (sys::poke _distance_singer (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_x
       (sys::poke _target_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _target_y
       (sys::poke _target_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _uav_x
       (sys::poke _uav_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _uav_y
       (sys::poke _uav_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _real_target_x
       (sys::poke _real_target_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _real_target_y
       (sys::poke _real_target_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _estimated_target_x
       (sys::poke _estimated_target_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _estimated_target_y
       (sys::poke _estimated_target_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vx
       (sys::poke _Vx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vy
       (sys::poke _Vy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vz
       (sys::poke _Vz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Hdg_rate
       (sys::poke _Hdg_rate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _mode
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _mode (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _mode) (= (length (_mode . bv)) 2)) ;; bignum
              (write-long (ash (elt (_mode . bv) 0) 0) s)
              (write-long (ash (elt (_mode . bv) 1) -1) s))
             ((and (class _mode) (= (length (_mode . bv)) 1)) ;; big1
              (write-long (elt (_mode . bv) 0) s)
              (write-long (if (>= _mode 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _mode s)(write-long (if (>= _mode 0) 0 #xffffffff) s)))
     ;; float64 _horizontal_distance
       (sys::poke _horizontal_distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _id
#+(or :alpha :irix6 :x86_64)
      (setf _id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64[] _real_distance
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _real_distance (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _real_distance i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _estimated_distance
     (setq _estimated_distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _depth
     (setq _depth (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _depth_distance
     (setq _depth_distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _use_depth
     (setq _use_depth (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _center_x
     (setq _center_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _center_y
     (setq _center_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _error_heading
     (setq _error_heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _error_altitude
     (setq _error_altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _controller_error
     (setq _controller_error (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _control_output
     (setq _control_output (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _target_lost
     (setq _target_lost (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _target_detected
     (setq _target_detected (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _distance_cnst
     (setq _distance_cnst (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distance_imm
     (setq _distance_imm (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distance_singer
     (setq _distance_singer (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_x
     (setq _target_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _target_y
     (setq _target_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _uav_x
     (setq _uav_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _uav_y
     (setq _uav_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _real_target_x
     (setq _real_target_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _real_target_y
     (setq _real_target_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _estimated_target_x
     (setq _estimated_target_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _estimated_target_y
     (setq _estimated_target_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vx
     (setq _Vx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vy
     (setq _Vy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vz
     (setq _Vz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Hdg_rate
     (setq _Hdg_rate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _mode
#+(or :alpha :irix6 :x86_64)
      (setf _mode (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _mode (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _horizontal_distance
     (setq _horizontal_distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get detection_msgs::Publish_Data :md5sum-) "d24cf57b017f31ef8582817de6a3c884")
(setf (get detection_msgs::Publish_Data :datatype-) "detection_msgs/Publish_Data")
(setf (get detection_msgs::Publish_Data :definition-)
      "int64 id
float64[] real_distance
float64 estimated_distance
float64 depth
float64 depth_distance
bool use_depth
float64 center_x
float64 center_y
float64 error_heading
float64 error_altitude
float64 altitude
float64 controller_error
float64 control_output
bool target_lost
bool target_detected
float64 distance_cnst
float64 distance_imm
float64 distance_singer
float64 target_x
float64 target_y
float64 uav_x
float64 uav_y
float64 real_target_x
float64 real_target_y
float64 estimated_target_x
float64 estimated_target_y
float64 Vx
float64 Vy
float64 Vz
float64 Hdg_rate
int64 mode
float64 horizontal_distance

")



(provide :detection_msgs/Publish_Data "d24cf57b017f31ef8582817de6a3c884")


