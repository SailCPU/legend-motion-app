# Flutter学习路径

## 🎯 学习目标

为Legend的运动监测APP项目提供Flutter学习指导，从零基础到能够开发完整的跨平台应用。

## 📚 学习阶段

### 第一阶段：基础入门 (1-2周)

#### 1. 环境搭建
- [ ] 安装Flutter SDK
- [ ] 配置Android Studio
- [ ] 设置VS Code + Flutter插件
- [ ] 创建第一个Flutter项目

#### 2. Dart语言基础
- [ ] 变量和数据类型
- [ ] 函数和类
- [ ] 异步编程 (async/await)
- [ ] 集合操作 (List, Map, Set)

#### 3. Flutter基础组件
- [ ] Widget概念
- [ ] StatelessWidget vs StatefulWidget
- [ ] 常用组件: Text, Container, Row, Column
- [ ] 布局组件: Scaffold, AppBar, Body

### 第二阶段：UI开发 (2-3周)

#### 1. 布局系统
- [ ] Flex布局 (Row, Column)
- [ ] 容器组件 (Container, Padding, Margin)
- [ ] 网格布局 (GridView)
- [ ] 列表组件 (ListView)

#### 2. 交互组件
- [ ] 按钮组件 (ElevatedButton, TextButton)
- [ ] 输入组件 (TextField, Form)
- [ ] 选择组件 (Checkbox, Radio, Switch)
- [ ] 导航组件 (Navigator, Routes)

#### 3. 高级UI组件
- [ ] 卡片组件 (Card)
- [ ] 对话框 (AlertDialog, BottomSheet)
- [ ] 进度指示器 (CircularProgressIndicator)
- [ ] 图表组件 (fl_chart)

### 第三阶段：状态管理 (1-2周)

#### 1. 基础状态管理
- [ ] setState方法
- [ ] StatefulWidget状态管理
- [ ] 父子组件通信

#### 2. Provider状态管理
- [ ] Provider包安装和配置
- [ ] ChangeNotifier
- [ ] Consumer和Selector
- [ ] 多Provider管理

#### 3. 实际应用
- [ ] 用户数据管理
- [ ] 传感器数据状态
- [ ] 应用设置管理

### 第四阶段：硬件集成 (2-3周)

#### 1. 蓝牙通信
- [ ] flutter_blue插件
- [ ] 蓝牙设备扫描
- [ ] 设备连接和断开
- [ ] 数据读写

#### 2. 传感器数据处理
- [ ] 实时数据接收
- [ ] 数据滤波和校准
- [ ] 数据存储和缓存
- [ ] 数据可视化

#### 3. 硬件控制
- [ ] 设备配对管理
- [ ] 连接状态监控
- [ ] 错误处理和重连
- [ ] 低功耗优化

### 第五阶段：高级功能 (2-3周)

#### 1. 数据持久化
- [ ] SharedPreferences
- [ ] SQLite数据库
- [ ] 文件存储
- [ ] 数据导入导出

#### 2. 网络通信
- [ ] HTTP请求 (dio包)
- [ ] WebSocket实时通信
- [ ] 数据同步
- [ ] 离线支持

#### 3. 用户体验优化
- [ ] 加载状态管理
- [ ] 错误处理
- [ ] 用户反馈
- [ ] 性能优化

## 📖 推荐学习资源

### 官方文档
- [Flutter官方文档](https://flutter.dev/docs)
- [Dart语言指南](https://dart.dev/guides/language)
- [Flutter API参考](https://api.flutter.dev/)

### 在线教程
- [Flutter中文网](https://flutterchina.club/)
- [B站Flutter教程](https://www.bilibili.com/video/BV1S4411E7xZ)
- [慕课网Flutter课程](https://www.imooc.com/course/list?c=flutter)

### 实践项目
- [Flutter实战](https://book.flutterchina.club/)
- [Flutter Samples](https://github.com/flutter/samples)
- [Awesome Flutter](https://github.com/Solido/awesome-flutter)

## 🛠️ 开发工具

### IDE选择
1. **VS Code** (推荐)
   - 轻量级，启动快
   - 丰富的插件生态
   - 优秀的调试功能

2. **Android Studio**
   - 官方推荐
   - 完整的Android开发支持
   - 强大的调试工具

### 必备插件
- Flutter
- Dart
- Flutter Intl
- Awesome Flutter Snippets
- Flutter Widget Snippets

## 📱 项目实践

### 阶段1项目：计数器APP
```dart
class CounterApp extends StatefulWidget {
  @override
  _CounterAppState createState() => _CounterAppState();
}

class _CounterAppState extends State<CounterApp> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('计数器')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('点击次数: $_counter'),
            ElevatedButton(
              onPressed: _incrementCounter,
              child: Text('点击我'),
            ),
          ],
        ),
      ),
    );
  }
}
```

### 阶段2项目：传感器数据展示
```dart
class SensorDataPage extends StatefulWidget {
  @override
  _SensorDataPageState createState() => _SensorDataPageState();
}

class _SensorDataPageState extends State<SensorDataPage> {
  List<SensorReading> _readings = [];
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('传感器数据')),
      body: Column(
        children: [
          // 实时数据显示
          Container(
            padding: EdgeInsets.all(16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildDataCard('心率', '${_readings.last?.heartRate ?? 0}', 'BPM'),
                _buildDataCard('步数', '${_readings.last?.steps ?? 0}', '步'),
              ],
            ),
          ),
          // 图表显示
          Expanded(
            child: LineChart(
              LineChartData(
                lineBarsData: [
                  LineChartBarData(
                    spots: _readings.map((r) => 
                      FlSpot(r.timestamp.millisecondsSinceEpoch.toDouble(), 
                             r.heartRate.toDouble())).toList(),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
  
  Widget _buildDataCard(String title, String value, String unit) {
    return Card(
      child: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            Text(title, style: TextStyle(fontSize: 16)),
            Text(value, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
            Text(unit, style: TextStyle(fontSize: 12)),
          ],
        ),
      ),
    );
  }
}
```

## 🎯 学习检查点

### 第1周检查点
- [ ] 能够创建基本的Flutter项目
- [ ] 理解Widget和State的概念
- [ ] 能够使用基础组件构建简单界面

### 第2周检查点
- [ ] 掌握布局系统
- [ ] 能够处理用户交互
- [ ] 理解导航和路由

### 第3周检查点
- [ ] 掌握Provider状态管理
- [ ] 能够管理复杂应用状态
- [ ] 理解数据流

### 第4周检查点
- [ ] 能够集成蓝牙功能
- [ ] 实现传感器数据读取
- [ ] 处理硬件连接问题

### 第5周检查点
- [ ] 实现数据持久化
- [ ] 添加网络功能
- [ ] 优化用户体验

## 💡 学习建议

1. **理论与实践结合**: 每学一个概念就立即实践
2. **循序渐进**: 不要跳跃式学习，打好基础
3. **多做项目**: 通过实际项目巩固知识
4. **查阅文档**: 养成查阅官方文档的习惯
5. **社区交流**: 加入Flutter社区，多交流学习

## 🚀 进阶方向

### 1. 性能优化
- 渲染优化
- 内存管理
- 启动速度优化

### 2. 平台特定功能
- Android原生功能集成
- iOS原生功能集成
- 平台通道 (Platform Channels)

### 3. 测试和调试
- 单元测试
- 集成测试
- 性能测试

### 4. 发布和部署
- 应用打包
- 应用商店发布
- 持续集成
