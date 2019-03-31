# model_recognition
前端利用canvas进行绘图
后台利用django框架实现，模板匹配、贝叶斯分类器、感知器手写数字识别。

## 环境安装:
该项目是用python3进行编写,所以得安装python3.0以上版本才能运行此项目  
该项目使用以下版本的model,在运行项目之前须安装以下版本的model  
django 2.1.7  
opencv-python 3.4.1   
pillow 4.2.1  
numpy 1.16.2  
这里使用pip进行model的安装  
打开cmd,输入如pip install django==2.1.7回车即可,如提示pip需更新则按照提示的更新操作进行更新

## 文件更改
需要更改file_upload里面的views.py的第39行,改为指向到img目录的绝对路径

## 运行
在项目根目录下运行python manage.py runserver
然后在浏览器当中输入127.0.0.1:8000即可访问进行识别
