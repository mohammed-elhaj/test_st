import streamlit as st
import time

# Leverage a data-driven approach for color selection
# Consider using tools like Adobe Color or Coolors for inspiration

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
    st.markdown('<div class="title">Speech Recognition App</div>', unsafe_allow_html=True)
    st.markdown(
        """
        This application uses speech recognition to convert video files to text.
        Upload an MP4 video file and the app will process the video to recognize and display the spoken text.
        """,
        unsafe_allow_html=True,
    )

# Main content container with rounded corners and light background
st.container(
    lambda: st.write(""),
    className="main",
)

# Main content heading
st.markdown('<div class="header">Upload your MP4 video file</div>', unsafe_allow_html=True)

# Create a file uploader with clear instructions
st.markdown('<div class="uploader">', unsafe
