import cv2
import numpy as np
import os

def classify_frame(hsv_image):
    brightness = np.mean(hsv_image[:,:,2])
    hue_histogram = cv2.calcHist([hsv_image],[0],None,[180],[0,180])
    if brightness > 200:
        return 'Day'
    elif brightness > 100 and hue_histogram[15:45].sum() > hue_histogram[90:120].sum():
        return 'Evening'
    else:
        return 'Night'

def visualizer(path):
    cam = cv2.VideoCapture(path)
    if(cam.isOpened() == False):
        print(" Error While Opening the Video File issue with the path")

    total_frames= 0
    counts = {'Day':0,'Evening':0,'Night':0}
    #Read the Video file frame by frame
    while(cam.isOpened()):
        ret,frame = cam.read()
        if(ret == True):          
            total_frames+=1            
            image_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)           
            time_period = classify_frame(image_hsv)
            counts[time_period]+=1
            if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
        else:
            break


    cam.release()
    cv2.destroyAllWindows()

    print(f'Total Number of frames : {total_frames}')

    #Calculating the percentage
    for time_period , count in counts.items():
        print(f'{time_period}: {count/total_frames * 100:.2f}%')




if __name__=="__main__":
    #Video Path
    path = "<PATH TO THE VIDEO FILE>"
    if not os.path.exists:
        print(f'Path not found')
    else:
        print(f'Path Found successfully')
    visualizer(path)
