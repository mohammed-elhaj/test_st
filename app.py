import streamlit as st
import time

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
        font-size: 2em;
        color: #4CAF50;
    }
    .header {
        font-size: 1.5em;
        color: #2196F3;
    }
    .subheader {
        font-size: 1.2em;
        color: #FF5722;
    }
    .center {
        display: flex;
        justify-content: center;
    }
    .logo {
        max-width: 100px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo
st.markdown('<div class="center"><img class="logo" src="lips.png" alt="Lips Logo"></div>', unsafe_allow_html=True)
st.image("lips.png", width=100)  # Added this line to ensure image is displayed

# Set the title of the app
st.markdown('<div class="title">Visual Speech Recognition</div>', unsafe_allow_html=True)

# Add a header
st.markdown('<div class="header">Upload your MP4 video file</div>', unsafe_allow_html=True)

# Create a file uploader
uploaded_file = st.file_uploader("Choose an MP4 video", type=["mp4"])

# Use columns for better layout
col1, col2 = st.columns(2)

if uploaded_file is not None:
    with col1:
        # Display the uploaded video
        st.markdown('<div class="subheader">Uploaded Video</div>', unsafe_allow_html=True)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder video

    with col2:
        # Display the processed video
        st.markdown('<div class="subheader">Processed Video</div>', unsafe_allow_html=True)

        # Show a progress bar
        st.markdown('<div class="subheader">Processing Video...</div>', unsafe_allow_html=True)
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(percent_complete + 1)

        # Re-render the section to remove the progress bar
        st.markdown('<div class="subheader">Processing Video...</div>', unsafe_allow_html=True)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder video

        # Show a spinner while processing
        with st.spinner('Running speech recognition...'):
            time.sleep(2)  # Simulate processing time

        # Show the result
        st.success("Processing complete!")
        st.markdown('<div class="subheader">Recognized Speech</div>', unsafe_allow_html=True)
        st.text("You said: [recognized speech placeholder]")
else:
    st.warning("Please upload an MP4 video file.")

# Add an expander for additional information
with st.expander("About this App"):
    st.write("""
        This application uses visual speech recognition to convert video inputs to text. 
        Upload an MP4 video, and the app will process the video to recognize and display the spoken text.
    """)
