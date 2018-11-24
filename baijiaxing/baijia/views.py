from django.shortcuts import render
from django.http import JsonResponse

from baijia.models import Baijiaxing


def index(request):
    if request.method == 'GET':
        all_name = Baijiaxing.objects.all()
        names = []
        i = 0
        for item in all_name:
            nums = i
            name = item.name
            # name_url = item.name_url
            print(nums)
            n = (name, nums)
            names.append(n)
            i += 1
            if i == 10:
                i = 1
        return render(request, 'index.html', {'names': names})
