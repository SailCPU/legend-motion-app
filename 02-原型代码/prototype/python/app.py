from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
import sqlite3
import json
from datetime import datetime
import threading
import time
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# 全局变量
is_monitoring = False
sensor_data = {
    'heart_rate': 0,
    'steps': 0,
    'calories': 0,
    'activity_level': 0
}

# 数据库初始化
def init_db():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            heart_rate INTEGER,
            steps INTEGER,
            calories REAL,
            activity_level INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("数据库初始化完成")

# 模拟传感器数据生成
def generate_sensor_data():
    global sensor_data
    while is_monitoring:
        # 模拟心率数据 (60-120 BPM)
        sensor_data['heart_rate'] = random.randint(60, 120)
        
        # 模拟步数增加
        sensor_data['steps'] += random.randint(1, 3)
        
        # 模拟卡路里计算 (基于步数)
        sensor_data['calories'] = round(sensor_data['steps'] * 0.04, 1)
        
        # 模拟活动强度 (1-5级)
        sensor_data['activity_level'] = random.randint(1, 5)
        
        # 发送数据到前端
        socketio.emit('sensor_data', sensor_data)
        
        # 保存到数据库
        save_sensor_data(sensor_data)
        
        time.sleep(2)  # 每2秒更新一次

# 保存传感器数据到数据库
def save_sensor_data(data):
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (heart_rate, steps, calories, activity_level)
        VALUES (?, ?, ?, ?)
    ''', (data['heart_rate'], data['steps'], data['calories'], data['activity_level']))
    conn.commit()
    conn.close()

# 路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 100')
    data = cursor.fetchall()
    conn.close()
    
    # 转换为字典格式
    result = []
    for row in data:
        result.append({
            'id': row[0],
            'timestamp': row[1],
            'heart_rate': row[2],
            'steps': row[3],
            'calories': row[4],
            'activity_level': row[5]
        })
    
    return jsonify(result)

@app.route('/api/start_monitoring', methods=['POST'])
def start_monitoring():
    global is_monitoring
    if not is_monitoring:
        is_monitoring = True
        # 启动传感器数据生成线程
        sensor_thread = threading.Thread(target=generate_sensor_data)
        sensor_thread.daemon = True
        sensor_thread.start()
        return jsonify({'status': 'success', 'message': '监测已开始'})
    return jsonify({'status': 'error', 'message': '监测已在运行'})

@app.route('/api/stop_monitoring', methods=['POST'])
def stop_monitoring():
    global is_monitoring
    is_monitoring = False
    return jsonify({'status': 'success', 'message': '监测已停止'})

@app.route('/api/clear_data', methods=['POST'])
def clear_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sensor_data')
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'message': '数据已清除'})

@app.route('/api/export_data')
def export_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC')
    data = cursor.fetchall()
    conn.close()
    
    # 转换为CSV格式
    csv_data = "时间,心率,步数,卡路里,活动强度\n"
    for row in data:
        csv_data += f"{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n"
    
    return csv_data, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=sensor_data.csv'
    }

# WebSocket事件
@socketio.on('connect')
def handle_connect():
    print('客户端已连接')
    emit('status', {'message': '连接成功', 'connected': True})

@socketio.on('disconnect')
def handle_disconnect():
    print('客户端已断开连接')

@socketio.on('start_monitoring')
def handle_start_monitoring():
    global is_monitoring
    if not is_monitoring:
        is_monitoring = True
        sensor_thread = threading.Thread(target=generate_sensor_data)
        sensor_thread.daemon = True
        sensor_thread.start()
        emit('monitoring_status', {'monitoring': True, 'message': '监测已开始'})
    else:
        emit('monitoring_status', {'monitoring': True, 'message': '监测已在运行'})

@socketio.on('stop_monitoring')
def handle_stop_monitoring():
    global is_monitoring
    is_monitoring = False
    emit('monitoring_status', {'monitoring': False, 'message': '监测已停止'})

if __name__ == '__main__':
    init_db()
    print("服务器启动中...")
    print("访问地址: http://localhost:5000")
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
