import tkinter as tk
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from tkinter import messagebox

window = tk.Tk()

window.title("Attendance System Using AI")


window.configure(background='white')


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

x_cord = 75;
y_cord = 10;
checker=0;

message = tk.Label(window, text="RAJIV GANDHI COLLEGE OF ENGINEERING AND TECHNOLOGY" ,bg="white"  ,fg="black"  ,width=80  ,height=2,font=('Times New Roman', 15, 'bold')) 
message.place(x=220, y=-10)

message = tk.Label(window, text="ATTENDANCE MANAGEMENT PORTAL" ,bg="white"  ,fg="black"  ,width=40  ,height=1,font=('Times New Roman', 30, 'bold underline')) 
message.place(x=200, y=30)

lbl7 = tk.Label(window, text="FOR NEW MODEL TRAINING FOLLOW THE STEPS :",width=50  ,height=1  ,fg="black"  ,bg="white" ,font=('Times New Roman', 15, ' bold ') ) 
lbl7.place(x=165-x_cord, y=125-y_cord)

lbl8 = tk.Label(window, text="STEP 1.",width=10  ,fg="red"  ,bg="white"  ,height=1 ,font=('Times New Roman', 15, ' bold '))
lbl8.place(x=140-x_cord, y=168-y_cord)

lbl8 = tk.Label(window, text="STEP 2.",width=10  ,fg="red"  ,bg="white"  ,height=1 ,font=('Times New Roman', 15, ' bold '))
lbl8.place(x=140-x_cord, y=225-y_cord)

lbl9 = tk.Label(window, text="STEP 3.",width=10  ,fg="red"  ,bg="white"  ,height=1 ,font=('Times New Roman', 15, ' bold '))
lbl9.place(x=140-x_cord, y=279-y_cord)

lbl10 = tk.Label(window, text="STEP 4.",width=10  ,fg="red"  ,bg="white"  ,height=1 ,font=('Times New Roman', 15, ' bold '))
lbl10.place(x=140-x_cord, y=330-y_cord)

lbl7 = tk.Label(window, text="**IF ALREADY THE MODEL IS TRAINED PRESS THE BUTTON BELOW TO MARK ATTENDANCE :",width=80  ,height=1  ,fg="black"  ,bg="white" ,font=('Times New Roman', 13, ' bold ') ) 
lbl7.place(x=165-x_cord, y=400-y_cord)

# lbl2 = tk.Label(window, text="Press Here To Capture Image :",width=30  ,fg="black"  ,bg="white"    ,height=1 ,font=('Times New Roman', 15, ' bold ')) 
# lbl2.place(x=200-x_cord, y=275-y_cord)

# lbl2 = tk.Label(window, text="Press Here To Link Image With Id :",width=35  ,fg="black"  ,bg="white"    ,height=1 ,font=('Times New Roman', 15, ' bold ')) 
# lbl2.place(x=200-x_cord, y=325-y_cord)

lbl = tk.Label(window, text="Enter Register Number :",width=25  ,height=1  ,fg="black"  ,bg="white" ,font=('Times New Roman', 15, ' bold ') ) 
lbl.place(x=240-x_cord, y=168-y_cord)


txt = tk.Entry(window,width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
txt.place(x=500-x_cord, y=170-y_cord)

lbl2 = tk.Label(window, text="Enter Student Name :",width=25  ,fg="black"  ,bg="white"    ,height=1 ,font=('Times New Roman', 15, ' bold ')) 
lbl2.place(x=250-x_cord, y=225-y_cord)

txt2 = tk.Entry(window,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
txt2.place(x=500-x_cord, y=225-y_cord)

lbl3 = tk.Label(window, text="NOTIFICATION AREA :",width=20  ,fg="black"  ,bg="white"  ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
lbl3.place(x=900-x_cord, y=120-y_cord)

message = tk.Label(window, text="" ,bg="white"  ,fg="red"  ,width=40  ,height=5, activebackground = "white" ,font=('Times New Roman', 15, ' bold ')) 
message.place(x=865-x_cord, y=180-y_cord)

lbl3 = tk.Label(window, text="ATTENDANCE LOG :",width=20  ,fg="black"  ,bg="white"  ,height=2 ,font=('Times New Roman', 20, ' bold ')) 
lbl3.place(x=80, y=550-y_cord)


message2 = tk.Label(window, text="" ,fg="red"   ,bg="skyblue",activeforeground = "green",width=60  ,height=4  ,font=('times', 15, ' bold ')) 
message2.place(x=400, y=550-y_cord)

# lbl4 = tk.Label(window, text="STEP 1",width=20  ,fg="green"  ,bg="white"  ,height=2 ,font=('Times New Roman', 20, ' bold '))
# lbl4.place(x=200-x_cord, y=300-y_cord)

# lbl5 = tk.Label(window, text="STEP 2",width=20  ,fg="green"  ,bg="white"  ,height=2 ,font=('Times New Roman', 20, ' bold ')) 
# lbl5.place(x=605-x_cord, y=300-y_cord)

# lbl6 = tk.Label(window, text="STEP 3",width=20  ,fg="green"  ,bg="white"  ,height=2 ,font=('Times New Roman', 20, ' bold ')) 
# lbl6.place(x=1060-x_cord, y=300-y_cord)
 
def clear1():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if not Id:
        res="Please enter Register Number Before Proceed.!!"
        message.configure(text = res)
        MsgBox = tk.messagebox.askquestion ("Warning","Please enter roll number properly , press yes if you understood",icon = 'warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need','Please go through the readme file properly')
    elif not name:
        res="Please enter Name Before Proceed.!!"
        message.configure(text = res)
        MsgBox = tk.messagebox.askquestion ("Warning","Please enter name properly , press yes if you understood",icon = 'warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need','Please go through the readme file properly')
        
    elif(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name +"!!"
            row = [Id , name]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name.!!"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id.!!"
            message.configure(text= res)
            
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained.!!"
    clear1();
    clear2();
    message.configure(text= res)
    tk.messagebox.showinfo('Completed','Your model has been trained successfully!!')
    

def getImagesAndLabels(path):

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    
    faces=[]

    Ids=[]

    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    message2.configure(text= res)
    res = "Attendance Taken.!!"
    message.configure(text= res)
    tk.messagebox.showinfo('Completed','Congratulations ! Your attendance has been marked successfully for the day!!')
    
def quit_window():
   MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
   if MsgBox == 'yes':
       tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
       window.destroy()
    
takeImg = tk.Button(window, text="PRESS HERE TO CAPTURE IMAGE ", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=45  ,height=1, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
takeImg.place(x=250-x_cord, y=275-y_cord)
trainImg = tk.Button(window, text="PRESS HERE TO TRAIN MODEL WITH THIS ID", command=TrainImages  ,fg="white"  ,bg="blue"  ,width=45  ,height=1, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
trainImg.place(x=250-x_cord, y=325-y_cord)
trackImg = tk.Button(window, text="MARK ATTENDANCE ", command=TrackImages  ,fg="white"  ,bg="red"  ,width=20  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
trackImg.place(x=400-x_cord, y=450-y_cord)
quitWindow = tk.Button(window, text="QUIT", command=quit_window  ,fg="white"  ,bg="red"  ,width=6  ,height=1, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
quitWindow.place(x=1250, y=670-y_cord)
 
window.mainloop()