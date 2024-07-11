// Auto-generated. Do not edit!

// (in-package detection_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Publish_Data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.real_distance = null;
      this.estimated_distance = null;
      this.depth = null;
      this.depth_distance = null;
      this.use_depth = null;
      this.center_x = null;
      this.center_y = null;
      this.error_heading = null;
      this.error_altitude = null;
      this.altitude = null;
      this.controller_error = null;
      this.control_output = null;
      this.target_lost = null;
      this.target_detected = null;
      this.distance_cnst = null;
      this.distance_imm = null;
      this.distance_singer = null;
      this.target_x = null;
      this.target_y = null;
      this.uav_x = null;
      this.uav_y = null;
      this.real_target_x = null;
      this.real_target_y = null;
      this.estimated_target_x = null;
      this.estimated_target_y = null;
      this.Vx = null;
      this.Vy = null;
      this.Vz = null;
      this.Hdg_rate = null;
      this.mode = null;
      this.horizontal_distance = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('real_distance')) {
        this.real_distance = initObj.real_distance
      }
      else {
        this.real_distance = [];
      }
      if (initObj.hasOwnProperty('estimated_distance')) {
        this.estimated_distance = initObj.estimated_distance
      }
      else {
        this.estimated_distance = 0.0;
      }
      if (initObj.hasOwnProperty('depth')) {
        this.depth = initObj.depth
      }
      else {
        this.depth = 0.0;
      }
      if (initObj.hasOwnProperty('depth_distance')) {
        this.depth_distance = initObj.depth_distance
      }
      else {
        this.depth_distance = 0.0;
      }
      if (initObj.hasOwnProperty('use_depth')) {
        this.use_depth = initObj.use_depth
      }
      else {
        this.use_depth = false;
      }
      if (initObj.hasOwnProperty('center_x')) {
        this.center_x = initObj.center_x
      }
      else {
        this.center_x = 0.0;
      }
      if (initObj.hasOwnProperty('center_y')) {
        this.center_y = initObj.center_y
      }
      else {
        this.center_y = 0.0;
      }
      if (initObj.hasOwnProperty('error_heading')) {
        this.error_heading = initObj.error_heading
      }
      else {
        this.error_heading = 0.0;
      }
      if (initObj.hasOwnProperty('error_altitude')) {
        this.error_altitude = initObj.error_altitude
      }
      else {
        this.error_altitude = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
      }
      if (initObj.hasOwnProperty('controller_error')) {
        this.controller_error = initObj.controller_error
      }
      else {
        this.controller_error = 0.0;
      }
      if (initObj.hasOwnProperty('control_output')) {
        this.control_output = initObj.control_output
      }
      else {
        this.control_output = 0.0;
      }
      if (initObj.hasOwnProperty('target_lost')) {
        this.target_lost = initObj.target_lost
      }
      else {
        this.target_lost = false;
      }
      if (initObj.hasOwnProperty('target_detected')) {
        this.target_detected = initObj.target_detected
      }
      else {
        this.target_detected = false;
      }
      if (initObj.hasOwnProperty('distance_cnst')) {
        this.distance_cnst = initObj.distance_cnst
      }
      else {
        this.distance_cnst = 0.0;
      }
      if (initObj.hasOwnProperty('distance_imm')) {
        this.distance_imm = initObj.distance_imm
      }
      else {
        this.distance_imm = 0.0;
      }
      if (initObj.hasOwnProperty('distance_singer')) {
        this.distance_singer = initObj.distance_singer
      }
      else {
        this.distance_singer = 0.0;
      }
      if (initObj.hasOwnProperty('target_x')) {
        this.target_x = initObj.target_x
      }
      else {
        this.target_x = 0.0;
      }
      if (initObj.hasOwnProperty('target_y')) {
        this.target_y = initObj.target_y
      }
      else {
        this.target_y = 0.0;
      }
      if (initObj.hasOwnProperty('uav_x')) {
        this.uav_x = initObj.uav_x
      }
      else {
        this.uav_x = 0.0;
      }
      if (initObj.hasOwnProperty('uav_y')) {
        this.uav_y = initObj.uav_y
      }
      else {
        this.uav_y = 0.0;
      }
      if (initObj.hasOwnProperty('real_target_x')) {
        this.real_target_x = initObj.real_target_x
      }
      else {
        this.real_target_x = 0.0;
      }
      if (initObj.hasOwnProperty('real_target_y')) {
        this.real_target_y = initObj.real_target_y
      }
      else {
        this.real_target_y = 0.0;
      }
      if (initObj.hasOwnProperty('estimated_target_x')) {
        this.estimated_target_x = initObj.estimated_target_x
      }
      else {
        this.estimated_target_x = 0.0;
      }
      if (initObj.hasOwnProperty('estimated_target_y')) {
        this.estimated_target_y = initObj.estimated_target_y
      }
      else {
        this.estimated_target_y = 0.0;
      }
      if (initObj.hasOwnProperty('Vx')) {
        this.Vx = initObj.Vx
      }
      else {
        this.Vx = 0.0;
      }
      if (initObj.hasOwnProperty('Vy')) {
        this.Vy = initObj.Vy
      }
      else {
        this.Vy = 0.0;
      }
      if (initObj.hasOwnProperty('Vz')) {
        this.Vz = initObj.Vz
      }
      else {
        this.Vz = 0.0;
      }
      if (initObj.hasOwnProperty('Hdg_rate')) {
        this.Hdg_rate = initObj.Hdg_rate
      }
      else {
        this.Hdg_rate = 0.0;
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = 0;
      }
      if (initObj.hasOwnProperty('horizontal_distance')) {
        this.horizontal_distance = initObj.horizontal_distance
      }
      else {
        this.horizontal_distance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Publish_Data
    // Serialize message field [id]
    bufferOffset = _serializer.int64(obj.id, buffer, bufferOffset);
    // Serialize message field [real_distance]
    bufferOffset = _arraySerializer.float64(obj.real_distance, buffer, bufferOffset, null);
    // Serialize message field [estimated_distance]
    bufferOffset = _serializer.float64(obj.estimated_distance, buffer, bufferOffset);
    // Serialize message field [depth]
    bufferOffset = _serializer.float64(obj.depth, buffer, bufferOffset);
    // Serialize message field [depth_distance]
    bufferOffset = _serializer.float64(obj.depth_distance, buffer, bufferOffset);
    // Serialize message field [use_depth]
    bufferOffset = _serializer.bool(obj.use_depth, buffer, bufferOffset);
    // Serialize message field [center_x]
    bufferOffset = _serializer.float64(obj.center_x, buffer, bufferOffset);
    // Serialize message field [center_y]
    bufferOffset = _serializer.float64(obj.center_y, buffer, bufferOffset);
    // Serialize message field [error_heading]
    bufferOffset = _serializer.float64(obj.error_heading, buffer, bufferOffset);
    // Serialize message field [error_altitude]
    bufferOffset = _serializer.float64(obj.error_altitude, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float64(obj.altitude, buffer, bufferOffset);
    // Serialize message field [controller_error]
    bufferOffset = _serializer.float64(obj.controller_error, buffer, bufferOffset);
    // Serialize message field [control_output]
    bufferOffset = _serializer.float64(obj.control_output, buffer, bufferOffset);
    // Serialize message field [target_lost]
    bufferOffset = _serializer.bool(obj.target_lost, buffer, bufferOffset);
    // Serialize message field [target_detected]
    bufferOffset = _serializer.bool(obj.target_detected, buffer, bufferOffset);
    // Serialize message field [distance_cnst]
    bufferOffset = _serializer.float64(obj.distance_cnst, buffer, bufferOffset);
    // Serialize message field [distance_imm]
    bufferOffset = _serializer.float64(obj.distance_imm, buffer, bufferOffset);
    // Serialize message field [distance_singer]
    bufferOffset = _serializer.float64(obj.distance_singer, buffer, bufferOffset);
    // Serialize message field [target_x]
    bufferOffset = _serializer.float64(obj.target_x, buffer, bufferOffset);
    // Serialize message field [target_y]
    bufferOffset = _serializer.float64(obj.target_y, buffer, bufferOffset);
    // Serialize message field [uav_x]
    bufferOffset = _serializer.float64(obj.uav_x, buffer, bufferOffset);
    // Serialize message field [uav_y]
    bufferOffset = _serializer.float64(obj.uav_y, buffer, bufferOffset);
    // Serialize message field [real_target_x]
    bufferOffset = _serializer.float64(obj.real_target_x, buffer, bufferOffset);
    // Serialize message field [real_target_y]
    bufferOffset = _serializer.float64(obj.real_target_y, buffer, bufferOffset);
    // Serialize message field [estimated_target_x]
    bufferOffset = _serializer.float64(obj.estimated_target_x, buffer, bufferOffset);
    // Serialize message field [estimated_target_y]
    bufferOffset = _serializer.float64(obj.estimated_target_y, buffer, bufferOffset);
    // Serialize message field [Vx]
    bufferOffset = _serializer.float64(obj.Vx, buffer, bufferOffset);
    // Serialize message field [Vy]
    bufferOffset = _serializer.float64(obj.Vy, buffer, bufferOffset);
    // Serialize message field [Vz]
    bufferOffset = _serializer.float64(obj.Vz, buffer, bufferOffset);
    // Serialize message field [Hdg_rate]
    bufferOffset = _serializer.float64(obj.Hdg_rate, buffer, bufferOffset);
    // Serialize message field [mode]
    bufferOffset = _serializer.int64(obj.mode, buffer, bufferOffset);
    // Serialize message field [horizontal_distance]
    bufferOffset = _serializer.float64(obj.horizontal_distance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Publish_Data
    let len;
    let data = new Publish_Data(null);
    // Deserialize message field [id]
    data.id = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [real_distance]
    data.real_distance = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [estimated_distance]
    data.estimated_distance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [depth]
    data.depth = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [depth_distance]
    data.depth_distance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [use_depth]
    data.use_depth = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [center_x]
    data.center_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [center_y]
    data.center_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [error_heading]
    data.error_heading = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [error_altitude]
    data.error_altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [controller_error]
    data.controller_error = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [control_output]
    data.control_output = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_lost]
    data.target_lost = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [target_detected]
    data.target_detected = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [distance_cnst]
    data.distance_cnst = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distance_imm]
    data.distance_imm = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distance_singer]
    data.distance_singer = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_x]
    data.target_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [target_y]
    data.target_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [uav_x]
    data.uav_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [uav_y]
    data.uav_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [real_target_x]
    data.real_target_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [real_target_y]
    data.real_target_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [estimated_target_x]
    data.estimated_target_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [estimated_target_y]
    data.estimated_target_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vx]
    data.Vx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vy]
    data.Vy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vz]
    data.Vz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Hdg_rate]
    data.Hdg_rate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mode]
    data.mode = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [horizontal_distance]
    data.horizontal_distance = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.real_distance.length;
    return length + 231;
  }

  static datatype() {
    // Returns string type for a message object
    return 'detection_msgs/Publish_Data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd24cf57b017f31ef8582817de6a3c884';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 id
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Publish_Data(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.real_distance !== undefined) {
      resolved.real_distance = msg.real_distance;
    }
    else {
      resolved.real_distance = []
    }

    if (msg.estimated_distance !== undefined) {
      resolved.estimated_distance = msg.estimated_distance;
    }
    else {
      resolved.estimated_distance = 0.0
    }

    if (msg.depth !== undefined) {
      resolved.depth = msg.depth;
    }
    else {
      resolved.depth = 0.0
    }

    if (msg.depth_distance !== undefined) {
      resolved.depth_distance = msg.depth_distance;
    }
    else {
      resolved.depth_distance = 0.0
    }

    if (msg.use_depth !== undefined) {
      resolved.use_depth = msg.use_depth;
    }
    else {
      resolved.use_depth = false
    }

    if (msg.center_x !== undefined) {
      resolved.center_x = msg.center_x;
    }
    else {
      resolved.center_x = 0.0
    }

    if (msg.center_y !== undefined) {
      resolved.center_y = msg.center_y;
    }
    else {
      resolved.center_y = 0.0
    }

    if (msg.error_heading !== undefined) {
      resolved.error_heading = msg.error_heading;
    }
    else {
      resolved.error_heading = 0.0
    }

    if (msg.error_altitude !== undefined) {
      resolved.error_altitude = msg.error_altitude;
    }
    else {
      resolved.error_altitude = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
    }

    if (msg.controller_error !== undefined) {
      resolved.controller_error = msg.controller_error;
    }
    else {
      resolved.controller_error = 0.0
    }

    if (msg.control_output !== undefined) {
      resolved.control_output = msg.control_output;
    }
    else {
      resolved.control_output = 0.0
    }

    if (msg.target_lost !== undefined) {
      resolved.target_lost = msg.target_lost;
    }
    else {
      resolved.target_lost = false
    }

    if (msg.target_detected !== undefined) {
      resolved.target_detected = msg.target_detected;
    }
    else {
      resolved.target_detected = false
    }

    if (msg.distance_cnst !== undefined) {
      resolved.distance_cnst = msg.distance_cnst;
    }
    else {
      resolved.distance_cnst = 0.0
    }

    if (msg.distance_imm !== undefined) {
      resolved.distance_imm = msg.distance_imm;
    }
    else {
      resolved.distance_imm = 0.0
    }

    if (msg.distance_singer !== undefined) {
      resolved.distance_singer = msg.distance_singer;
    }
    else {
      resolved.distance_singer = 0.0
    }

    if (msg.target_x !== undefined) {
      resolved.target_x = msg.target_x;
    }
    else {
      resolved.target_x = 0.0
    }

    if (msg.target_y !== undefined) {
      resolved.target_y = msg.target_y;
    }
    else {
      resolved.target_y = 0.0
    }

    if (msg.uav_x !== undefined) {
      resolved.uav_x = msg.uav_x;
    }
    else {
      resolved.uav_x = 0.0
    }

    if (msg.uav_y !== undefined) {
      resolved.uav_y = msg.uav_y;
    }
    else {
      resolved.uav_y = 0.0
    }

    if (msg.real_target_x !== undefined) {
      resolved.real_target_x = msg.real_target_x;
    }
    else {
      resolved.real_target_x = 0.0
    }

    if (msg.real_target_y !== undefined) {
      resolved.real_target_y = msg.real_target_y;
    }
    else {
      resolved.real_target_y = 0.0
    }

    if (msg.estimated_target_x !== undefined) {
      resolved.estimated_target_x = msg.estimated_target_x;
    }
    else {
      resolved.estimated_target_x = 0.0
    }

    if (msg.estimated_target_y !== undefined) {
      resolved.estimated_target_y = msg.estimated_target_y;
    }
    else {
      resolved.estimated_target_y = 0.0
    }

    if (msg.Vx !== undefined) {
      resolved.Vx = msg.Vx;
    }
    else {
      resolved.Vx = 0.0
    }

    if (msg.Vy !== undefined) {
      resolved.Vy = msg.Vy;
    }
    else {
      resolved.Vy = 0.0
    }

    if (msg.Vz !== undefined) {
      resolved.Vz = msg.Vz;
    }
    else {
      resolved.Vz = 0.0
    }

    if (msg.Hdg_rate !== undefined) {
      resolved.Hdg_rate = msg.Hdg_rate;
    }
    else {
      resolved.Hdg_rate = 0.0
    }

    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = 0
    }

    if (msg.horizontal_distance !== undefined) {
      resolved.horizontal_distance = msg.horizontal_distance;
    }
    else {
      resolved.horizontal_distance = 0.0
    }

    return resolved;
    }
};

module.exports = Publish_Data;
