
#!/usr/bin/python
# -*- coding: utf-8 -*-
from messengerbot import MessengerClient, messages, attachments, templates, elements

import os
import sys
import json
import time
import requests
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must
    # return the 'hub.challenge' value in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

# With env var export MESSENGER_PLATFORM_ACCESS_TOKEN=your_token
from messengerbot import messenger
@app.route('/', methods=['POST'])
def webook():
	# Manually initialize client
	messenger = MessengerClient(access_token='EAAOfYt7dcGsBALJFcp2ZBHyZAde6Tlfyt7Gr2GPfRzYm35yTH2ZAGqLZBqct7gzRFcSphQMNPMUSa4aPzYYnVGDwiVetRBjpY2wfbXvVbuvDXc81YK8BZCH0ZApvolfGsj7kkoY5eIkAHKgufFt46or5gNOI7Yn0kICNdKQbHSIQZDZD')

	recipient = messages.Recipient(recipient_id='1140257512682784')

	# Send text message
	message = messages.Message(text='Hello World hahaha')
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
	return "ok", 200
