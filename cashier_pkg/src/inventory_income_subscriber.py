#!/usr/bin/env python3

import rospy
from cashier_pkg.msg import Bill
from cashier_pkg.srv import UpdateParams

inventory = rospy.get_param('~inventory', 0)
income = rospy.get_param('~income', 0)

def bill_callback(data):
    global inventory, income
    inventory -= data.quantity
    income += data.total

def update_params_callback(request):
    global inventory, income
    inventory += request.quantity
    income += request.total

    return {'success': True, 'message': 'Parameters updated successfully'}

def inventory_income_subscriber():
    rospy.init_node('inventory_income_subscriber', anonymous=True)
    rospy.Subscriber('bill_topic', Bill, bill_callback)
    rospy.Service('update_params', UpdateParams, update_params_callback)
    rospy.set_param('~inventory', inventory)
    rospy.set_param('~income', income)
    rospy.spin()

if __name__ == '__main__':
    try:
        inventory_income_subscriber()
    except rospy.ROSInterruptException:
        pass
