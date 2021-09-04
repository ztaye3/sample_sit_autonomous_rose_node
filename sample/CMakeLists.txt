cmake_minimum_required(VERSION 2.8.3)
project(sample)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)


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

install(TARGETS talker_cpp
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_python_setup()

install(PROGRAMS
   scripts/talker.py

   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

if (CATKIN_ENABLE_TESTING)
  add_subdirectory(tests)
endif()

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
