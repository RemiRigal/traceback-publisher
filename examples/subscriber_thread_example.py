#!/usr/bin/env python
# coding: utf-8

import rospy
import threading
from std_msgs.msg import Empty
from traceback_publisher import TracebackPublisher


class SubscriberThreadExample(object):

    TAG = "SubscriberThreadExample"

    def __init__(self):
        rospy.init_node("subscriber_thread")
        self.tracebackPublisher = TracebackPublisher()
        # Publisher and subscriber pair
        self.subscriber = rospy.Subscriber("/some_data", Empty, self.onMessage)
        self.publisher = rospy.Publisher("/some_data", Empty, queue_size=5)
        rospy.loginfo("{} Starting publish loop...".format(self.TAG))
        self.publishLoop()

    def onMessage(self, message):
        rospy.loginfo("{}::onMessage Got message in thread '{}', raising exception".format(self.TAG, threading.current_thread().ident))
        # This exception will be caught by the ROS Subscriber stack
        raise Exception("Some exception in a subscriber callback")

    def publishLoop(self):
        while not rospy.is_shutdown():
            rospy.sleep(3.0)
            self.publisher.publish(Empty())


if __name__ == "__main__":
    subscriberThreadExample = SubscriberThreadExample()
    rospy.spin()
