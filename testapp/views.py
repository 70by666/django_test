from django.shortcuts import render


def testapp(request):
    return render(request, 'testapp/index.html')
