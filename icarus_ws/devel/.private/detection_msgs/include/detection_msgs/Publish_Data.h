// Generated by gencpp from file detection_msgs/Publish_Data.msg
// DO NOT EDIT!


#ifndef DETECTION_MSGS_MESSAGE_PUBLISH_DATA_H
#define DETECTION_MSGS_MESSAGE_PUBLISH_DATA_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace detection_msgs
{
template <class ContainerAllocator>
struct Publish_Data_
{
  typedef Publish_Data_<ContainerAllocator> Type;

  Publish_Data_()
    : id(0)
    , real_distance()
    , estimated_distance(0.0)
    , depth(0.0)
    , depth_distance(0.0)
    , use_depth(false)
    , center_x(0.0)
    , center_y(0.0)
    , error_heading(0.0)
    , error_altitude(0.0)
    , altitude(0.0)
    , controller_error(0.0)
    , control_output(0.0)
    , target_lost(false)
    , target_detected(false)
    , distance_cnst(0.0)
    , distance_imm(0.0)
    , distance_singer(0.0)
    , target_x(0.0)
    , target_y(0.0)
    , uav_x(0.0)
    , uav_y(0.0)
    , real_target_x(0.0)
    , real_target_y(0.0)
    , estimated_target_x(0.0)
    , estimated_target_y(0.0)
    , Vx(0.0)
    , Vy(0.0)
    , Vz(0.0)
    , Hdg_rate(0.0)
    , mode(0)
    , horizontal_distance(0.0)  {
    }
  Publish_Data_(const ContainerAllocator& _alloc)
    : id(0)
    , real_distance(_alloc)
    , estimated_distance(0.0)
    , depth(0.0)
    , depth_distance(0.0)
    , use_depth(false)
    , center_x(0.0)
    , center_y(0.0)
    , error_heading(0.0)
    , error_altitude(0.0)
    , altitude(0.0)
    , controller_error(0.0)
    , control_output(0.0)
    , target_lost(false)
    , target_detected(false)
    , distance_cnst(0.0)
    , distance_imm(0.0)
    , distance_singer(0.0)
    , target_x(0.0)
    , target_y(0.0)
    , uav_x(0.0)
    , uav_y(0.0)
    , real_target_x(0.0)
    , real_target_y(0.0)
    , estimated_target_x(0.0)
    , estimated_target_y(0.0)
    , Vx(0.0)
    , Vy(0.0)
    , Vz(0.0)
    , Hdg_rate(0.0)
    , mode(0)
    , horizontal_distance(0.0)  {
  (void)_alloc;
    }



   typedef int64_t _id_type;
  _id_type id;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _real_distance_type;
  _real_distance_type real_distance;

   typedef double _estimated_distance_type;
  _estimated_distance_type estimated_distance;

   typedef double _depth_type;
  _depth_type depth;

   typedef double _depth_distance_type;
  _depth_distance_type depth_distance;

   typedef uint8_t _use_depth_type;
  _use_depth_type use_depth;

   typedef double _center_x_type;
  _center_x_type center_x;

   typedef double _center_y_type;
  _center_y_type center_y;

   typedef double _error_heading_type;
  _error_heading_type error_heading;

   typedef double _error_altitude_type;
  _error_altitude_type error_altitude;

   typedef double _altitude_type;
  _altitude_type altitude;

   typedef double _controller_error_type;
  _controller_error_type controller_error;

   typedef double _control_output_type;
  _control_output_type control_output;

   typedef uint8_t _target_lost_type;
  _target_lost_type target_lost;

   typedef uint8_t _target_detected_type;
  _target_detected_type target_detected;

   typedef double _distance_cnst_type;
  _distance_cnst_type distance_cnst;

   typedef double _distance_imm_type;
  _distance_imm_type distance_imm;

   typedef double _distance_singer_type;
  _distance_singer_type distance_singer;

   typedef double _target_x_type;
  _target_x_type target_x;

   typedef double _target_y_type;
  _target_y_type target_y;

   typedef double _uav_x_type;
  _uav_x_type uav_x;

   typedef double _uav_y_type;
  _uav_y_type uav_y;

   typedef double _real_target_x_type;
  _real_target_x_type real_target_x;

   typedef double _real_target_y_type;
  _real_target_y_type real_target_y;

   typedef double _estimated_target_x_type;
  _estimated_target_x_type estimated_target_x;

   typedef double _estimated_target_y_type;
  _estimated_target_y_type estimated_target_y;

   typedef double _Vx_type;
  _Vx_type Vx;

   typedef double _Vy_type;
  _Vy_type Vy;

   typedef double _Vz_type;
  _Vz_type Vz;

   typedef double _Hdg_rate_type;
  _Hdg_rate_type Hdg_rate;

   typedef int64_t _mode_type;
  _mode_type mode;

   typedef double _horizontal_distance_type;
  _horizontal_distance_type horizontal_distance;





  typedef boost::shared_ptr< ::detection_msgs::Publish_Data_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::detection_msgs::Publish_Data_<ContainerAllocator> const> ConstPtr;

}; // struct Publish_Data_

typedef ::detection_msgs::Publish_Data_<std::allocator<void> > Publish_Data;

typedef boost::shared_ptr< ::detection_msgs::Publish_Data > Publish_DataPtr;
typedef boost::shared_ptr< ::detection_msgs::Publish_Data const> Publish_DataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::detection_msgs::Publish_Data_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::detection_msgs::Publish_Data_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::detection_msgs::Publish_Data_<ContainerAllocator1> & lhs, const ::detection_msgs::Publish_Data_<ContainerAllocator2> & rhs)
{
  return lhs.id == rhs.id &&
    lhs.real_distance == rhs.real_distance &&
    lhs.estimated_distance == rhs.estimated_distance &&
    lhs.depth == rhs.depth &&
    lhs.depth_distance == rhs.depth_distance &&
    lhs.use_depth == rhs.use_depth &&
    lhs.center_x == rhs.center_x &&
    lhs.center_y == rhs.center_y &&
    lhs.error_heading == rhs.error_heading &&
    lhs.error_altitude == rhs.error_altitude &&
    lhs.altitude == rhs.altitude &&
    lhs.controller_error == rhs.controller_error &&
    lhs.control_output == rhs.control_output &&
    lhs.target_lost == rhs.target_lost &&
    lhs.target_detected == rhs.target_detected &&
    lhs.distance_cnst == rhs.distance_cnst &&
    lhs.distance_imm == rhs.distance_imm &&
    lhs.distance_singer == rhs.distance_singer &&
    lhs.target_x == rhs.target_x &&
    lhs.target_y == rhs.target_y &&
    lhs.uav_x == rhs.uav_x &&
    lhs.uav_y == rhs.uav_y &&
    lhs.real_target_x == rhs.real_target_x &&
    lhs.real_target_y == rhs.real_target_y &&
    lhs.estimated_target_x == rhs.estimated_target_x &&
    lhs.estimated_target_y == rhs.estimated_target_y &&
    lhs.Vx == rhs.Vx &&
    lhs.Vy == rhs.Vy &&
    lhs.Vz == rhs.Vz &&
    lhs.Hdg_rate == rhs.Hdg_rate &&
    lhs.mode == rhs.mode &&
    lhs.horizontal_distance == rhs.horizontal_distance;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::detection_msgs::Publish_Data_<ContainerAllocator1> & lhs, const ::detection_msgs::Publish_Data_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace detection_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::detection_msgs::Publish_Data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::detection_msgs::Publish_Data_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::detection_msgs::Publish_Data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::detection_msgs::Publish_Data_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::detection_msgs::Publish_Data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::detection_msgs::Publish_Data_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::detection_msgs::Publish_Data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d24cf57b017f31ef8582817de6a3c884";
  }

  static const char* value(const ::detection_msgs::Publish_Data_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd24cf57b017f31efULL;
  static const uint64_t static_value2 = 0x8582817de6a3c884ULL;
};

template<class ContainerAllocator>
struct DataType< ::detection_msgs::Publish_Data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "detection_msgs/Publish_Data";
  }

  static const char* value(const ::detection_msgs::Publish_Data_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::detection_msgs::Publish_Data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 id\n"
"float64[] real_distance\n"
"float64 estimated_distance\n"
"float64 depth\n"
"float64 depth_distance\n"
"bool use_depth\n"
"float64 center_x\n"
"float64 center_y\n"
"float64 error_heading\n"
"float64 error_altitude\n"
"float64 altitude\n"
"float64 controller_error\n"
"float64 control_output\n"
"bool target_lost\n"
"bool target_detected\n"
"float64 distance_cnst\n"
"float64 distance_imm\n"
"float64 distance_singer\n"
"float64 target_x\n"
"float64 target_y\n"
"float64 uav_x\n"
"float64 uav_y\n"
"float64 real_target_x\n"
"float64 real_target_y\n"
"float64 estimated_target_x\n"
"float64 estimated_target_y\n"
"float64 Vx\n"
"float64 Vy\n"
"float64 Vz\n"
"float64 Hdg_rate\n"
"int64 mode\n"
"float64 horizontal_distance\n"
;
  }

  static const char* value(const ::detection_msgs::Publish_Data_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::detection_msgs::Publish_Data_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.real_distance);
      stream.next(m.estimated_distance);
      stream.next(m.depth);
      stream.next(m.depth_distance);
      stream.next(m.use_depth);
      stream.next(m.center_x);
      stream.next(m.center_y);
      stream.next(m.error_heading);
      stream.next(m.error_altitude);
      stream.next(m.altitude);
      stream.next(m.controller_error);
      stream.next(m.control_output);
      stream.next(m.target_lost);
      stream.next(m.target_detected);
      stream.next(m.distance_cnst);
      stream.next(m.distance_imm);
      stream.next(m.distance_singer);
      stream.next(m.target_x);
      stream.next(m.target_y);
      stream.next(m.uav_x);
      stream.next(m.uav_y);
      stream.next(m.real_target_x);
      stream.next(m.real_target_y);
      stream.next(m.estimated_target_x);
      stream.next(m.estimated_target_y);
      stream.next(m.Vx);
      stream.next(m.Vy);
      stream.next(m.Vz);
      stream.next(m.Hdg_rate);
      stream.next(m.mode);
      stream.next(m.horizontal_distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Publish_Data_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::detection_msgs::Publish_Data_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::detection_msgs::Publish_Data_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int64_t>::stream(s, indent + "  ", v.id);
    s << indent << "real_distance[]" << std::endl;
    for (size_t i = 0; i < v.real_distance.size(); ++i)
    {
      s << indent << "  real_distance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.real_distance[i]);
    }
    s << indent << "estimated_distance: ";
    Printer<double>::stream(s, indent + "  ", v.estimated_distance);
    s << indent << "depth: ";
    Printer<double>::stream(s, indent + "  ", v.depth);
    s << indent << "depth_distance: ";
    Printer<double>::stream(s, indent + "  ", v.depth_distance);
    s << indent << "use_depth: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.use_depth);
    s << indent << "center_x: ";
    Printer<double>::stream(s, indent + "  ", v.center_x);
    s << indent << "center_y: ";
    Printer<double>::stream(s, indent + "  ", v.center_y);
    s << indent << "error_heading: ";
    Printer<double>::stream(s, indent + "  ", v.error_heading);
    s << indent << "error_altitude: ";
    Printer<double>::stream(s, indent + "  ", v.error_altitude);
    s << indent << "altitude: ";
    Printer<double>::stream(s, indent + "  ", v.altitude);
    s << indent << "controller_error: ";
    Printer<double>::stream(s, indent + "  ", v.controller_error);
    s << indent << "control_output: ";
    Printer<double>::stream(s, indent + "  ", v.control_output);
    s << indent << "target_lost: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.target_lost);
    s << indent << "target_detected: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.target_detected);
    s << indent << "distance_cnst: ";
    Printer<double>::stream(s, indent + "  ", v.distance_cnst);
    s << indent << "distance_imm: ";
    Printer<double>::stream(s, indent + "  ", v.distance_imm);
    s << indent << "distance_singer: ";
    Printer<double>::stream(s, indent + "  ", v.distance_singer);
    s << indent << "target_x: ";
    Printer<double>::stream(s, indent + "  ", v.target_x);
    s << indent << "target_y: ";
    Printer<double>::stream(s, indent + "  ", v.target_y);
    s << indent << "uav_x: ";
    Printer<double>::stream(s, indent + "  ", v.uav_x);
    s << indent << "uav_y: ";
    Printer<double>::stream(s, indent + "  ", v.uav_y);
    s << indent << "real_target_x: ";
    Printer<double>::stream(s, indent + "  ", v.real_target_x);
    s << indent << "real_target_y: ";
    Printer<double>::stream(s, indent + "  ", v.real_target_y);
    s << indent << "estimated_target_x: ";
    Printer<double>::stream(s, indent + "  ", v.estimated_target_x);
    s << indent << "estimated_target_y: ";
    Printer<double>::stream(s, indent + "  ", v.estimated_target_y);
    s << indent << "Vx: ";
    Printer<double>::stream(s, indent + "  ", v.Vx);
    s << indent << "Vy: ";
    Printer<double>::stream(s, indent + "  ", v.Vy);
    s << indent << "Vz: ";
    Printer<double>::stream(s, indent + "  ", v.Vz);
    s << indent << "Hdg_rate: ";
    Printer<double>::stream(s, indent + "  ", v.Hdg_rate);
    s << indent << "mode: ";
    Printer<int64_t>::stream(s, indent + "  ", v.mode);
    s << indent << "horizontal_distance: ";
    Printer<double>::stream(s, indent + "  ", v.horizontal_distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DETECTION_MSGS_MESSAGE_PUBLISH_DATA_H
