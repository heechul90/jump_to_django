from django.shortcuts import render, get_object_or_404

def kmps(request):

    context = {'kmas_list': 'list'}

    return render(request, 'kmas/kmas_list.html', context)