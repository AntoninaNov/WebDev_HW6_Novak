def set_cookie(response, key, value, http_only=False):
    """
    Sets a cookie on the response object.
    Args:
    - response: HttpResponse object
    - key: Cookie name
    - value: Cookie value
    - http_only: Boolean indicating if the cookie is HTTP only
    """
    response.set_cookie(key, value, httponly=http_only)

def get_cookie(request, key):
    """
    Retrieves a cookie value by its key from the request object.
    Args:
    - request: HttpRequest object
    - key: Cookie name
    Returns:
    - The cookie value or None if not found
    """
    return request.COOKIES.get(key)