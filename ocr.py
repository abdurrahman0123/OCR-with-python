import cv2
import pytesseract #if any occur pytesseract.pytesseract.tesseract_cmd=r'C:Program FilesTesseract-OCRtesseract.exe' 
import streamlit as st
from pytesseract import Output
def get_grayscale(image):
   st.title("Upload")
    
    
with st.container():
    st.header('OCR with python')
    st.subheader("upload your image ") 
    img= st.file_uploader("Upload Your Dataset")
    
    img = cv2.imread("image.jpg")
    img = get_grayscale(img)
    img = cv2.resize(img, (400, 450))


    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
    st.show("Image", img)
    text = pytesseract.image_to_string(img)
    st.write(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
