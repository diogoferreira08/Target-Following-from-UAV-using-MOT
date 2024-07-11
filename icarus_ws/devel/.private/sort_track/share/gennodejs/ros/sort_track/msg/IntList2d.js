// Auto-generated. Do not edit!

// (in-package sort_track.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let IntList = require('./IntList.js');

//-----------------------------------------------------------

class IntList2d {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data2d = null;
    }
    else {
      if (initObj.hasOwnProperty('data2d')) {
        this.data2d = initObj.data2d
      }
      else {
        this.data2d = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IntList2d
    // Serialize message field [data2d]
    // Serialize the length for message field [data2d]
    bufferOffset = _serializer.uint32(obj.data2d.length, buffer, bufferOffset);
    obj.data2d.forEach((val) => {
      bufferOffset = IntList.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IntList2d
    let len;
    let data = new IntList2d(null);
    // Deserialize message field [data2d]
    // Deserialize array length for message field [data2d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.data2d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.data2d[i] = IntList.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.data2d.forEach((val) => {
      length += IntList.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sort_track/IntList2d';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1d7b9704b92687ed27b85eeae87a237e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    IntList[] data2d
    
    ================================================================================
    MSG: sort_track/IntList
    int32[] data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IntList2d(null);
    if (msg.data2d !== undefined) {
      resolved.data2d = new Array(msg.data2d.length);
      for (let i = 0; i < resolved.data2d.length; ++i) {
        resolved.data2d[i] = IntList.Resolve(msg.data2d[i]);
      }
    }
    else {
      resolved.data2d = []
    }

    return resolved;
    }
};

module.exports = IntList2d;
