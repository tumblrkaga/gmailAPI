from googleapiclient import discovery, errors

def get_message(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    print('Message snippet: %s' % message['snippet'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)