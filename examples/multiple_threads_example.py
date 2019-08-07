#!/usr/bin/env python
# coding: utf-8

import rospy
import threading
from traceback_publisher import TracebackPublisher, TracebackThread


class MultipleThreadsExample(object):

    TAG = "MultipleThreadsExample"

    def __init__(self):
        rospy.init_node("multiple_threads")
        self.tracebackPublisher = TracebackPublisher()
        rospy.loginfo("{} Starting thread loop...".format(self.TAG))
        self.threadLoop()

    def thread(self):
        rospy.loginfo("{}::thread Raising exception from thread '{}'".format(self.TAG, threading.current_thread().ident))
        raise Exception("Some exception in a thread")

    def threadLoop(self):
        while not rospy.is_shutdown():
            rospy.sleep(3.0)
            thread = TracebackThread(target=self.thread)
            thread.setDaemon(True)
            thread.start()


if __name__ == "__main__":
    multipleThreadsExample = MultipleThreadsExample()
    rospy.spin()
