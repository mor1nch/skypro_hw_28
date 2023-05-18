from django.http import JsonResponse
from django.views import View


class StartView(View):
    def get(self, request):
        response = {"status": "ok"}

        return JsonResponse(response, status=200)
