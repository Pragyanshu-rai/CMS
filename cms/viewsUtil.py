
# to check if the session is not expired then modify the session
def modifySession(request):

    if 'user' not in request.session:

        return render(request, 'cms/session_expired.html')
    
    request.session.modified = True

    return request