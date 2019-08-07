#!/usr/bin/env python
# coding: utf-8

import rospy
from traceback_publisher import TracebackPublisher


class MainThreadExample(object):

    TAG = "MainThreadExample"

    def __init__(self):
        rospy.init_node("main_thread")
        self.tracebackPublisher = TracebackPublisher()
        rospy.loginfo("{} Starting exception loop...".format(self.TAG))
        self.exceptionLoop()

    def exceptionLoop(self):
        while not rospy.is_shutdown():
            rospy.sleep(3.0)
            rospy.loginfo("{}::exceptionLoop Raising error".format(self.TAG))
            raise Exception("Some exception")


if __name__ == "__main__":
    mainThreadExample = MainThreadExample()
    rospy.spin()
