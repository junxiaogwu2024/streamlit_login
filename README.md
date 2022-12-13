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
  
8. You can find the output logs in the info.log file with the following information

ERROR: hostname, ip-address, timestamp(hh:mm:ss), Error_Code, username

2022-12-13 01:07:53.007 info mode start
2022-12-13 01:07:53.697 ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:07:53,False,asdad
2022-12-13 01:07:53.698 ERROR: user/password incorrect
2022-12-13 01:07:53.698 ERROR:ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:07:53,ERROR_CREDENTIAL,asdad
2022-12-13 01:08:02.740 info mode start
2022-12-13 01:08:03.432 ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:08:03,False,junsad
2022-12-13 01:08:03.432 ERROR: user/password incorrect
2022-12-13 01:08:03.433 ERROR:ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:08:03,ERROR_CREDENTIAL,junsad
2022-12-13 01:08:10.334 info mode start
2022-12-13 01:08:11.025 ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:08:11,False,jubsda
2022-12-13 01:08:11.026 ERROR: user/password incorrect
2022-12-13 01:08:11.026 ERROR:ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:08:11,ERROR_CREDENTIAL,jubsda
2022-12-13 01:09:30.747 info mode start
2022-12-13 01:09:31.784 ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:09:31,True,jsmith
2022-12-13 01:09:31.784 ERROR: login outside of office hours - 9:00-12:00
2022-12-13 01:09:31.785 ERROR:ip-10-0-46-173.ap-northeast-1.compute.internal,10.0.46.173,01:09:31,ERROR_TIME,jsmith
