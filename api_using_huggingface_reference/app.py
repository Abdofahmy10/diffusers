import streamlit as st 
from help import RealVisXL , runwayml , cetusmix ,convert_bytes_to_image

model_1 = RealVisXL
model_2 = runwayml
model_3 = cetusmix

def main():
    st.sidebar.title("Generative Ai ")
    model= st.sidebar.selectbox("Select your model", ("anime", "clip"))

    # Display the input controls for Text2Img task
    st.title("Text2Img Using diffusers ❤ ")
    text = st.text_area("Enter the text")
    generate_button = st.button("Generate")

    if generate_button:
            # Render different windows based on the selected task
        if model == "anime":
            with st.spinner("Loading model..."):
                image_bytes = model_3({
                                    "inputs": text,
                                    })
                img = convert_bytes_to_image(image_bytes)
                st.image(img, caption="Generated Image")

          
        elif model == "RealVisXL":
                with st.spinner("Loading model..."):
                    image_bytes = model_1({
                                        "inputs": text,
                                        })
                    img = convert_bytes_to_image(image_bytes)
                    st.image(img, caption="Generated Image")  


        elif model == "clip":
                with st.spinner("Loading model..."):
                    image_bytes = model_2({
                                        "inputs": text,
                                        })
                    img = convert_bytes_to_image(image_bytes)
                    st.image(img, caption="Generated Image")

if __name__ == "__main__":
    main()