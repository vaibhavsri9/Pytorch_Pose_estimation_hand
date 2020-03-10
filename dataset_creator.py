#!/usr/bin/env python

"""
Extract Pose and Images and create a dataset
"""

from __future__ import print_function

import os
import argparse
import sys

import cv2

#for csv file processing
import math
import csv

#Import tf
import tf

import roslib
import rospy
import rosbag

#ROS messages
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import *
from std_msgs.msg import *
from openvr_ros.msg import TrackedDevicePose

def main():
	
	parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
	parser.add_argument("--bag_file", required="true", help="Input ROS bag.")
	parser.add_argument("--output_dir", help="Output directory.", default="/home/vaibhav/test")	
	parser.add_argument("--image_topic", help="Image topic.", default="/camera/rgb/image_rect_color/compressed")
	parser.add_argument("--pose_topic", help="Pose topic.", default="/track_publisher/tracked_device_pose")
	args = parser.parse_args()
#	image_topic = "/camera/rgb/image_rect_color/compressed"    
	num_img_extracted = image_info_extractor(args)
	num_pose_extracted = pose_info_extractor(args)
	print(num_img_extracted,num_pose_extracted)
	Ratio_sample = int(num_pose_extracted/num_img_extracted)-1
	print(Ratio_sample)
        
	return



def image_info_extractor(args):
	bag = rosbag.Bag(args.bag_file, "r")
    	bridge = CvBridge()
    	image_count = 0

    	for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        	cv_img = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="passthrough")
        	#cv2.imshow('mat',cv_img)
		#cv2.waitKey(3)
		filename=args.output_dir + '/frame_{}.png'.format(image_count)
		print(filename)
        	cv2.imwrite(filename, cv_img)
        	image_count += 1
	bag.close()

    	return image_count


def pose_info_extractor(args):
	bag = rosbag.Bag(args.bag_file, "r")
	pose_count = 0
	rowx = []
	rowy = []
	rowz = []
	rowox = []
	rowoy = []
	rowoz = []
	rowow = []
# Add twist information as required	
	for topic,msg,t in bag.read_messages(topics=[args.pose_topic]):		
		rowx.append(msg.pose.position.x)		
		rowy.append(msg.pose.position.y)
		rowz.append(msg.pose.position.z)
		rowox.append(msg.pose.orientation.x)
		rowoy.append(msg.pose.orientation.y)
		rowoz.append(msg.pose.orientation.z)		
		rowow.append(msg.pose.orientation.w)
		pose_count += 1		
		print(msg.pose)			
	bag.close()
	print(pose_count)
	with open('All_poses.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(rowx)
		writer.writerow(rowy)
		writer.writerow(rowz)
		writer.writerow(rowox)
		writer.writerow(rowoy)
		writer.writerow(rowoz)
		writer.writerow(rowow)
	
	return pose_count

"""
def sampler(N):
	with open('All_poses.csv', 'r') as f:
		reader= csv.reader(f)
		for row in reader
"""



if __name__ == '__main__':
	main()
