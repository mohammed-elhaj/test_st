import streamlit as st
import time

# Set the page config to use the full width of the screen
st.set_page_config(layout="wide")

# Custom CSS for styling with the curated color palette
primary_color = "#336699"  # Dark blue (can be adjusted based on data/preference)
secondary_color = "#FFCC00"  # Orange (complementary color for contrast)
accent_color = "#CCFF99"  # Light green (accent for buttons and highlights)

# Set the page config to use the full width of the screen
st.set_page_config(
    layout="wide",
    page_title="Speech Recognition App",  # Clear and descriptive title
    page_icon="️",  # Speech bubble icon for visual appeal
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: """
    + primary_color
    + """;
        color: white;
        font-family: sans-serif;  /* Specify a user-friendly font */
    }
    .main {
        background-color: #f5f5f5;  /* Light background for readability */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);  /* Subtle shadow */
    }
    .title {
        font-size: 2.5em;
        color: white;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .header {
        font-size: 1.75em;
        color: """
    + secondary_color
    + """;
        text-align: center;
        margin-bottom: 1em;
    }
    .subheader {
        font-size: 1.5em;
        color: #333;  /* Darker text for better contrast */
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
        color: """
    + secondary_color
    + """;
        text-align: center;
        margin-top: 1em;
        border: 1px solid #ddd;  /* Lighter border for subtlety */
        padding: 10px;
        border-radius: 10px;
        background-color: white;
    }
    .uploader {
        display: flex;
        justify-content: center;
        margin-bottom: 1em;
    }
    .button {
        background-color: """
    + accent_color
    + """;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;  /* Add some spacing */
    }
    .button:hover {
        background-color: """
    + str(hex(int(accent_color[1:], 16) + 55555)[2:])  # Darken on hover
    + """;
    }
    </style>
    """,
    unsafe_allow_html=True,
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
