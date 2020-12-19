#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
import time

num1 = 0
num2 = 0

def isprime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
            else:
                return True

    else:
        return False

def print_prime(num1,num2):
    if isprime(num1) and isprime(num2):
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif isprime(num1):
        print(num1)
    elif isprime(num2):
        print(num2)
    else:
        if num1>num2:
            print(num1)
        else:
            print(num2)
    
def callback(data):
    global num1
    num1 = data.data
    rospy.loginfo("got num1 = %d", data.data)
    
def callback2(data):
    global num2
    num2 = data.data
    rospy.loginfo("got num2 = %d", data.data)
    print_prime(num1,num2)

def listener():
    global num1,num2
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('topic_A', Int64, callback)
    rospy.Subscriber('topic_B', Int64, callback2)
    rospy.spin()
    

if __name__ == '__main__':
    listener()
