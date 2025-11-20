from django.shortcuts import render, redirect
from . models import QR_code

def index(request):
    context = {}
    if request.method == "POST":
        data = request.POST.get("lien")
        logo = request.FILES.get("logo")
        obj = QR_code.objects.create(data=data, logo=logo)
        
        return redirect(f"/?qr={obj.token}")

    token = request.GET.get("qr")
    if token:
        obj = QR_code.objects.filter(token=token).first()
        if obj:
            context["qr_code"] = obj.qr_code

    return render(request, 'Generator/index.html', context)
