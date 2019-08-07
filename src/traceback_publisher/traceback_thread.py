#!/usr/bin/env python
# coding: utf-8

import rospy
import traceback
from threading import Thread


class TracebackThread(Thread):

    def run(self):
        try:
            super(TracebackThread, self).run()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            rospy.logerr("Error in a TracebackThread:\n{}".format(traceback.format_exc()))
