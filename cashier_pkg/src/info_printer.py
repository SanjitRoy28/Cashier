#!/usr/bin/env python3

import rospy
from cashier_pkg.msg import Bill

def info_printer():
    rospy.init_node('info_printer')
    rospy.wait_for_message('bill_topic', Bill, timeout=1)
    rospy.wait_for_service('update_params')

    print('Last Bill Message:')
    print(rospy.get_param('last_bill'))

    print('\nCurrent Inventory:')
    print(rospy.get_param('inventory'))

    print('\nCurrent Income:')
    print(rospy.get_param('income'))

if __name__ == '__main__':
    try:
        info_printer()
    except rospy.ROSInterruptException:
        pass
