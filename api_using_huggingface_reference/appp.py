import streamlit as st 
from help import RealVisXL , runwayml , cetusmix ,convert_bytes_to_image

model = RealVisXL
def main():
    st.sidebar.title("Generative Ai ")
    
    st.title("Text2Img")
    text = st.text_area("Enter the text")
    generate_button = st.button("Generate")

    if generate_button:
           
       
            image_bytes = model({
	                              "inputs": text,
                                })
            img = convert_bytes_to_image(image_bytes)
            st.image(img, caption="Generated Image")

          
       
if __name__ == "__main__":
    main()