#!/usr/bin/env python
"""
Extract Pose for every message and take the average of every N poses and write it to a file. N is the ratio of image messages to Pose messages
"""
from __future__ import print_function
import math
import csv

# OpenVR package
#import openvr_ros

# ROS packages
import roslib
import rospy
import rosbag
import tf
import argparse

# ROS messages
from geometry_msgs.msg import *
from std_msgs.msg import *
from openvr_ros.msg import TrackedDevicePose

# Constants


def main():
	"""
	Extract the csv file with pose annotations
	"""
	parser = argparse.ArgumentParser(description="Extract pose annotations from a ROS bag.")
	parser.add_argument("--bag_file",required="true", help="Input ROS bag.")
	args = parser.parse_args()

	print(args.bag_file)
	bag = rosbag.Bag(args.bag_file, "r")
	count = 0
	rowx = []
	rowy = []
	rowz = []
	rowox = []
	rowoy = []
	rowoz = []
	rowow = []
# Add angles and twist information as well
	for topic,msg,t in bag.read_messages(topics=['/track_publisher/tracked_device_pose']):
		rowx.append(msg.pose.position.x)
		rowy.append(msg.pose.position.y)
		rowz.append(msg.pose.position.z)
		rowox.append(msg.pose.orientation.x)
		rowoy.append(msg.pose.orientation.y)
		rowoz.append(msg.pose.orientation.z)
		rowow.append(msg.pose.orientation.w)
		print(msg.pose)
	bag.close()
	print(count)
	rowxavg = sample_row(rowx)
	rowyavg = sample_row(rowy)
	rowzavg = sample_row(rowz)
	rowoxavg = sample_row(rowox)	
	rowoyavg = sample_row(rowoy)	
	rowozavg = sample_row(rowoz)		
	rowowavg = sample_row(rowow)
	with open('All_poses.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(rowxavg)
		writer.writerow(rowyavg)
		writer.writerow(rowzavg)
		writer.writerow(rowoxavg)
		writer.writerow(rowoyavg)
		writer.writerow(rowozavg)
		writer.writerow(rowowavg)
	return



def sample_row(row):
	rowavg = []
	y = len(row)//18 + len(row)%18	
	for i in range(0,y):	
		smallrow = sum(row[i:i+18])/18
		rowavg.append(smallrow)
	print(len(rowavg))
	return rowavg	


if __name__ == '__main__':
    main()
