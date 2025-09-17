# Legend Motion App - 运动监测原型

这是一个基于ESP32和HTML的运动监测原型项目，适合学生快速上手和验证想法。

## 🚀 快速开始

### 1. 环境准备

#### Python环境
```bash
# 安装Python 3.8+
# 安装依赖
pip install -r requirements.txt
```

#### 硬件准备
- ESP32开发板
- MPU6050加速度计+陀螺仪
- MAX30102心率传感器
- 杜邦线若干

### 2. 运行项目

#### 启动后端服务
```bash
cd python
python app.py
```

#### 访问前端页面
打开浏览器访问: http://localhost:5000

### 3. 功能说明

- ✅ **实时数据显示**: 心率、步数、卡路里、活动强度
- ✅ **图表展示**: 心率趋势和步数统计
- ✅ **数据存储**: SQLite本地数据库
- ✅ **数据导出**: CSV格式导出
- ✅ **响应式设计**: 支持移动端访问

## 📁 项目结构

```
prototype/
├── index.html              # 主页面
├── css/
│   └── style.css          # 样式文件
├── js/
│   ├── main.js            # 主要逻辑
│   ├── chart.js           # 图表功能
│   └── websocket.js       # 实时数据
├── python/
│   ├── app.py             # Flask后端
│   ├── sensor_reader.py   # 传感器读取
│   └── database.py        # 数据库操作
├── requirements.txt        # Python依赖
└── README.md             # 项目说明
```

## 🔧 开发指南

### 添加新传感器
1. 在`sensor_data`字典中添加新字段
2. 更新数据库表结构
3. 修改前端显示组件
4. 更新图表配置

### 自定义UI
1. 修改`css/style.css`文件
2. 调整`index.html`中的HTML结构
3. 使用响应式设计适配不同设备

### 扩展功能
1. 添加用户认证
2. 实现数据云端同步
3. 增加更多图表类型
4. 添加数据分析和报告

## 📱 移动端适配

项目已支持移动端访问，包括：
- 响应式布局
- 触摸友好的按钮
- 适配不同屏幕尺寸
- 优化的图表显示

## 🚀 下一步计划

1. **硬件集成**: 连接真实的ESP32传感器
2. **功能完善**: 添加更多监测功能
3. **UI优化**: 改进用户界面设计
4. **性能优化**: 提升数据处理效率
5. **正式迁移**: 迁移到Flutter框架

## 💡 学习资源

- [Flask官方文档](https://flask.palletsprojects.com/)
- [Chart.js图表库](https://www.chartjs.org/)
- [ESP32开发指南](https://docs.espressif.com/projects/esp-idf/)
- [WebSocket实时通信](https://socket.io/)

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

MIT License
