from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("Hello, AWS!")


def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "message": "server is running"
        },
        json_dumps_params={"ensure_ascii": False}
    )


def api_test(request):
    return JsonResponse(
        {
            "title": "AWS 배포 세미나",
            "message": "Django server response success!",
            "method": request.method
        },
        json_dumps_params={"ensure_ascii": False}
    )