# -*- coding:utf-8
import numpy as np
import multiprocessing
from multiprocessing import Process ,Queue
import random
import cv2

def run1(que,cap):

  while 1:
    ret,img = cap.read()
    for i in  range(200):
      for j in range(200):
        for k in  range(3):
          img[j,i,k] = random.randint(0,255)
    

    lenth = que.qsize()
    print ("que lenth: ",lenth)

    if lenth >2:
      for i in range(lenth-2):
        frame = que.get()   #清除缓存
    que.put(img)
    #pipe.send(img_q)
    cv2.imshow("show",img)

    cv2.waitKey(1000/23)
  cv2.destroyAllWindows()
  cap.release()


def test_1(que,cap):
  run1(que)



def test_2(que):
  while 1:
    img = que.get()
    #img = pipe.recv()
    #img = cv2.resize(img,(360,240))
    cv2.imshow("show2",img)
    key = cv2.waitKey(1000/23)
    if key == 27:
      break
  cv2.destroyAllWindows()


def cmd_send():
  pass
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    que = manager.Queue()
    # que = Queue()
    test1_start = 1
    test2_start = 1

    cap= cv2.VideoCapture(0)

    t1 = Process(target=run1,args=(que,cap,))
    # t2 = Process(target=test_2,args=(que,))

    t1.start()
    # t2.start()

    test_2(que)
    # 
    t1.terminate()
