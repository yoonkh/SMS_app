from django.shortcuts import render, redirect
import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from .forms import SmsForm


def sms_send(request):
    if request.method == "POST":
        # set api key, api secret
        api_key = ""
        api_secret = ""

        params = dict()
        params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
        params['from'] = ''  # Sender number

        form = SmsForm(request.POST)

        if form.is_valid():
            params['to'] = form.cleaned_data['to']  # Recipients Number '01000000000,01000000001'
            params['text'] = form.cleaned_data['contents']  # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

        try:
            sys.exit()
        except SystemExit:
            return redirect('sms:sms_index')
    else:
        context = {
            'form': SmsForm()
        }
    return render(request, 'sms/sms_index.html', context)

