# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sort_track: 2 messages, 0 services")

set(MSG_I_FLAGS "-Isort_track:/home/diogocf/icarus_ws/src/sort_track/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Isort_track:/home/diogocf/icarus_ws/src/sort_track/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sort_track_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_custom_target(_sort_track_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sort_track" "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" ""
)

get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_custom_target(_sort_track_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sort_track" "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" "sort_track/IntList"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sort_track
)
_generate_msg_cpp(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg"
  "${MSG_I_FLAGS}"
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sort_track
)

### Generating Services

### Generating Module File
_generate_module_cpp(sort_track
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sort_track
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(sort_track_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(sort_track_generate_messages sort_track_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_cpp _sort_track_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_cpp _sort_track_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sort_track_gencpp)
add_dependencies(sort_track_gencpp sort_track_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sort_track_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sort_track
)
_generate_msg_eus(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg"
  "${MSG_I_FLAGS}"
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sort_track
)

### Generating Services

### Generating Module File
_generate_module_eus(sort_track
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sort_track
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(sort_track_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(sort_track_generate_messages sort_track_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_eus _sort_track_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_eus _sort_track_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sort_track_geneus)
add_dependencies(sort_track_geneus sort_track_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sort_track_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sort_track
)
_generate_msg_lisp(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg"
  "${MSG_I_FLAGS}"
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sort_track
)

### Generating Services

### Generating Module File
_generate_module_lisp(sort_track
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sort_track
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(sort_track_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(sort_track_generate_messages sort_track_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_lisp _sort_track_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_lisp _sort_track_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sort_track_genlisp)
add_dependencies(sort_track_genlisp sort_track_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sort_track_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sort_track
)
_generate_msg_nodejs(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg"
  "${MSG_I_FLAGS}"
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sort_track
)

### Generating Services

### Generating Module File
_generate_module_nodejs(sort_track
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sort_track
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(sort_track_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(sort_track_generate_messages sort_track_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_nodejs _sort_track_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_nodejs _sort_track_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sort_track_gennodejs)
add_dependencies(sort_track_gennodejs sort_track_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sort_track_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track
)
_generate_msg_py(sort_track
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg"
  "${MSG_I_FLAGS}"
  "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track
)

### Generating Services

### Generating Module File
_generate_module_py(sort_track
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(sort_track_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(sort_track_generate_messages sort_track_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_py _sort_track_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/diogocf/icarus_ws/src/sort_track/msg/IntList2d.msg" NAME_WE)
add_dependencies(sort_track_generate_messages_py _sort_track_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sort_track_genpy)
add_dependencies(sort_track_genpy sort_track_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sort_track_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sort_track)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sort_track
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(sort_track_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sort_track_generate_messages_cpp)
  add_dependencies(sort_track_generate_messages_cpp sort_track_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sort_track)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sort_track
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(sort_track_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sort_track_generate_messages_eus)
  add_dependencies(sort_track_generate_messages_eus sort_track_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sort_track)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sort_track
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(sort_track_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sort_track_generate_messages_lisp)
  add_dependencies(sort_track_generate_messages_lisp sort_track_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sort_track)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sort_track
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(sort_track_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sort_track_generate_messages_nodejs)
  add_dependencies(sort_track_generate_messages_nodejs sort_track_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sort_track
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sort_track_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sort_track_generate_messages_py)
  add_dependencies(sort_track_generate_messages_py sort_track_generate_messages_py)
endif()
