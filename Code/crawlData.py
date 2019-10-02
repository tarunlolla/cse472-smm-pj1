#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:34:47 2019

@author: tarunlolla
"""

import tweepy 
import csv
import os
import test_connection

def find_friends(user,csvwriter,api):
    #This function builds a tree of all Friends of a given user and writes the pair to the csv file.
    for friend in api.friends(screen_name=str(user)):
        csvwriter.writerow([user,friend.screen_name])


def main():
    keys_file=open("conn_details.txt",'r')
    lines=keys_file.readlines()
    conn_details=dict()
    for line in lines:
        a=line.rstrip().split('=')
        conn_details[a[0]] = a[1]
    keys_file.close()

    #If credentials are not entered in the file conn_details.txt, the below logic prompts the user to enter the same.
    if conn_details['consumer_key'] == '':
        conn_details['consumer_key'] = input("No Consumer Key found in file. Please enter a consumer key: ")
    if conn_details['consumer_secret'] == '':
        conn_details['consumer_secret'] = input("No Consumer Secret Key found in file. Please enter a consumer secret key: ")
    if conn_details['access_token'] == '':
        conn_details['access_token'] = input("No Access Token found in file. Please enter an Access Token: ")
    if conn_details['access_token_secret'] == '':
        conn_details['access_token_secret'] = input("No Secret Access Token found in file. Please enter a Secret Access Token: ")

    auth = tweepy.OAuthHandler(conn_details['consumer_key'], conn_details['consumer_secret'])
    auth.set_access_token(conn_details['access_token'], conn_details['access_token_secret'])
    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #Calls the fucntion tweepy_conn_test from the file test_connection.py to validate the user credentials

    test_connection.tweepy_conn_test(conn_details)

    user=api.me().screen_name

    if os.path.isfile('data.csv'):
        os.system('rm data.csv')
    os.system('touch data.csv')
    csvfile_write=open('data.csv','r+')
    csvwriter=csv.writer(csvfile_write)

    for friend in api.friends():
        csvwriter.writerow([user,friend.screen_name])
        find_friends(friend.screen_name,csvwriter,api)

    csvfile_write.close()

if __name__ == '__main__' :
    main()
