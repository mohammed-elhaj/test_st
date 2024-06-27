import streamlit as st
import time

# Set the page config to use the full width of the screen
st.set_page_config(layout="wide")

# Custom CSS for refined styling with the updated color palette and professional design
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #000000;  /* Black background */
        color: #FFFFFF;  /* White text */
        line-height: 1.6;
    }
    .sidebar {
        background-color: #FF6600;  /* Orangish sidebar background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);  /* Subtle shadow */
    }
    .main {
        background-color: #222222;  /* Dark gray main content background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);  /* Subtle shadow */
    }
    .title {
        font-size: 2.8em;
        color: #FFFFFF;  /* White title text */
        text-align: center;
        margin-bottom: 0.3em;
    }
    .header {
        font-size: 2em;
        color: #FF6600;  /* Orange header text */
        text-align: center;
        margin-bottom: 0.8em;
    }
    .subheader {
        font-size: 1.8em;
        color: #669900;  /* Green subheader text */
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
        color: #FF6600;  /* Orange recognized text */
        text-align: center;
        margin-top: 1em;
        padding: 10px;
        border-radius: 10px;
        background-color: #222222;  /* Dark gray background for recognized text */
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);  /* Subtle shadow */
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
