import streamlit as st
import time

# Set the page config to use the full width of the screen
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 2.5em;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .header {
        font-size: 1.75em;
        color: #2196F3;
        text-align: center;
        margin-bottom: 1em;
    }
    .subheader {
        font-size: 1.5em;
        color: #FF5722;
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
        color: #333333;
        text-align: center;
        margin-top: 1em;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .sidebar-content {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo and information
with st.sidebar:
    st.image("lips.png", width=100)
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown('<div class="title">Visual Speech Recognition</div>', unsafe_allow_html=True)
    st.markdown(
        """
        This application uses visual speech recognition to convert video inputs to text. 
        Upload an MP4 video, and the app will process the video to recognize and display the spoken text.
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Main content
st.markdown('<div class="header">Upload your MP4 video file</div>', unsafe_allow_html=True)

# Create a file uploader
uploaded_file = st.file_uploader("", type=["mp4"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        # Display the uploaded video
        st.markdown('<div class="subheader">Uploaded Video</div>', unsafe_allow_html=True)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder video

    with col2:
        # Display the processed video
        st.markdown('<div class="subheader">Processed Video</div>', unsafe_allow_html=True)
        
        # Show a progress bar and message
        progress_message = st.empty()
        progress_bar = st.empty()
        
        progress_message.markdown('<div class="subheader">Processing Video...</div>', unsafe_allow_html=True)
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
        with st.spinner('Running speech recognition...'):
            time.sleep(2)  # Simulate processing time

        # Show the result
        st.success("Processing complete!")
        st.markdown('<div class="subheader">Recognized Speech</div>', unsafe_allow_html=True)
        st.markdown('<div class="recognized-text">You said: [recognized speech placeholder]</div>', unsafe_allow_html=True)

else:
    st.warning("Please upload an MP4 video file.")
