def set_header(response, key, value):
    """
    Sets a header on the response object.
    Args:
    - response: HttpResponse object
    - key: Header name
    - value: Header value
    """
    response[key] = value

def get_header(request, key):
    """
    Retrieves a header value by its key from the request object.
    Args:
    - request: HttpRequest object
    - key: Header name
    Returns:
    - The header value or None if not found
    """
    # Django converts headers to uppercase, and replaces dashes with underscores
    header_key = 'HTTP_' + key.upper().replace('-', '_')
    return request.META.get(header_key)
