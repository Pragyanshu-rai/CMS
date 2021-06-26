# to check if the session is expired then logout the user
def checkSession(request):
    
    if "user" not in request.session:

        auth.logout(request)

    return False

# to check if the session is not expired then modify the session
def modifySession(request):

    if 'user' not in request.session:

        checkSession(request)
    
    else:

        request.session.modified = True

    return True