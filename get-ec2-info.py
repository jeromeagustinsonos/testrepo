'''
Created on Oct 23, 2017

@author: jerome.agustin
'''
import boto3
import sys
import awscli

#Prompt for instance ID 
#user_instanceID = raw_input("Please enter in the instanceID: ")

#Prompt for region us-east-1, us-east-2, us-west-1, us-west-2, etc...
user_regionID = raw_input("Please enter in the region: ")

ec2 = boto3.resource('ec2',region_name=user_regionID)

instances = ec2.instances.filter(
   Filters=[{'Name': 'instance-state-name', 'Values': ['running']
             }])

for instance in instances:
    print "The instance ID is: " + instance.id 
    
    for tag in instance.tags:
       for value, key in tag.iteritems():
           print value + "=" + key + "\n"
    
