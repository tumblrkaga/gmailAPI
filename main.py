
from authorize import authorization
from create_msg import create_message
from send_msg import send_message
from search_msg import list_matching_messages

#importing other     modules that are used in the current module.

class Info:

    def __init__(self, sender, recipient, subject, content, key):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.content = content
        self.key = key
        self.user_id = 'me'

        """ Scope represents the to operations like read/write access given to the user. 
            Please refer the below link for more information
          - https://developers.google.com/gmail/api/auth/scopes
          If modifying these scopes, delete the file token.pickle.
        """
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.modify']

       
    @classmethod
    def get_user_input(cls):
        while 1:
            try:                
                key = input('Preferred task:\n 1. Send an email with attachment \n 2. Search for a message\n Your input: ')
                if key == '1':
                    sender = input('Enter sender\'s e-mail:\n')
                    recipient = input('Enter recipient\'s e-mail:\n')
                    subject = input('Enter the subject of the e-mail: \n')
                    content = input('Enter the content of the e-mail: \n')
                    return cls(sender, recipient, subject, content, key)
                elif key == '2':
                    sender = ''
                    recipient = ''
                    subject = ''
                    content = ''
                    return cls(sender, recipient, subject, content, key)
            except:
                print('Invalid input!')
                pass
    #The decorator is used to get the user inputs

    def main(self):

        """Check the user option to send or search the message by letting them choose the key.

        If they key is 1, the user is authenticated, message is created and sent to the recipient 
        (This uses authorization,create_message and send_message modules)

        If they key is 2, the query to be searched is received from the user,the user is authenticated,
        and the message content is displayed to the user.
        (This uses authorization, list_matching_messages and get_msg modules)
        
        """
        if(self.key == '1'): 
            while 1:        
                try:
                    self.file = input("Please enter the file location:\n")
                    self.service = authorization(self.SCOPES)
                    self.message = create_message(self.sender, self.recipient, self.subject, self.content, self.file)
                    send_message(self.service, self.user_id, self.message)
                    break 
                except:
                    print('File not found! Please enter the correct location')    
                    
        elif(self.key == '2'):
            self.query = input("Please enter the query you would like to search: \n")            
            self.service = authorization(self.SCOPES)
            list_matching_messages(self.service, self.user_id, self.query)
            
        else:            
            print("Wrong input! Try again by choosing either 1 or 2")
            
if __name__=="__main__":
    user = Info.get_user_input()
    user.main()

    
    