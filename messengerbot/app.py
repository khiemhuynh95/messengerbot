from messengerbot import MessengerClient, messages, attachments, templates, elements

# Manually initialize client
messenger = MessengerClient(access_token='EAAIOULJXEmwBAPmhNKdXifnudPQZC5YYJVI45wMIVqdBiC9Y4OvZBwCyOeR0jYnJVQIytQNxn7nDuS3OQCyRhDVbzAkbVNMEhUWXoSd2jQfODiAzUEvin1trQ0TEPBeFBZBqa9cDrID259tg2AHtoYZBPJjES2dZBrdUgZAqN6lwZDZD')

# With env var export MESSENGER_PLATFORM_ACCESS_TOKEN=your_token
from messengerbot import messenger
@app.route('/', methods=['POST'])
recipient = messages.Recipient(recipient_id='100003143410968')

# Send text message
message = messages.Message(text='Hello World')
request = messages.MessageRequest(recipient, message)
messenger.send(request)

# Send button template
web_button = elements.WebUrlButton(
   title='Show website',
   url='https://petersapparel.parseapp.com'
)
postback_button = elements.PostbackButton(
   title='Start chatting',
   payload='USER_DEFINED_PAYLOAD'
)
template = templates.ButtonTemplate(
   text='What do you want to do next?',
   buttons=[
       web_button, postback_button
   ]
)
attachment = attachments.TemplateAttachment(template=template)

message = messages.Message(attachment=attachment)
request = messages.MessageRequest(recipient, message)
messenger.send(request)