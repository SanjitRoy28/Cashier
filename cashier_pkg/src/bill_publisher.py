#!/usr/bin/env python3

import rospy
from cashier_pkg.msg import Bill

def publish_bill():
    rospy.init_node('bill_publisher', anonymous=True)
    pub = rospy.Publisher('bill_topic', Bill, queue_size=10)
    rate = rospy.Rate(1)  # Publish once per second

    while not rospy.is_shutdown():
        bill = Bill()
        bill.bill_number = 1
        bill.time_stamp = rospy.get_rostime()
        bill.quantity = 5
        bill.price = 10
        bill.total = bill.quantity * bill.price

        pub.publish(bill)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_bill()
    except rospy.ROSInterruptException:
        pass
