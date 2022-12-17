import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride'''

'''_______________________________________________________________________________'''

#date and time
pickup_date = st.date_input(
    "Enter your pickup datetime",
    datetime.date(2014, 7, 6))
st.write('Your pickup datetime is:', pickup_date)
pickup_datetime = str(pickup_date) + ' 17:18:00'

'''_______________________________________________________________________________'''

#pickup longitude
pickup_longitude = st.number_input('Enter the pickup longitude',-73.950655)
st.write('Your pickup longitude  is ', pickup_longitude)

'''_______________________________________________________________________________'''

#pickup latitude
pickup_latitude = st.number_input('Enter the pickup latitude',40.783282)
st.write('Your pickup latitude  is ', pickup_latitude)

'''_______________________________________________________________________________'''

#dropoff longitude
dropoff_longitude = st.number_input('Enter the dropoff longitude',-73.984365)
st.write('Your dropoff longitude  is ', dropoff_longitude)

'''_______________________________________________________________________________'''

#dropoff latitude
dropoff_latitude = st.number_input('Enter the dropoff latitude',40.769802)
st.write('Your dropoff latitude  is ', dropoff_latitude)

'''_______________________________________________________________________________'''

#passenger count
passenger_count = st.slider('Select the number of passengers', 0, 10, 2)
st.write('Total passengers: ', passenger_count)

'''_______________________________________________________________________________'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''2. Let's build a dictionary containing the parameters for our API...'''

params = dict(pickup_datetime = pickup_datetime,
              pickup_longitude = pickup_longitude,
              pickup_latitude = pickup_latitude,
              dropoff_longitude = dropoff_longitude,
              dropoff_latitude = dropoff_latitude,
              passenger_count = passenger_count)

'''3. Let's call our API using the `requests` package...'''

r = requests.get(url,params = params).json()
'''4. Let's retrieve the prediction from the **JSON** returned by the API...'''

fare = r["fare"]
st.title('Your fare is:')
st.title('{0:.2f}'.format(fare))
