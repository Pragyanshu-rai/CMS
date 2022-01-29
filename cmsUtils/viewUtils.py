from django.contrib.auth.models import User


def get_user_ip(request) -> str:
    """
        Given the request object this function will return
        the IP address of the user machine. \n
        NOTE: implementation reference - 'https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django'
    """

    forwarded_for: list = request.META.get('HTTP_X_FORWARDED_FOR')
    ip: str

    try:
        # if forwarded_for is not empty
        if forwarded_for:
            # get the last ip address from the list and trim the extra space
            ip = forwarded_for.split(',')[-1].strip()

        else:
            ip = request.META.get('REMOTE_ADDR')

    except Exception as error:
        print("[SERVER ERROR] IP ERROR - ", error)
        ip = None

    return ip


def validate_email_and_get_user(request, email: str = None) -> User:
    """
        Given the request object and the email* this function will validate if the user exists
        and fetch the user if the user exists and is not in the request object. \n
        NOTE: * - optional arguments 
    """
    if request.user.id is None:
        request.user = User.objects.get(email=email)
        print("user - ", request.user)

        if request.user is None:
            return Exception

    else:

        if email is not None and request.user.email != email:
            return Exception

    return request.user