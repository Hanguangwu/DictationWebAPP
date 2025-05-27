import streamlit as st
import pyttsx3
import tempfile
import os
from pathlib import Path

# 设置页面配置
st.set_page_config(
    page_title="听写练习WebAPP",
    page_icon="🎧",
    layout="wide"
)

# 页面标题
st.title("🎧 听写练习WebAPP")
st.markdown("---")

# 初始化session state
if 'audio_file' not in st.session_state:
    st.session_state.audio_file = None
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""

def text_to_speech(text):
    """
    将文本转换为语音文件
    
    Args:
        text (str): 要转换的文本
    
    Returns:
        str: 生成的音频文件路径
    """
    try:
        # 初始化TTS引擎
        engine = pyttsx3.init()
        
        # 获取可用语音
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            # 使用第二个语音（通常是女声）
            engine.setProperty('voice', voices[1].id)
        
        # 设置语音速度
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)  # 稍微慢一点，便于听写
        
        # 创建临时文件
        temp_dir = tempfile.gettempdir()
        audio_file = os.path.join(temp_dir, "dictation_audio.wav")
        
        # 保存语音到文件
        engine.save_to_file(text, audio_file)
        engine.runAndWait()
        engine.stop()
        
        return audio_file
    except Exception as e:
        st.error(f"语音生成失败: {str(e)}")
        return None

# 创建两列布局
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 输入要听写的文本")
    
    # 文本输入框
    input_text = st.text_area(
        "请输入文本内容：",
        height=200,
        placeholder="请在此输入要进行听写练习的文本内容...",
        help="输入完成后点击'生成语音'按钮"
    )
    
    # 生成语音按钮
    if st.button("🔊 生成语音", type="primary", use_container_width=True):
        if input_text.strip():
            with st.spinner("正在生成语音，请稍候..."):
                audio_file = text_to_speech(input_text.strip())
                if audio_file and os.path.exists(audio_file):
                    st.session_state.audio_file = audio_file
                    st.session_state.generated_text = input_text.strip()
                    st.success("✅ 语音生成成功！")
                else:
                    st.error("❌ 语音生成失败，请重试")
        else:
            st.warning("⚠️ 请先输入文本内容")

with col2:
    st.subheader("🎵 语音播放")
    
    if st.session_state.audio_file and os.path.exists(st.session_state.audio_file):
        st.success("语音已准备就绪")
        
        # 显示生成的文本
        with st.expander("查看原文", expanded=False):
            st.text(st.session_state.generated_text)
        
        # 播放音频
        try:
            with open(st.session_state.audio_file, 'rb') as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/wav')
        except Exception as e:
            st.error(f"音频播放失败: {str(e)}")
    else:
        st.info("请先输入文本并生成语音")

# 添加使用说明
st.markdown("---")
with st.expander("📖 使用说明"):
    st.markdown("""
    ### 如何使用听写练习WebAPP：
    
    1. **输入文本**：在左侧文本框中输入要进行听写练习的内容
    2. **生成语音**：点击"生成语音"按钮，系统将把文本转换为语音
    3. **播放练习**：在右侧点击播放按钮开始听写练习
    4. **查看原文**：可以展开"查看原文"来对照答案
    
    ### 功能特点：
    - 🎯 支持中英文文本转语音
    - 🔊 可调节语音速度，适合听写练习
    - 📱 响应式设计，支持各种设备
    - 💾 自动保存生成的语音文件
    """)

# 页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>💡 听写练习WebAPP - 提升听力和书写能力</div>",
    unsafe_allow_html=True
)