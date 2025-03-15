import streamlit as st
import base64

@st.cache_resource
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image
def set_background_image(png_file):
    base64_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Use your own image path here
image_path = 'media/Bitcoin.png'
set_background_image(image_path)

st.header(":blue[Crypto Price Prediction]:coin:")


st.markdown('Crypto Price Prediction is the webapp based on Machine Learning model that predicts the future closing price.')

st.markdown('----')
st.markdown('# Language/Libraries used?')
st.markdown('API: yfinance python scraped the data from Yahoo Finance')
st.markdown('Data Wrangling: Pandas, Numpy')
st.markdown('Data Visualisation: Matplotlib, Seaborn')
st.markdown('Data Modeling: Scikit: Learn, TensorFlow, Keras')
st.markdown('Database: SQL')
st.markdown('Webapp: Streamlit')
st.markdown('IDE: Jupyter Notebook/ VS CODE')

st.markdown('----')
st.markdown('# Which Machine Learning Model is used in this webapp?')
st.markdown('LSTM is used in this webapp.')
st.markdown('LSTMs are widely used for sequence prediction problems and have proven to be extremely effective. The reason they work so well is that LSTM is able to store past information that is important and forget the information that is not.')
st.markdown('LSTM has three gates:')
st.markdown('a. The input gate: The input gate adds information to the cell state.')
st.markdown('b. The forget gate: It removes the information that is no longer required by model.')
st.markdown('c. The output gate: The output Gate at LSTM selects the information to be shown as output This deep learning model has done some work here.')

st.markdown('----')
st.markdown('# What is the accuracy of the model?')
st.markdown('It has recognized all the potential upward and downtrends in stock prices. It is much more efficient compared to all other different ML models and the **Accuracy of the model is 97%**.')
import base64

