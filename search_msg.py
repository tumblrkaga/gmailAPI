
from googleapiclient import discovery, errors

from get_msg import get_message

def list_matching_messages(service, user_id, query):
    """List all Messages of the user's mailbox matching the query.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        query: String used to filter messages returned.
        Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
        List of Messages that match the criteria of the query. Note that the
        returned list contains Message IDs and they are passed to the GetMessage funtion
        to get the details of a Message.
    """
    try:
        response = service.users().messages().list(userId=user_id,
                                                q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                                pageToken=page_token).execute()
            messages.extend(response['messages'])   
        if len(messages)>1:       
            print('The below list shows the body of the e-mail where the search query has been found \n')
            for i in range(len(messages)):
                get_message(service, user_id, messages[i]['id'])
        else:
            print("Sorry, No search result found!")
        return True
    except errors.HttpError as error:
        print('An error occurred: %s' % error)