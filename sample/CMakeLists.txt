cmake_minimum_required(VERSION 2.8.3)
project(sample)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
## Declare ROS messages and services
# add_message_files(DIRECTORY msg FILES Num.msg)
# add_service_files(DIRECTORY srv FILES AddTwoInts.srv)

## Generate added messages and services
# generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

add_executable(talker_cpp src/talker.cpp)
target_link_libraries(talker_cpp ${catkin_LIBRARIES})

# add_executable(listener src/listener.cpp)
# target_link_libraries(listener ${catkin_LIBRARIES})

