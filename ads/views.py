import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from ads.models import Ads


class StartView(View):
    def get(self, request):
        response = {"status": "ok"}

        return JsonResponse(response, status=200)


class AdsDataView(View):
    def get(self, request):
        with open('datasets/ads.json') as file:
            data1 = json.load(file)

            for item in data1:
                ads = Ads(name=item['name'], author=item['author'], price=item['price'],
                          description=item['description'], address=item['address'], is_published=item['is_published'])
                ads.save()

        return JsonResponse({"status": "ads completed"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []

        for ads_item in ads:
            response.append({
                "id": ads_item.id,
                "name": ads_item.name,
                "author": ads_item.author,
                "price": ads_item.price,
                "description": ads_item.description,
                "address": ads_item.address,
                "is_published": ads_item.is_published,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = Ads()

        ads.id = ads_data["id"]
        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["price"]
        ads.is_published = ads_data.get("is_published", False)

        try:
            ads.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        })


class AdsEntityView(View):
    def get(self, request, pk):
        ads = get_object_or_404(Ads, id=pk)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        })
