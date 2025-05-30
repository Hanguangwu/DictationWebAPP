# 听写练习WebAPP

一个基于Streamlit开发的听写练习Web应用，支持文本转语音功能，帮助用户进行听写训练。

## 功能特点

- 📝 **文本输入**：支持输入任意中英文文本
- 🔊 **语音生成**：使用pyttsx3引擎将文本转换为语音
- 🎵 **音频播放**：内置音频播放器，支持重复播放
- 📱 **响应式设计**：适配各种设备屏幕
- 🎯 **听写练习**：隐藏原文，专注听写训练

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址为：http://localhost:8501

## 使用方法

1. **输入文本**：在左侧文本框中输入要进行听写练习的内容
2. **生成语音**：点击"生成语音"按钮，系统将把文本转换为语音
3. **播放练习**：在右侧点击播放按钮开始听写练习
4. **查看原文**：可以展开"查看原文"来对照答案

## 技术栈

- **前端框架**：Streamlit
- **语音合成**：pyttsx3
- **编程语言**：Python 3.7+

## 项目结构

```
DictationWebAPP/
├── app.py              # 主应用文件
├── requirements.txt    # 依赖包列表
└── README.md          # 项目说明文档
```

## 注意事项

- 确保系统已安装音频驱动和扬声器
- 首次运行可能需要下载语音引擎组件
- 建议使用Chrome或Firefox浏览器以获得最佳体验

## 许可证

MIT License