# Picmap

基于Python的相片拍摄位置定位及路线推荐设计

**按照TODO中的任务执行，及时反馈**



## 文件结构

总体部分：

> 每次我给你代码的时候，只把libPicmap文件夹替换就好，其他两个文件夹当做用法参考

- **libPicmap**

  > 算法和数据模块，这部分你可以直接替换我的，你不用修改，没有写到的功能向我提，我来完善

- **sample**

  > 这里是我给出的样例，其中cli是我会完善的内容，写命令行操作的逻辑流程，可以参照
  > gui部分主要保留了原来的拖拽显示程序和js回调程序，之后有什么不会写的告诉我，我会把例子写在这

- **test**

  > 这里面都是对libPicmap的单独功能调用测试，供参照用法
  > 其中api文件夹放的是http接口测试
  > feature文件夹应该不会在维护了




GUI部分：

> 这个就是你的source目录了，因为你不需要写cli 
> 你的目录应该是
> root 
>   |- libPicmap:	这个就每次替换我的
>   |- source:		这个你自己写，可以参照这个gui部分
> source内部分文件夹，你就随意吧，也可以先和我这样分出resources和ui等等

- **resources** 

  > 存放资源文件，网页的文件和自动生成ui的文件
  > 其中web文件夹存放了网页有关的html、js、css等

- **ui**

  > .ui文件自动生成的py文件




CLI部分：

> 这部分你不用写，我是为了方便测试整体功能，所以写cli的，你可以参照使用方式
> 这里面picmap是入口，不需要看
> 其他的每个文件都是一个小功能
> 需要找某个功能怎么写的话，只需要看文件中的parse方法



## 高德地图接口使用方法

### [JS API](https://lbs.amap.com/api/javascript-api/guide/abc/quickstart)

详见**jsApiTest.html**与**jsApiTest.py**，这两个文件看懂即可

1. 准备工作

   ```html
   <!-- 1.在body中间加入id为container的div，这个是用来存放地图的 -->
   <div id="container"></div>
   <!-- 2.加载高德地图JS API的脚本 -->
   <script src="https://webapi.amap.com/maps?v=1.4.14&key={你的key}"></script>
   <!-- 3.修改控件样式 -->
   <style type="text/css">
       #container {
           width: 800px;
           height: 600px;
       }
   </style>
   ```

2. 初始化地图：

   ```js
   // 初始化地图
   var map = new AMap.Map('container', {
       resizeEnable: true
   });
   ```

3. Python运行这个页面

   ```python
   # 前提是之前做ui的时候添加了webEngineView
   self.webEngineView.setHtml('html的地址').read())
   ```

4. Py调用JS

   ```python
   self.webEngineView.page().runJavaScript('需要调用的js代码')
   ```

5. JS回调Py

   1. 先写一个handler，用来获取数据，要继承QObject

      ```python
      class Handler(QObject):
          @pyqtSlot()
          def callback(self, message):
              {doSomething}
      ```

   2. 绑定handler，设置通信的通道

      ```python
      # 新建一个通道
      self.channel = QWebChannel()
      # 这里要注意一点，如果写在类中必须要self.不然注册完了这个handler就丢失了，之后找不到
      # 这个就是刚刚写的Handler
      self.handler = Handler()
      # 通道注册这个handler，之后js那边就可以拿到这个对象，并且调用这个类的方法
      # 第一个参数是给js调用时用的对象名
      self.channel.registerObject('handler', self.handler)
      # 给webEngineView设置这个通道
      self.webEngineView.page().setWebChannel(self.channel)
      ```

   3. 加载script

      ```html
      <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
      ```

   4. JS中获取Handler对象

      ```js
      new QWebChannel(qt.webChannelTransport, function (channel) {
          // 这里channel.objects.handler就是之前注册方法中的'handler'
      	window.handler = channel.objects.handler; 
      });
      ```

   5. JS调用Handler方法

      ```js
      // 这里的callback是函数名，之前定义Handler类的时候取好的
      window.handler.callback('something');
      ```



### [Web Serve](https://lbs.amap.com/api/webservice/guide/api/georegeo)

详见**webServeApiTest.http**，这里所有方法都是http请求，返回JS，比较简单，就不多写了。



## 功能实现方法

按照之前列举的功能

| 功能                                     | 方法过程                                                     |
| ---------------------------------------- | ------------------------------------------------------------ |
| 显示拍照地点<br />基础导航<br />显示周边 | 1. 读图片<br />2. 用piexif读Exif<br />3. 用HTTP API显示位置<br />（为什么不用JS API，因为HTTP API直接由导航和周边功能，能直接用就直接用） |
| 照片归档/整理/可视化                     | 归档/整理都是普通客户端操作了，想办法吧<br />可视化API我还没看，但是也是JS API，大同小异，想办法实现 |
| 给图片添加Exif地址                       | 1. 用JS API显示地图<br />2. 用JS API的交互功能，点击地图获取地址信息<br />3. 用Web Serve API通过输入提示和地点转坐标通过用户输入地点获取地址<br />4. 用piexif将地址信息写入图片 |
| 多点路线推荐                             | 1. 用Web Serve API获取每两个点之间的导航距离和时间<br />2. 写算法计算出最优解<br />3. 使用JS API将结果画在地图上 |

