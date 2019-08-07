cmake_minimum_required(VERSION 2.8.3)
project(traceback_publisher)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package()


###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############

install(PROGRAMS
  examples/main_thread_example.py
  examples/multiple_threads_example.py
  examples/subscriber_thread_example.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
