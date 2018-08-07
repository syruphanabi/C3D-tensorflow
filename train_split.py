#! /usr/bin/env python    
#coding=utf-8    
import cv2    
import numpy as np    
import os

path = '../data/ShotMoment/'
files = os.listdir(path)
for file in files:
    if file[-10:-4] == "jiance":
        continue
    else:
        os.makedirs(path+file[:-4]+"_split_videos")

        videoCapture = cv2.VideoCapture(path+file) # 从文件读取视频    
        # 判断视频是否打开    
        if (videoCapture.isOpened()):    
            print('Open')    
        else:    
            print('Fail to open!')    

        print ('总帧数：',videoCapture.get(cv2.CAP_PROP_FRAME_COUNT))
        print ('帧率：',videoCapture.get(cv2.CAP_PROP_FPS))
            
        fps = videoCapture.get(cv2.CAP_PROP_FPS)  #获取原视频的帧率    
            
        # size = (int(600), int(1536))#自定义需要截取的画面的大小    
        size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))#获取原视频帧的大小    

        success = True
        frame_count = 0
        all_frame = []
        #videoWriter = cv2.VideoWriter('/Users/kj-xhzy/Documents/004_1_copy2.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)    
        while(success):
            success, frame = videoCapture.read()
            all_frame.append(frame)
            # params = []
            # #params.append(cv.CV_IMWRITE_PXM_BINARY)
            # params.append(1)
            # cv2.imwrite("/Users/kj-xhzy/Documents/test1_frame/video" + "_%d.jpg" % frame_count, frame, params)
            # cv2.imwrite("/Users/kj-xhzy/Documents/test1jiance_frame/video" + "_%d.jpg" % frame_count, frame)

            frame_count = frame_count + 1

        for i in range(0,frame_count,10):
            videoWriter = cv2.VideoWriter(path+file[:-4]+"_split_videos/"+file[:-4]+"_%d.mp4" % i, cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)
            for j in range(i, min(i+20, frame_count)):
                videoWriter.write(all_frame[j])
            videoWriter.release()

        videoCapture.release()