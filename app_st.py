import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the model
model_path = "path_to_your_saved_model"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)
model.eval()

st.title("Chatbot")

input_text = st.text_input("You:", "")

if st.button("Reply"):
    if input_text:
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        output_ids = model.generate(input_ids, max_length=50)
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        st.text_area("Chatbot:", value=output_text, height=100)
    else:
        st.write("Please enter some text to get a reply.")
