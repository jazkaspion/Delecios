from django.shortcuts import render


def sug_list(requests):
    return render(requests, 'dashboard/suggetion/list.html', {})




