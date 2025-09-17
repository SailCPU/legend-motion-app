# ESP32开发指南

## 📋 硬件清单

### 必需组件
- **ESP32开发板** (约30元)
  - 型号: ESP32-WROOM-32
  - 特点: WiFi + 蓝牙，低功耗
  - 购买链接: [淘宝搜索](https://s.taobao.com/search?q=ESP32开发板)

- **MPU6050传感器** (约15元)
  - 功能: 加速度计 + 陀螺仪
  - 通信: I2C接口
  - 用途: 步数检测、姿态识别

- **MAX30102传感器** (约25元)
  - 功能: 心率监测
  - 通信: I2C接口
  - 特点: 非接触式心率检测

- **杜邦线** (约10元)
  - 公对公、公对母、母对母各20根
  - 用于连接传感器和开发板

### 可选组件
- **OLED显示屏** (约15元)
  - 型号: 0.96寸 I2C OLED
  - 用途: 显示实时数据

- **面包板** (约5元)
  - 用于搭建原型电路

- **电阻包** (约10元)
  - 常用阻值: 10KΩ, 4.7KΩ, 1KΩ

## 🔌 电路连接

### ESP32引脚分配
```
ESP32引脚    →    传感器引脚
GPIO21      →    SDA (I2C数据线)
GPIO22      →    SCL (I2C时钟线)
3.3V        →    VCC (电源正极)
GND         →    GND (电源负极)
```

### 连接示意图
```
ESP32开发板
├── 3.3V ──→ MPU6050 VCC
├── GND  ──→ MPU6050 GND
├── GPIO21 ──→ MPU6050 SDA
├── GPIO22 ──→ MPU6050 SCL
├── 3.3V ──→ MAX30102 VCC
├── GND  ──→ MAX30102 GND
├── GPIO21 ──→ MAX30102 SDA
└── GPIO22 ──→ MAX30102 SCL
```

## 💻 开发环境搭建

### 1. 安装Arduino IDE
1. 下载Arduino IDE: https://www.arduino.cc/en/software
2. 安装ESP32开发板支持包:
   - 文件 → 首选项 → 附加开发板管理器网址
   - 添加: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
   - 工具 → 开发板 → 开发板管理器 → 搜索"ESP32" → 安装

### 2. 安装必要的库
```cpp
// 在Arduino IDE中安装以下库:
// 工具 → 管理库 → 搜索并安装:
- MPU6050库
- MAX30102库
- WiFi库
- WebServer库
```

## 📝 基础代码示例

### ESP32传感器读取代码
```cpp
#include <Wire.h>
#include <MPU6050.h>
#include <MAX30102.h>
#include <WiFi.h>
#include <WebServer.h>

// 传感器对象
MPU6050 mpu;
MAX30102 max30102;

// WiFi配置
const char* ssid = "你的WiFi名称";
const char* password = "你的WiFi密码";

// Web服务器
WebServer server(80);

// 传感器数据
struct SensorData {
  float accelX, accelY, accelZ;
  float gyroX, gyroY, gyroZ;
  int heartRate;
  int steps;
} sensorData;

void setup() {
  Serial.begin(115200);
  
  // 初始化I2C
  Wire.begin();
  
  // 初始化传感器
  mpu.initialize();
  max30102.begin();
  
  // 连接WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("连接WiFi中...");
  }
  Serial.println("WiFi连接成功!");
  Serial.print("IP地址: ");
  Serial.println(WiFi.localIP());
  
  // 设置Web服务器路由
  server.on("/", handleRoot);
  server.on("/api/data", handleData);
  server.begin();
}

void loop() {
  // 读取传感器数据
  readSensors();
  
  // 处理Web请求
  server.handleClient();
  
  delay(100); // 100ms更新一次
}

void readSensors() {
  // 读取MPU6050数据
  mpu.getMotion6(&sensorData.accelX, &sensorData.accelY, &sensorData.accelZ,
                 &sensorData.gyroX, &sensorData.gyroY, &sensorData.gyroZ);
  
  // 读取心率数据
  sensorData.heartRate = max30102.getHeartRate();
  
  // 简单的步数检测算法
  float acceleration = sqrt(sensorData.accelX*sensorData.accelX + 
                           sensorData.accelY*sensorData.accelY + 
                           sensorData.accelZ*sensorData.accelZ);
  
  if (acceleration > 12.0) { // 阈值可调整
    sensorData.steps++;
  }
}

void handleRoot() {
  String html = "<!DOCTYPE html><html><head><title>ESP32传感器数据</title></head><body>";
  html += "<h1>ESP32传感器数据</h1>";
  html += "<div id='data'></div>";
  html += "<script>setInterval(function(){fetch('/api/data').then(r=>r.json()).then(d=>document.getElementById('data').innerHTML=JSON.stringify(d))},1000);</script>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void handleData() {
  String json = "{";
  json += "\"accelX\":" + String(sensorData.accelX) + ",";
  json += "\"accelY\":" + String(sensorData.accelY) + ",";
  json += "\"accelZ\":" + String(sensorData.accelZ) + ",";
  json += "\"heartRate\":" + String(sensorData.heartRate) + ",";
  json += "\"steps\":" + String(sensorData.steps);
  json += "}";
  server.send(200, "application/json", json);
}
```

## 🔧 常见问题解决

### 1. 传感器无法读取数据
- 检查I2C连接是否正确
- 确认传感器地址是否正确
- 检查电源电压是否为3.3V

### 2. WiFi连接失败
- 确认WiFi名称和密码正确
- 检查信号强度
- 尝试重启ESP32

### 3. 心率检测不准确
- 确保传感器与皮肤紧密接触
- 调整检测阈值
- 增加滤波算法

## 📚 进阶学习

### 1. 传感器融合算法
- 卡尔曼滤波
- 互补滤波
- 四元数姿态解算

### 2. 低功耗优化
- 深度睡眠模式
- 动态频率调节
- 传感器休眠控制

### 3. 无线通信
- 蓝牙BLE
- WiFi AP模式
- LoRa长距离通信

## 🛒 购买建议

### 推荐商家
- **淘宝**: 搜索"ESP32开发板"选择销量高的商家
- **京东**: 选择官方旗舰店
- **拼多多**: 价格更便宜，适合批量购买

### 注意事项
- 选择支持Arduino IDE的开发板
- 确认包含USB数据线
- 检查是否有详细的中文说明文档
