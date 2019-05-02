Feature: 显示图片拍摄地点

  Scenario: 读取图片

    Given 图片地址
    When  地址合法
    Then  将文件读到内存
    When  文件为JPG格式
    And   Exif中包含Location信息
    Then  读取成功

  Scenario: 在地图上显示位置

    Given Location信息
    Then  解析Location信息，转换成标准形式
    When  Location格式合法
    Then  调用高德url api


