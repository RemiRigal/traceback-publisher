#!/usr/bin/env python
# coding: utf-8

import sys
import rospy
import traceback
import StringIO
from std_msgs.msg import String


class TracebackPublisher(object):

    TAG = "TracebackPublisher"

    def __init__(self, publishTopic=None):
        sys.excepthook = self.exceptHook
        self.publisher = None
        if publishTopic is not None:
            self.publisher = rospy.Publisher(publishTopic, String, queue_size=20)

    def exceptHook(self, exctype, value, tb):
        tracebackOutput = StringIO.StringIO()
        traceback.print_tb(tb, None, tracebackOutput)
        rospy.logerr("Error in main thread:\n{}".format(tracebackOutput.getvalue()))
        if self.publisher is not None:
            self.publisher.publish(String(tracebackOutput.getvalue()))
