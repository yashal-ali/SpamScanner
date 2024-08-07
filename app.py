import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# Add background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/premium-photo/fiber-optics-background-generative-ai_1041269-730.jpg");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
}
.st-emotion-cache-1gulkj5 {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    padding: 1rem;
    background-color:none ;
    border-radius: 0.5rem;
    border: #ad9a9a 2px solid !important;
    color: rgb(49, 51, 63);
    background: none;
}
img {
    width: 200px !important
}
.st-emotion-cache-7ym5gk{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color:#921691 !important;
    border: 1px solid rgba(49, 51, 63, 0.2);
    color: white;
    padding: 5px;
    min-width:150px 
}
.st-emotion-cache-1n76uvr {
    width: 704px;
    position: relative;
    display: flex;
    flex: 1 1 0%;
    flex-direction: column;
    padding : 50px
    
}
.st-emotion-cache-1r4qj8v {
    position: absolute;
    background: rgb(255, 255, 255);
    color: rgb(49, 51, 63);
    inset: 0px;
    color-scheme: light;
    overflow: hidden;
}
.st-emotion-cache-1n76uvr {
    width: 780px;
    position: relative;
    display: flex;
    flex: 1 1 0%;
    flex-direction: column;
    background-color: rgba(0, 0, 0, 0.7); !important
    padding:50px !important;
    border-radius: 26px;
}
.st-emotion-cache-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    padding-left: 20px;
}
p, ol, ul, dl {
    margin: -21px 19px 1rem;
    padding: 0px;
    font-size: 1rem;
    font-weight: 400;
    color: honeydew;
}
.st-emotion-cache-9ycgxx {
    margin-bottom: 0.25rem;
    color: honeydew;
}
.st-emotion-cache-1aehpvj {
    color: rgba(49, 51, 63, 0.6);
    font-size: 14px;
    line-height: 1.25;
    color: honeydew;
}
.similar-images-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
}

.similar-image {
    margin-bottom: 10px;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.similar-image img {
    width: 100%;
    height: auto;
    object-fit: cover;
}
st-emotion-cache-16idsys p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 20px;
}
.st-bs {
    color: rgb(29 67 40);
}

.st-emotion-cache-5rimss p {
    word-break: break-word;
    font-size: 24px;
}
.st-emotion-cache-10trblm {
   
    color: white !important;
    font-size: 49px;
    margin: 20px;
    padding-left: 20px;
}
.st-c0 {
    min-height: 169px;
    border: 1px solid;
    background: #bfbaba;
    border-radius: 20px;
    box-shadow: 10px 10px black;
    color: #0e101a;
}
.st-emotion-cache-7ym5gk {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: #921691 !important
    border: 1px solid rgba(49, 51, 63, 0.2);
    color: white;
    padding: 10px;
    min-width: 150px;

}

.st-emotion-cache-183lzff {
    white-space: pre;
    font-size: 30px;
    justify-content: center;
    align-items: center;
    display: flex;
    margin: 5px;
    font-style: italic;
    font-weight: bolder;
    background: none;
    padding: 10px;
    border-radius: none;
    text-align: center;
    margin-left: 48px;
    color :white !important;
}

.st-emotion-cache-1vbkxwb p {
    word-break: break-word;
    margin-top: -10px !important;
    font-size: 24px;
    text-align: center;
    font-weight:900;
}

.st-b1 {
     background-color: transparent !important;
}

.st-b0 {
    border-bottom-color: transparent !important;
     border-bottom-color:none;

.st-az {
    border-top-color: none;
    border-top-color:  transparent !important;
}

.st-ay {
     border-right-color:none;
     border-right-color :transparent !important;
}

.st-ax {
    border-left-color: none;
     border-left-color: transparent !important;
}

</style>
"""
# Set the background image using st.markdown

st.markdown(background_image, unsafe_allow_html=True)

# Add title with emoji
st.markdown("<h1 style='text-align: center;'>📧 SMS Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <p>This application classifies whether an entered SMS or email message is Spam or Not Spam. 
        It uses Natural Language Processing (NLP) techniques to preprocess the text and a trained 
        machine learning model to make predictions.</p>
    </div>
""", unsafe_allow_html=True)
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.text("The Above Message is : Spam")
    else:
        st.text("The Above Message is : Not Spam")
