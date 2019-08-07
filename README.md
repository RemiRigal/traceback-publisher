# Traceback publisher

Simple ROS library that allows any python-based node to publish errors into the `/rosout` topic. It can work both on main and child threads.


### TracebackPublisher

Can be used simply by adding these lines to any Python script:
```python
from traceback_publisher import TracebackPublisher

TracebackPublisher()
```

It also features a separate publication of stacktraces in a choosable topic:
```python
import rospy
from traceback_publisher import TracebackPublisher

# The ROS node needs to be initialized before instantiating the traceback publisher
rospy.init_node("my_node")
TracebackPublisher(publishTopic="/stacktraces")
```


### TracebackThread 

As the `excepthook` only works on the main thread, a `threading.Thread` subclass `TracebackThread` can be used:
```python
from traceback_publisher import TracebackThread

# Will log any threaded error to /rosout
TracebackThread(target=someFunction).start()
```