def messages(request):
    request.session.modified = True
    messages = {}
    if 'donate_message' in request.session:
        message_type = request.session.get('message_type', 'danger')
        messages = {'message': request.session['donate_message'],
                    'message_type': message_type}
        del request.session['donate_message']
        if 'message_type' in request.session:
            del request.session['message_type']
    return messages