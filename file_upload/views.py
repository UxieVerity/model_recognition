from django.shortcuts import render,HttpResponse
from .models import *
import base64
import cv2
import numpy
import json
# Create your views here.
'''
def uploadImg(request):
    if request.method == 'POST':
        for img in request.FILES.getlist('img'):
            new_img = IMG(
                img = img,
                name = img.name
            )
            new_img.save()
    return render(request, 'upload.html')

def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'show.html',content)
'''

to_str = ""
length = ""
number = 0

def draw(request):
    if request.method == 'POST':
        step = request.POST.get('step')
        if step == "1":
            global to_str, number,length
            strs = request.POST.get('img').split(',')[1]
            imgdata = base64.b64decode(strs)
            length = str(len(IMG.objects.filter()))#获取新图片的编号
            Str = 'E:\\web_design\\django_program\\file_upload\\media\\img\\'+length+'.png'#获取新图片的路径
            file = open(Str, 'wb')
            file.write(imgdata)#绘制新图片
            file.close()
            img = cv2.imread(Str)#读取图片
            cut = img[top(img):down(img), left(img):right(img)]#切割图片
            res = cv2.resize(cut, (28, 28), interpolation=cv2.INTER_AREA)#图片重置大小为28*28
            #cv2.namedWindow("Image")
            #cv2.imshow("Image", res)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #print(massage(res))
            to_str = to_string(massage(res))#获取像素值
            if request.POST.get('type') == "model":
                #模板匹配
                number = get_number(to_str)
            elif request.POST.get('type') == "bayes":
                #贝叶斯匹配
                number = bayes(to_str)
            else:
                #感知器
                number = out(result1(to_str))
            return HttpResponse(json.dumps({'number': number}))
        else:
            if request.POST.get('is_right') == "1":
                insert(to_str,length,number)
            else:
                number = request.POST.get('number')
                insert(to_str, length, number)
        print("success")

    return render(request,'draw.html')

def top(self):
    for i in range(240):
        for j in range(240):
            if str(self[i][j]) != str(numpy.array([255, 255, 255])):
                return i

def left(self):
    for i in range(240):
        for j in range(240):
            if str(self[j][i]) != str(numpy.array([255, 255, 255])):
                return i

def down(self):
    for i in range(240):
        for j in range(240):
            if str(self[239-i][j]) != str(numpy.array([255, 255, 255])):
                return 240-i

def right(self):
    for i in range(240):
        for j in range(240):
            if str(self[j][239-i]) != str(numpy.array([255, 255, 255])):
                return 240-i
#二值化处理
def massage(self):
    data =[[0 for col in range(28)] for row in range(28)]
    for i in range(28):
        for j in range(28):
            if str(self[i][j]) != str(numpy.array([255, 255, 255])):
                data[i][j] = 1
    return data

#数字转字符串
def to_string(self):
    string = [str() for col in range(28)]
    for i in range(28):
        for j in range(28):
            string[i]=string[i]+str(self[i][j])
    return string

#插入数据到数据库
def insert(self,length,number):
    new_img = IMG(
        img = length+'.png',
        number = number,
        #eigenvalue = eigenvalue(self),
        col0=self[0],
        col1=self[1],
        col2=self[2],
        col3=self[3],
        col4=self[4],
        col5=self[5],
        col6=self[6],
        col7=self[7],
        col8=self[8],
        col9=self[9],
        col10=self[10],
        col11=self[11],
        col12=self[12],
        col13=self[13],
        col14=self[14],
        col15=self[15],
        col16=self[16],
        col17=self[17],
        col18=self[18],
        col19=self[19],
        col20=self[20],
        col21=self[21],
        col22=self[22],
        col23=self[23],
        col24=self[24],
        col25=self[25],
        col26=self[26],
        col27=self[27],
    )
    new_img.save()

#模板匹配
def get_number(to_str):
    min = 28*28#不重复的点的个数
    number = 0#保存min对应的number值
    photos = IMG.objects.filter().values()#获取所有的数据
    for photo in photos:
        sum = 0
        for i in range(28):
            for j in range(28):
                if to_str[i][j] != photo["col"+str(i)][j]:
                    sum = sum + 1#遍历模板,遍历模板数据的像素,不等时sum+1
        if sum < min:
            min = sum
            number = photo["number"]
    return number

#获取指定照片特征值的个数(1的个数)
def eigenvalue(self):
    eigenvalue = 0
    for sel in self:
        for i in range(28):
            if sel[i] == "1":
                eigenvalue = eigenvalue + 1
    return eigenvalue

#贝叶斯
def bayes(self):
    number = 0#保存最大概率所对应的值
    max = 0#保存最大概率
    for num in range(10):
        rate = 0#初始化待测数为指定数的概率
        length = len(IMG.objects.filter(number=str(num)))#获取数据库中值为number的模型个数
        for img in IMG.objects.filter(number=str(num)):#遍历模型
            for i in range(28):#遍历指定模型的像素获取相等特征值的个数
                for j in range(28):
                    eigen_length = 0
                    if i==0:
                      imgCol = img.col0
                    elif i==1:
                      imgCol = img.col1
                    elif i==2:
                      imgCol = img.col2
                    elif i==3:
                      imgCol = img.col3
                    elif i==4:
                      imgCol = img.col4
                    elif i==5:
                      imgCol = img.col5
                    elif i==6:
                      imgCol = img.col6
                    elif i==7:
                      imgCol = img.col7
                    elif i==8:
                      imgCol = img.col8
                    elif i==9:
                      imgCol = img.col9
                    elif i==10:
                      imgCol = img.col10
                    elif i==11:
                      imgCol = img.col11
                    elif i==12:
                      imgCol = img.col12
                    elif i==13:
                      imgCol = img.col13
                    elif i==14:
                      imgCol = img.col14
                    elif i==15:
                      imgCol = img.col15
                    elif i==16:
                      imgCol = img.col16
                    elif i==17:
                      imgCol = img.col17
                    elif i==18:
                      imgCol = img.col18
                    elif i==19:
                      imgCol = img.col19
                    elif i==20:
                      imgCol = img.col20
                    elif i==21:
                      imgCol = img.col21
                    elif i==22:
                      imgCol = img.col22
                    elif i==23:
                      imgCol = img.col23
                    elif i==24:
                      imgCol = img.col24
                    elif i==25:
                      imgCol = img.col25
                    elif i==26:
                      imgCol = img.col26
                    elif i==27:
                      imgCol = img.col27
                    if self[i][j] == imgCol[j]:
                        eigen_length = eigen_length + 1
                    rate = rate + (eigen_length/length)
        rate = rate/784#rate为待测数为指定数的平均值概率
        #print("num:"+str(num)+"概率:"+str(rate))
        if rate > max:
            max = rate
            number = num
    return number

#net
#激活函数
def f(x):
    if x > 0:
        return 1
    else :
        return 0

b1s = [0 for i in range(10)]#10个值的b值
w1s = [[[0 for a in range(28)] for b in range(28)] for k in range(10)]#10个数的28*28的值的数
target = [[1,0,0,0,0,0,0,0,0,0],#target为目标,经过wx+b以及激活函数处理过后的结果对象
          [0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,1,0,0,0],
          [0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0,0,1]]

numbers_length = len(IMG.objects.filter().values())#数据库数据的长度
imgs = [["" for c in range(28)] for d in range(numbers_length)]#用于保存数据库图片信息
imgs_number = [0 for g in range(numbers_length)]#用于保存数据库中数据对应的数字
imgs_target = [[] for h in range(numbers_length)]#保存数据库图片对应的目标数组

list_number = 0#数据编号
for img in IMG.objects.filter().values():#遍历数据库,

    for e in range(28):
        imgs[list_number][e] = img["col" + str(e)]#imgs初始化

    #imgs_number以及imgs_target初始化
    if img["number"] == "0":
        imgs_number[list_number] = 0
        imgs_target[list_number] = target[0]
    elif img["number"] == "1":
        imgs_number[list_number] = 1
        imgs_target[list_number] = target[1]
    elif img["number"] == "2":
        imgs_number[list_number] = 2
        imgs_target[list_number] = target[2]
    elif img["number"] == "3":
        imgs_number[list_number] = 3
        imgs_target[list_number] = target[3]
    elif img["number"] == "4":
        imgs_number[list_number] = 4
        imgs_target[list_number] = target[4]
    elif img["number"] == "5":
        imgs_number[list_number] = 5
        imgs_target[list_number] = target[5]
    elif img["number"] == "6":
        imgs_number[list_number] = 6
        imgs_target[list_number] = target[6]
    elif img["number"] == "7":
        imgs_number[list_number] = 7
        imgs_target[list_number] = target[7]
    elif img["number"] == "8":
        imgs_number[list_number] = 8
        imgs_target[list_number] = target[8]
    else :
        imgs_number[list_number] = 9
        imgs_target[list_number] = target[9]

    list_number = list_number + 1

#第一层
def result1(self):
    sums = [0 for i in range(10)]#保存sum值经过激活函数处理之后的值
    for a in range(10):
        sum = 0
        for i in range(28):
            for j in range(28):
                sum = sum + int(self[i][j]) * w1s[a][i][j]#sum为对应的数据*对应的数据所对应的w值的和加上对应值的b值
        sum = sum + b1s[a]
        sums[a] = f(sum)
    return sums

#训练函数
def train(self,TAR):
    global w1s,b1s
    delta1 = [0 for i in range(10)]#与目标状态的差值
    rate1 = 0.01#训练速率
    result = result1(self)#获得结果对象
    #遍历隐藏层结点
    for i in range(10):
        delta1[i] = TAR[i] - result[i]
    for i in range(10):
        for j in range(28):
            for k in range(28):
                w1s[i][j][k] = w1s[i][j][k] + rate1 * delta1[i] * int(self[j][k])#更新w
        b1s[i] = b1s[i] + rate1 * delta1[i]#更新b

#结果输出
def out(self):
    number = 0#储存识别的数值结果
    level2 = ""#将数组转为字符串
    for i in self:
        level2 = level2 + str(i)
    #print(level2)
    if self[0] == 1 and level2[1:] == "000000000":
        number = 0
    elif self[1] == 1 and level2[0:1] == "0" and level2[2:] == "00000000":
        number = 1
    elif self[2] == 1 and level2[0:2] == "00" and level2[3:] == "0000000":
        number = 2
    elif self[3] == 1 and level2[0:3] == "000" and level2[4:] == "000000":
        number = 3
    elif self[4] == 1 and level2[0:4] == "0000" and level2[5:] == "00000":
        number = 4
    elif self[5] == 1 and level2[0:5] == "00000" and level2[6:] == "0000":
        number = 5
    elif self[6] == 1 and level2[0:6] == "000000" and level2[7:] == "000":
        number = 6
    elif self[7] == 1 and level2[0:7] == "0000000" and level2[8:] == "00":
        number = 7
    elif self[8] == 1 and level2[0:8] == "00000000" and level2[9:] == "0":
        number = 8
    elif self[9] == 1 and level2[0:9] == "000000000":
        number = 9
    else:
        number = "识别失败"
    return number

#正确率
def right_rate():
    right_number = 0
    for m in range(numbers_length):
        if out(result1(imgs[m])) == imgs_number[m]:
            right_number = right_number + 1
    return right_number/numbers_length

turn = 0
while right_rate() < 0.98:
    turn = turn + 1
    for n in range(numbers_length):
        train(imgs[n],imgs_target[n])
    print("训练次数为：" + str(turn) + "\n正确率为：" + str(right_rate()))
    #print("识别结果为："+str(out(result1(imgs[12]))))

#print("总数为："+str(numbers_length)+"\n正确数为："+str(right_number)+"\n正确率为："+str(right_number/numbers_length))