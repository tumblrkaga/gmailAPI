from googleapiclient import discovery, errors

def send_message(service, user_id, message):
    """Send an email message.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

    Returns:
        Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                .execute())
        print('Your message with Message Id: %s has been sent successfuly' % message['id'] )
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)