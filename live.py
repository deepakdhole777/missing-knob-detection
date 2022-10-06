import cv2
import numpy as np
import basicutils

#cam

cam=cv2.VideoCapture(0)


while True:
    ret,frame=cam.read()
    if(ret==False):
        print("Cam prob!")
    else:    
        img1_color = frame
        gray=cv2.cvtColor(img1_color,cv2.COLOR_BGR2GRAY)
        part1 = cv2.imread("E:\Mini_Project\Dynamic\part1.jpg",0)
        part2 = cv2.imread("E:\Mini_Project\Dynamic\part2.jpg",0)
        part3 = cv2.imread("E:\Mini_Project\Dynamic\part3.jpg",0)
        blur1=cv2.medianBlur(part1,5)
        thresh1=cv2.adaptiveThreshold(blur1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        blur2=cv2.medianBlur(part2,5)
        thresh2=cv2.adaptiveThreshold(blur2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        blur3=cv2.medianBlur(part3,5)
        thresh3=cv2.adaptiveThreshold(blur3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #temp1= cv2.imread("F:/MINI_PROJECT-Inspectiondevice/temp1.jpg",0) 
        blur=cv2.medianBlur(gray,5)
        thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)    

        ##Part detection
        res1=cv2.matchTemplate(thresh.copy(),thresh1,cv2.TM_CCOEFF_NORMED)
        res2=cv2.matchTemplate(thresh.copy(),thresh2,cv2.TM_CCOEFF_NORMED)
        res3=cv2.matchTemplate(thresh.copy(),thresh3,cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(res1)
        (_, maxVal1, _, maxLoc1) = cv2.minMaxLoc(res2)
        (_, maxVal2, _, maxLoc2) = cv2.minMaxLoc(res3)
        if((maxVal>maxVal1)&(maxVal>maxVal2)):
            part="part 1"
        elif((maxVal1>maxVal)&(maxVal1>maxVal2)):
            part="part 2"
        elif((maxVal2>maxVal)&(maxVal2>maxVal1)):
            part="part 3"

        print(part)
        ##Screws

        ##part1
        #Original image processed
        
        #part='part 1'
        blur_img=cv2.medianBlur(gray,5)
        thresh_img=cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            
        

        if(part=="part 1"):

            s_temp1A=cv2.imread("E:\Mini_Project\Dynamic\sample1A.jpg",0)
            blur_s1A=cv2.medianBlur(s_temp1A,3)
            thresh1A=cv2.adaptiveThreshold(blur_s1A,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            h,w=s_temp1A.shape[:2]

            s_temp1B=cv2.imread("E:\Mini_Project\Dynamic\sample1B.jpg",0)
            blur_s1B=cv2.medianBlur(s_temp1B,5)
            thresh1B=cv2.adaptiveThreshold(blur_s1B,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            s_temp1C=cv2.imread("E:\Mini_Project\Dynamic\sample1C.jpg",0)
            blur_s1C=cv2.medianBlur(s_temp1C,5)
            thresh1C=cv2.adaptiveThreshold(blur_s1C,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            s_temp1D=cv2.imread("E:\Mini_Project\Dynamic\sample1D.jpg",0)
            blur_s1D=cv2.medianBlur(s_temp1D,5)
            thresh1D=cv2.adaptiveThreshold(blur_s1D,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        
            cv2.putText(frame,"PART 1",(468,410),cv2.FONT_HERSHEY_SIMPLEX , 1.5,(255,255,255))
            
            res_s1A=cv2.matchTemplate(thresh_img.copy(),thresh1A,cv2.TM_CCOEFF_NORMED)
            loc=np.where(res_s1A>=0.65)
            for pt in zip(*loc[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                cv2.putText(frame,"Screw A missing",(43,190),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))
                
            res_s1B=cv2.matchTemplate(thresh_img.copy(),thresh1B,cv2.TM_CCOEFF_NORMED)
            loc1=np.where(res_s1B>=0.75)
            for pt in zip(*loc1[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                cv2.putText(frame,"Screw B missing",(170,245),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))

            res_s1C=cv2.matchTemplate(thresh_img.copy(),thresh1C,cv2.TM_CCOEFF_NORMED)
            loc2=np.where(res_s1C>=0.75)
            for pt in zip(*loc2[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                cv2.putText(frame,"Screw C missing",(378,210),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))
                
            res_s1D=cv2.matchTemplate(thresh_img.copy(),thresh1D,cv2.TM_CCOEFF_NORMED)
            loc2=np.where(res_s1D>=0.75)
            for pt in zip(*loc2[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                cv2.putText(frame,"Screw D missing",(109,425),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))

        #part2

        elif(part=="part 2"):

            s_temp2A=cv2.imread("E:\Mini_Project\Dynamic\sample2A.jpg",0)
            blur_s2A=cv2.medianBlur(s_temp2A,5)
            thresh2A=cv2.adaptiveThreshold(blur_s2A,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            h,w=s_temp2A.shape[:2]

            s_temp2B=cv2.imread("E:\Mini_Project\Dynamic\sample2B.jpg",0)
            blur_s2B=cv2.medianBlur(s_temp2B,5)
            thresh2B=cv2.adaptiveThreshold(blur_s2B,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            s_temp2C=cv2.imread("E:\Mini_Project\Dynamic\sample2C.jpg",0)
            blur_s2C=cv2.medianBlur(s_temp2C,5)
            thresh2C=cv2.adaptiveThreshold(blur_s2C,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            cv2.putText(frame,"PART 2",(468,410),cv2.FONT_HERSHEY_SIMPLEX , 1.5,(255,255,255))
            
            res_s2A=cv2.matchTemplate(thresh_img.copy(),thresh2A,cv2.TM_CCOEFF_NORMED)
            loc=np.where(res_s2A>=0.75)
            for pt in zip(*loc[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                #cv2.putText(img1_color,"Screw A missing",pt,cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))
                
            res_s2B=cv2.matchTemplate(thresh_img.copy(),thresh2B,cv2.TM_CCOEFF_NORMED)
            loc1=np.where(res_s2B>=0.75)
            for pt in zip(*loc1[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                #cv2.putText(img1_color,"Screw B missing",(250,285),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))

            res_s2C=cv2.matchTemplate(thresh_img.copy(),thresh2C,cv2.TM_CCOEFF_NORMED)
            loc2=np.where(res_s2C>=0.75)
            for pt in zip(*loc2[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                #cv2.putText(img1_color,"Screw C missing",(518,230),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))


        elif(part=="part 3"):

            s_temp3A=cv2.imread("E:\Mini_Project\Dynamic\sample3A.jpg",0)
            blur_s3A=cv2.medianBlur(s_temp3A,5)
            thresh3A=cv2.adaptiveThreshold(blur_s3A,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            h,w=s_temp3A.shape[:2]

            s_temp3B=cv2.imread("E:\Mini_Project\Dynamic\sample3B.jpg",0)
            blur_s3B=cv2.medianBlur(s_temp3B,5)
            thresh3B=cv2.adaptiveThreshold(blur_s3B,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            s_temp3C=cv2.imread("E:\Mini_Project\Dynamic\sample3C.jpg",0)
            blur_s3C=cv2.medianBlur(s_temp3C,5)
            thresh3C=cv2.adaptiveThreshold(blur_s3C,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

            cv2.putText(frame,"PART 3",(468,410),cv2.FONT_HERSHEY_SIMPLEX , 1.5,(255,255,255))
            
            res_s3A=cv2.matchTemplate(thresh_img.copy(),thresh3A,cv2.TM_CCOEFF_NORMED)
            loc=np.where(res_s3A>=0.75)
            for pt in zip(*loc[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                #cv2.putText(img1_color,"Screw A missing",pt,cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))
                
            res_s3B=cv2.matchTemplate(thresh_img.copy(),thresh3B,cv2.TM_CCOEFF_NORMED)
            loc1=np.where(res_s3B>=0.75)
            for pt in zip(*loc1[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
                #cv2.putText(img1_color,"Screw B missing",(250,285),cv2.FONT_HERSHEY_SIMPLEX , 0.5,(0,0,255))

            res_s3C=cv2.matchTemplate(thresh_img.copy(),thresh3C,cv2.TM_CCOEFF_NORMED)
            loc2=np.where(res_s3C>=0.75)
            for pt in zip(*loc2[::-1]):
                x=pt[0]+w
                y=pt[1]+h
                cv2.rectangle(img1_color,pt,(x,y),(0,0,255),3)
            
        
        cv2.namedWindow("out",cv2.WINDOW_NORMAL);
        cv2.imshow("out",img1_color)

        if (cv2.waitKey(1) == 27):
            break





    






#display



cam.release()
cv2.destroyAllWindows()
