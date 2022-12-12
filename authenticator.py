import streamlit as st
import streamlit_authenticator as stauth
import yaml
import logging
from datetime import datetime

officehour_start="09:00:00"
officehour_end="12:00:00"

logging.basicConfig(filename='authenticator.log')
logging.info('info mode')
currenttime=format(datetime.now())
logging.info('Logging time is: ' + currenttime)

logintime=datetime.strftime(datetime.utcnow(),"%H:%M:%S")

if (logintime > officehour_end or logintime < officehour_start):
    logging.info('ERROR: login outside of office hours - 9:00-12:00')
    st.error('You cannot login outside of office hours - 9:00-12:00')

hashed_passwords = stauth.Hasher(['123', '456']).generate()

with open('config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
    logging.info(authentication_status)
elif authentication_status == None:
    st.warning('Please enter your username and password during working hours: M-F 9:00-12:00EST')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
    logging.info('ERROR: user/password incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password during working hours: M-F 9:00-12:00EST')

if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

    try:
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
        if username_forgot_pw:
            st.success('New password sent securely')
        # Random password to be transferred to user securely
        elif username_forgot_pw == False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    try:
        username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
        if username_forgot_username:
            st.success('Username sent securely')
            # Username to be transferred to user securely
        elif username_forgot_username == False:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

    if authentication_status:
        try:
            if authenticator.update_user_details(username, 'Update user details'):
                st.success('Entries updated successfully')
        except Exception as e:
            st.error(e)

with open('../config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
