import json

from django.http import JsonResponse
from categories.models import Categories
from django.views import View


class DataView(View):
    def get(self, request):
        with open('datasets/categories.json') as file:
            data2 = json.load(file)

            for item in data2:
                categories = Categories(name=item['name'])
                categories.save()

        return JsonResponse({"status": "categories completed"}, status=200)
