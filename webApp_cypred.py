import pickle

import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image

loaded_model = pickle.load(open('C:/Users/anrut/Downloads/cy_trained_model.sav', 'rb'))

def crop_yield_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,17)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)
    return prediction
def main():
    with st.sidebar:
        selected=option_menu(menu_title='Main Menu',options=['About','Predict','Visualization'])
    if selected=='Predict':
        nav1()
    elif selected=='About':
        nav3()
    else :
        st.title('Visualization')
        nav2()


def nav1():
    # giving a title
    st.title('Crop Yield Prediction Web App')

    # getting the input data from the user

    avg_temp = st.text_input('Average Temperature ')
    pesticides = st.text_input('Pesticides Tones ')
    avg_rain = st.text_input('Average Rainfall')
    country = st.selectbox('Country',('Australia','Country_Brazil','India','Japan','Mexico'))
    crop = st.selectbox('Crop',('Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Wheat','Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams'))
    country_lt = ['Australia','Country_Brazil','India','Japan','Mexico']
    crop_lt=['Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Wheat','Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams']
    t_val = [avg_temp,pesticides,avg_rain]
    cn_ind=0
    for i in range(0, len(country_lt)):
        if country == country_lt[i]:
            cn_ind = i
    k = 0
    while k < 5:
        if k == cn_ind:
            t_val.append(1)
        else:
            t_val.append(0)
        k += 1
    c_ind=0
    for i in range(0, len(crop_lt)):
        if crop == crop_lt[i]:
            c_ind = i
    k = 0
    while k < 9:
        if k == c_ind:
            t_val.append(1)
        else:
            t_val.append(0)
        k += 1


    yield_pd=0
    if st.button('Yield Prediction '):
        yield_pd = crop_yield_prediction(t_val)

    st.success(yield_pd)
def nav2():
    html_temp = "<div class='tableauPlaceholder' id='viz1654605982729' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;cr&#47;cropYeildC&#47;Sheet6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='cropYeildC&#47;Sheet6' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;cr&#47;cropYeildC&#47;Sheet6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1654605982729');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"

    components.html(html_temp,height=600,width=600,scrolling=True)

def nav3():
    st.title('About')
   # info='Agriculture plays a critical role in the global economy. With the continuing expansion of the human population understanding worldwide crop yield is central to addressing food security challenges and reducing the impacts of climate change.'
    #st.text(info)
    image = Image.open('D:/Hands-On Machine Learning Course/projects/about_img.png')

    st.image(image)

if __name__ == '__main__':
    main()




