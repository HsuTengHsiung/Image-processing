#  作業3
---
    方法說明:
    1.對影像做LBP直方圖及正規化
    2.採取路面樣本並做LBP直方圖
    3.將原始影像切割為若干個區塊並逐個區塊比較兩者直方圖相似度
    控制參數
      1.LBP是否抗旋轉
      2.切割視窗大小
      3.閥值得選取(相似度)
    4.延伸
      1.兩次閥值:先以大框框出範圍(閥值較低)，再以小框比對細節(閥值較高)
      2.lbp直方圖捨去1和255特徵後比對==>1 255皆表示平滑面，出現機率過高正規化後容易造成匹配過於容易成功
    5.後續(還沒完成)
      1.多樣本匹配

![Road5](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road5_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D%E4%B8%80%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Road_5.jpg)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road5_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D%E4%B8%80%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_Final_forRoad5.jpg)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road5_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D%E4%B8%80%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_Final_forRoad5%20(4).jpg)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road5_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D%E4%B8%80%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_Final_forRoad5%20(2).jpg)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road5_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D%E4%B8%80%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_Final_forRoad5%20(3).jpg)

------------------------------------------
##  兩次批配

    不同視角的馬路
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_12.jpg)

    馬路樣本
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_12_Sample.jpg)

    比對結果(白色為最後結果，灰色為第一次匹配成功第二次失敗)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_Block_test1_2.jpg)

    重疊結果
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_Block_test1.jpg)

    調整閥值
    比對結果(白色為最後結果，灰色為第一次匹配成功第二次失敗)
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_Block_test2_2.jpg)

    重疊結果
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road12_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D/Road_Block_test2_1.jpg)

------------------------------------------

![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road7_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E4%BA%8C%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_forRoad5_2.jpg)

![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road7_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E4%BA%8C%E6%AC%A1_%E9%96%A5%E5%80%BC%E6%B8%AC%E8%A9%A6/Block_test_Final2_forRoad5_raw_image.jpg)




------------------------------------------
##  兩次批配 + 直方圖修正(0&255)

![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road10_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8E%BB0%26255/Road_10%E5%8C%B9%E9%85%8D%E6%B8%AC%E8%A9%A6.jpg)

--------------------------------------------
        原圖
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road16_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8E%BB0%26255/Road_16_raw.jpg)

        匹配結果
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road16_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8E%BB0%26255/Road_16_raw_LBP.jpg)

        做大範圍Close
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road16_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8E%BB0%26255/Road_16_raw_LBP_Close.jpg)

        重疊
![image](https://github.com/HsuTengHsiung/Image-processing/blob/master/000.%E4%BD%9C%E6%A5%AD%E7%B4%80%E9%8C%84/HW3/Road16_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8C%B9%E9%85%8D_%E7%9B%B4%E6%96%B9%E5%9C%96%E5%8E%BB0%26255/Road_16_raw_LBP_Close_Final.jpg)
