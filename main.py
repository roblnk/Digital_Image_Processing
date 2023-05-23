import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Computer Vision",
    page_icon="👋",
)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# LOAD ASSETS
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")

st.write("# Welcome to Computer Vision! 👋")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    Computer vision is a field of artificial intelligence (AI) that enables computers and 
    systems to derive meaningful information from digital images, videos and other visual 
    inputs — and take actions or make recommendations based on that information. 
    If AI enables computers to think, computer vision enables them to see, observe and understand.
    **👈 Select a demo from the sidebar** to see some examples of what Computer Vision can do!
    ### Want to learn more?
    - Check out [What is Computer Vision?](https://www.ibm.com/topics/computer-vision)
    - Orther [Wikipedia](https://vi.wikipedia.org/wiki/Th%E1%BB%8B_gi%C3%A1c_m%C3%A1y_t%C3%ADnh)
"""
)

with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")



