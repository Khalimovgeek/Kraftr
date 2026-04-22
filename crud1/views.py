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

def post_user(request):
    if request.method == "POST":
        return JsonResponse({
            "message": "success"
        }, status=200)

    return JsonResponse({
        "error": "invalid method"
    }, status=405)

def user(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "success"
        }, status=200)

    return JsonResponse({
        "error": "invalid method"
    }, status=405)

def user1(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "success"
        }, status=200)

    return JsonResponse({
        "error": "invalid method"
    }, status=405)


def api_final_test(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "success"
        }, status=200)

    return JsonResponse({
        "error": "invalid method"
    }, status=405)