import cv2
import numpy as np
import streamlit as st

L = 256
#-----Function Chapter 5-----#
def CreateMotionfilter(M, N):
    H = np.zeros((M,N), np.complex)
    a = 0.1
    b = 0.1
    T = 1
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi*((u-M//2)*a + (v-N//2)*b)
            if np.abs(phi) < 1.0e-6:
                RE = T*np.cos(phi)
                IM = -T*np.sin(phi)
            else:
                RE = T*np.sin(phi)/phi*np.cos(phi)
                IM = -T*np.sin(phi)/phi*np.sin(phi)
            H.real[u,v] = RE
            H.imag[u,v] = IM
    return H

def CreateMotionNoise(imgin):
    M, N = imgin.shape
    f = imgin.astype(np.float)
    # Buoc 1: DFT
    F = np.fft.fft2(f)
    # Buoc 2: Shift vao the center of the image
    F = np.fft.fftshift(F)

    # Buoc 3: Tao bo loc H
    H = CreateMotionfilter(M, N)

    # Buoc 4: Nhan F voi H
    G = F*H

    # Buoc 5: Shift return
    G = np.fft.ifftshift(G)

    # Buoc 6: IDFT
    g = np.fft.ifft2(G)
    g = g.real
    g = np.clip(g, 0, L-1)
    g = g.astype(np.uint8)
    return g

def CreateInverseMotionfilter(M, N):
    H = np.zeros((M,N), np.complex)
    a = 0.1
    b = 0.1
    T = 1
    phi_prev = 0
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi*((u-M//2)*a + (v-N//2)*b)
            if np.abs(phi) < 1.0e-6:
                RE = np.cos(phi)/T
                IM = np.sin(phi)/T
            else:
                if np.abs(np.sin(phi)) < 1.0e-6:
                    phi = phi_prev
                RE = phi/(T*np.sin(phi))*np.cos(phi)
                IM = phi/(T*np.sin(phi))*np.sin(phi)
            H.real[u,v] = RE
            H.imag[u,v] = IM
            phi_prev = phi
    return H

def DenoiseMotion(imgin):
    M, N = imgin.shape
    f = imgin.astype(np.float)
    # Buoc 1: DFT
    F = np.fft.fft2(f)
    # Buoc 2: Shift vao the center of the image
    F = np.fft.fftshift(F)

    # Buoc 3: Tao bo loc H
    H = CreateInverseMotionfilter(M, N)

    # Buoc 4: Nhan F voi H
    G = F*H

    # Buoc 5: Shift return
    G = np.fft.ifftshift(G)

    # Buoc 6: IDFT
    g = np.fft.ifft2(G)
    g = g.real
    g = np.clip(g, 0, L-1)
    g = g.astype(np.uint8)
    return g


st.title("Chapter 5: Image Restoration and Reconstruction")
st.write("Khôi phục ảnh")

st.markdown(
    f"""<style>
    .stApp {{
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZCZE2MJRYih--8-Y90xKGy2OadWhwlC9IQZ5s_QfLBR_YC4wZmYOsAVJPkesf5-2Rehw&usqp=CAU");
    background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Chọn file ảnh", type=["jpg","jpeg","png","tif"])

if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    st.image(image, caption='Ảnh trước khi xử lý', use_column_width=True)

    option = st.selectbox(
        'Chọn phương thức xử lý ảnh:',
        ('Không', 'CreateMotionfilter', 'CreateMotionNoise', 'CreateInverseMotionfilter', 'DenoiseMotion')
    )

    if option == 'Không':
        st.write("Vui lòng chọn phương thức xử lý ảnh.")
    elif option == 'CreateMotionfilter':
        imgout = CreateMotionfilter(image)
        st.image(imgout, caption='Ảnh sau khi xử lý', use_column_width=True)
    elif option == 'CreateMotionNoise':
        imgout = CreateMotionNoise(image)
        st.image(imgout, caption='Ảnh sau khi xử lý', use_column_width=True)
    elif option == 'CreateInverseMotionfilter':
        imgout = CreateInverseMotionfilter(image)
        st.image(imgout, caption='Ảnh sau khi xử lý', use_column_width=True)
    elif option == 'DenoiseMotion':
        imgout = DenoiseMotion(image)
        st.image(imgout, caption='Ảnh sau khi xử lý', use_column_width=True)