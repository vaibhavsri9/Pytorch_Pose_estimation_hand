#!/usr/bin/env python
"""
Extract Images from a topic
"""

from __future__ import print_function


import os
import argparse
import sys

import cv2
"""
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
"""

import roslib
import rospy
import rosbag
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

def main():

    """
    Extract a folder of images from a bag file
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("--bag_file",required="true", help="Input ROS bag.")
    parser.add_argument("--output_dir", help="Output directory.", default="/home/vaibhav/test")
    parser.add_argument("--image_topic", help="Image topic.", default="/camera/rgb/image_rect_color/compressed")

    args = parser.parse_args()

    print(args.bag_file,args.image_topic)

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 1

    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        cv_img = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="passthrough")
        #cv2.imshow('mat',cv_img)
	#cv2.waitKey(3)
	filename=args.output_dir + '/frame_{}.png'.format(count)
	print(filename)
        cv2.imwrite(filename, cv_img)
        count += 1
	print(count)

    bag.close()

    return

if __name__ == '__main__':
    main()
