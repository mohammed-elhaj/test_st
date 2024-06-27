import streamlit as st
import time

# Set the page config to use the full width of the screen
st.set_page_config(layout="wide")

# Custom CSS for dark theme styling with a balanced color palette
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;  /* Dark background */
        color: #FFFFFF;  /* White text */
    }
    .main {
        background-color: #2C2C2C;  /* Darker background for main content */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(255,255,255,0.1);  /* Subtle white shadow */
    }
    .title {
        font-size: 2.5em;
        color: #4CAF50;  /* Green title */
        text-align: center;
        margin-bottom: 0.5em;
    }
    .header {
        font-size: 1.75em;
        color: #2196F3;  /* Blue header */
        text-align: center;
        margin-bottom: 1em;
    }
    .subheader {
        font-size: 1.5em;
        color: #FF5722;  /* Orange subheader */
        text-align: center;
        margin-bottom: 0.5em;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .recognized-text {
        font-size: 1.5em;
        color: #FFEB3B;  /* Yellow recognized text */
        text-align: center;
        margin-top: 1em;
        border: 1px solid #333333;  /* Dark border */
        padding: 10px;
        border-radius: 10px;
        background-color: #333333;  /* Dark background for recognized text */
    }
    .uploader {
        display: flex;
        justify-content: center;
        margin-bottom: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo and information
with st.sidebar:
    st.image("lips.png", width=100)
    st.markdown('<div class="title">التعرف على الكلام البصري</div>', unsafe_allow_html=True)
    st.markdown(
        """
        هذا التطبيق يستخدم التعرف على الكلام البصري لتحويل ملفات الفيديو إلى نص.
        قم بتحميل ملف فيديو بتنسيق MP4، وسيقوم التطبيق بمعالجة الفيديو للاعتراف وعرض النص المنطوق.
        """,
        unsafe_allow_html=True
    )

# Main content
st.markdown('<div class="header">قم بتحميل ملف الفيديو MP4 الخاص بك</div>', unsafe_allow_html=True)

# Create a file uploader
st.markdown('<div class="uploader">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["mp4"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        # Display the uploaded video
        st.markdown('<div class="subheader">ملف الفيديو المحمل</div>', unsafe_allow_html=True)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder video

    with col2:
        # Display the processed video
        st.markdown('<div class="subheader">معالجة الفيديو</div>', unsafe_allow_html=True)
        
        # Show a progress bar and message
        progress_message = st.empty()
        progress_bar = st.empty()
        
        progress_message.markdown('<div class="subheader">جارٍ معالجة الفيديو...</div>', unsafe_allow_html=True)
        progress_bar = progress_bar.progress(0)
        
        for percent_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(percent_complete + 1)

        # Clear the progress message and bar
        progress_message.empty()
        progress_bar.empty()
        
        # Show the processed video
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder video

        # Show a spinner while processing
        with st.spinner('جارٍ تشغيل التعرف على الكلام...'):
            time.sleep(2)  # Simulate processing time

        # Show the result
        st.success("اكتملت عملية المعالجة!")
        st.markdown('<div class="subheader">النص المعترف به</div>', unsafe_allow_html=True)
        st.markdown('<div class="recognized-text">لقد قلت: [نص معترف به]</div>', unsafe_allow_html=True)

else:
    st.warning("الرجاء تحميل ملف فيديو MP4.")
