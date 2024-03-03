from django.http import HttpResponse, JsonResponse
from .helpers.cookie_helper import set_cookie, get_cookie
from .helpers.header_helper import set_header, get_header


def set_cookie_view(request):
    key = request.GET.get('key')
    value = request.GET.get('value')
    response = HttpResponse("Cookie set successfully.")
    set_cookie(response, key, value, http_only=True)
    return response


def get_cookie_view(request, key):
    value = get_cookie(request, key)
    if value:
        return JsonResponse({'cookie': value})
    else:
        return JsonResponse({'error': 'Cookie not found'})


def set_header_view(request):
    key = request.GET.get('key')
    value = request.GET.get('value')
    response = HttpResponse("Header set successfully.")
    set_header(response, key, value)
    return response


def get_header_view(request, key):
    header_value = request.META.get(f'HTTP_{key.upper()}')
    if header_value:
        return JsonResponse({'header': header_value})
    else:
        return JsonResponse({'error': 'Header not found'}, status=404)
