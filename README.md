# gmailAPI
Send and Search messages via gmailAPI


Gmail API is an API that helps us to create, search, search messages and to manage gmail settings. In this section, the authorize, create, send and search features were implemented in python. Please follow the below steps to use the folder:

1. Prerequisites

   * Python 2.4 or greater (to provide a web server)
   * A Google account with GmailAPI enabled

2. Clone or download the folder is the location where you like to work(current working directory - cwd)

3. Enable the Gmail API

    Please enable the Gmail API by following the below link:
    https://developers.google.com/gmail/api/quickstart/python

4. After enabling the API, download and save the client configuration as "credentials.json" in the cwd

5. Open the python terminal and run the main.py file 

6. Give the required input as directed and play with it!


*******************************************************************************************************************************************
                                                         IMPORTANT TO NOTE
*******************************************************************************************************************************************
1. While running for the first time, gmail will give an error message "This app isn't verified". Please do the below steps to allow the application to access the email:
    * Go to Advanced
    * Grant permisstion
    * Allow Now, the authentication is completed
2. The libraries needed for the application should also be installed by using the below command:
     pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib   

