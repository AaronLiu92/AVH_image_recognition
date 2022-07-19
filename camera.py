#coding:utf-8
import cv2

camSet = 'v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480,framerate=25/1 ! videoconvert ! appsink'
cap = cv2.VideoCapture(camSet)
flag = cap.isOpened()

index = 1
while(flag):
    ret, frame = cap.read()
    cv2.imshow("myCam",frame)
    cv2.moveWindow('myCam', 0, 0)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):     #按下s键，进入下面的保存图片操作
        cv2.imwrite(str(index) + ".jpg", frame)
        print(cap.get(3))
        print(cap.get(4))
        print("save" + str(index) + ".jpg successfuly!")
        print("-------------------------")
        index += 1
    elif k == ord('q'):     #按下q键，程序退出
        break
cap.release()
cv2.destroyAllWindows()
