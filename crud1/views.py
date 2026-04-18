# example view for testing

from django.http import JsonResponse


def get_user(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "success"
        }, status=200)

    return JsonResponse({
        "error": "invalid method"
    }, status=405)