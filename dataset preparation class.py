#dataset preparartion class to make it easier to load the data
import cv2
import numpy as np

class DataSet:
    
    def __init__(me,location,categories,resize=True,
                 lheight=500,lwidth=500,grayscale=True,shuffled=False,
                 apply=None,count=1000,multiclass=False,enhance=False):
        me.categories=categories
        me.datadir=location
        me.lheight=lheight
        me.lwidth=lwidth
        me.grayscale=grayscale
        me.shuffled=shuffled
        me.multiclass=multiclass
        me.apply=apply
        me.count=count
        me.enhance=enhance
        me.dataset=me.create_traindata()
        if resize==True:
            me.dataset=me.resizeIt(me.dataset)

        
        
    
    def resizeIt(me,traindata_array):
        resized_traindata=[]
        resized_traindata_temp=[]
        for img in traindata_array[0]:
            
            new_image_array=cv2.resize(img,(me.lheight,me.lwidth))
            resized_traindata_temp.append(np.array(new_image_array))
        array=[np.array(resized_traindata_temp),np.array(traindata_array[1])]
        return(array)



    def create_traindata(me):
        traindata=[]
        for cats in me.categories:
            n=0
            path=os.path.join(me.datadir,cats)
            class_num=me.categories.index(cats)
            for img in os.listdir(path):
                if(me.grayscale==True and me.enhance==True):
                    y=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)

                    y=cv2.resize(y,(512,512))


                    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(5,5))
                    img_array = clahe.apply(y)

                    img_array = cv2.GaussianBlur(y,(3,3),1)


                    n=n+1
                    print(str(n)+" images loaded successfully",end='')
                    if n>=me.count:
                      break
                
                elif(me.enhance==True):
                    img_array=cv2.imread(os.path.join(path,img))

                    img_array=cv2.resize(img_array,(512,512))

                    img_yuv_1 = cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)

                    
                    img_yuv = cv2.cvtColor(img_yuv_1,cv2.COLOR_RGB2YUV)

                    y,u,v = cv2.split(img_yuv)

                    

                    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(5,5))
                    y = clahe.apply(y)

                    y = cv2.GaussianBlur(y,(3,3),1)

                    img_array_1 = cv2.merge((y,u,v))
                    img_array = cv2.cvtColor(img_array_1,cv2.COLOR_YUV2RGB)
                    
                    n=n+1
                    print(str(n)+" images loaded successfully",end='')
                    if n>=me.count:
                      break
                else:
                    img_array=cv2.imread(os.path.join(path,img))

                    n=n+1
                    print(str(n)+" images loaded successfully",end='')
                    if n>=me.count:
                      break
                if(me.multiclass==False):
                    traindata.append([img_array,class_num])
                else:
                    traindata.append([img_array,me.classes(class_num=class_num,classes=len(me.categories))])
            print(len(traindata))
            print()
            
        if(me.shuffled==True):
          random.shuffle(traindata)
          print("shuffled")
        traindata_img=[]
        traindata_lab=[]
        for sets in traindata:
            traindata_img.append(sets[0])
            traindata_lab.append(sets[1])
        traindata=[traindata_img,traindata_lab]
        return(traindata)

    def classes(me,class_num,classes):
        array = [0 for i in range(classes)]
        array[class_num]=1
        return(array)
