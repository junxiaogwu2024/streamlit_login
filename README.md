# streamlit_login_splunk
GWU SEAS8414 - streamlit login exercise for creating splunk dashboard
This is an enhancement to an existing streamlint authentication code in github contributed by https://github.com/mkhorasani.
The oringial source code is at 
https://github.com/mkhorasani/Streamlit-Authenticator.git
The new file is called authenticator.py which captures the login failures and hours to generate errors in the log for splunk dashboard purpose.

Setup Steps:
1. install git, docker, streamlit by using yum install
2. sudo bash to the Linux terminal
3. run the following command first
    a. systemctl start docker
    b. export PATH=$PATH:/usr/local/bin
4. start the authenticator program by execute this command:
    streamlit run authenticator.py --logger.level=info 2>info.log
5. Go to a browser and type host-ip-address:8051
  
  ![image](https://user-images.githubusercontent.com/116442253/207199243-ee6cb763-7219-45e6-a842-db5a1d027f9e.png)


6. login using any combination of username/password for username/password incorrect test.
7. For after hours testing, the correct username/password pairs are:

    jsmith/123
    
    rbriggs/456
  
8. You can find the output logs in the info.log file
