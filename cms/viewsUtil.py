from django.shortcuts import redirect


# to check if the session is not expired then modify the session
def modifySession(request):

    if 'user' not in request.session:

        return False
    
    request.session.modified = True

    return request