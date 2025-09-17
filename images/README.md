# 图片资源说明

## 📸 图片文件说明

这个文件夹用于存放项目相关的图片资源，确保在GitHub上能正确显示。

## 🖼️ 需要的图片文件

### 1. Flora开发板图片
- **文件名**: `flora.jpg`
- **描述**: Adafruit Flora开发板图片
- **用途**: 在项目文档中展示Flora硬件

### 2. ZSWatch图片
- **文件名**: `zswatch.png`
- **描述**: ZSWatch智能手表图片
- **用途**: 在项目文档中展示ZSWatch硬件

## 📁 如何添加图片

### 方法1: 通过GitHub Web界面
1. 访问: https://github.com/SailCPU/legend-motion-app
2. 进入 `images` 文件夹
3. 点击 "Add file" → "Upload files"
4. 拖拽或选择图片文件上传
5. 提交更改

### 方法2: 通过Git命令
```bash
# 添加图片到images文件夹
cp your-image.jpg "/Users/sail/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyKnowledgeBase/projects/Legend Motion App/images/flora.jpg"

# 提交更改
cd "/Users/sail/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyKnowledgeBase/projects/Legend Motion App"
git add images/
git commit -m "Add project images"
git push origin main
```

## 🔗 图片链接格式

在Markdown文件中使用以下格式引用图片：

### GitHub绝对路径（推荐）
```markdown
![图片描述](https://raw.githubusercontent.com/SailCPU/legend-motion-app/main/images/图片文件名)
```

### 相对路径（本地使用）
```markdown
![图片描述](images/图片文件名)
```

### 从子文件夹引用
```markdown
![图片描述](../images/图片文件名)
```

## 📋 已添加的图片

- [x] `flora.jpg` - Adafruit Flora开发板
- [x] `zswatch.png` - ZSWatch智能手表

## 📋 待添加的图片

- [ ] `esp32.jpg` - ESP32开发板
- [ ] `prototype-screenshot.png` - 原型界面截图

## 💡 图片要求

- **格式**: JPG, PNG, SVG
- **大小**: 建议不超过1MB
- **分辨率**: 建议800x600以上
- **命名**: 使用英文和数字，避免特殊字符
