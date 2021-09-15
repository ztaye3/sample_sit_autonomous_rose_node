cmake_minimum_required(VERSION 2.8.3)
project(sample)

## Find catkin and any catkin packages
set(CATKIN_DEPS roscpp rospy std_msgs genmsg)
set(SYS_DEPS python-serial python-sys)
find_package(catkin REQUIRED COMPONENTS ${CATKIN_DEPS})


if (CMAKE_BUILD_TYPE STREQUAL "Debug")
  message(STATUS "Enabling coverage testing")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
endif()

if (NOT "${CMAKE_CXX_STANDARD_COMPUTED_DEFAULT}")
  message(STATUS "Changing CXX_STANDARD from C++98 to C++11")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif ("${CMAKE_CXX_STANDARD_COMPUTED_DEFAULT}" STREQUAL "98")
  message(STATUS "Changing CXX_STANDARD from C++98 to C++11")
  set(CMAKE_CXX_STANDARD 11)
endif()

## Declare ROS messages and services
# add_message_files(DIRECTORY msg FILES Num.msg)
# add_service_files(DIRECTORY srv FILES AddTwoInts.srv)

## Generate added messages and services
# generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(talker_cpp src/talker.cpp)
target_link_libraries(talker_cpp ${catkin_LIBRARIES})
set_target_properties(talker_cpp PROPERTIES OUTPUT_NAME talker_cpp PREFIX "")

add_executable(talker_c scripts/test.c)
target_link_libraries(talker_c ${catkin_LIBRARIES})
set_target_properties(talker_c PROPERTIES OUTPUT_NAME talker_c PREFIX "")

install(TARGETS talker_cpp
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_python_setup()

install(PROGRAMS
   scripts/talker.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )




