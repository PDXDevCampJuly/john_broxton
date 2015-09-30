from django.shortcuts import render

def javapic_query(request):
    return render(request, 'javapic_query.html')


def query_join(request):
    return render(request, 'query_join.html')


def query_gallery(request):
    return render(request, 'query_gallery.html')
