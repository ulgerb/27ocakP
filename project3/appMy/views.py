from django.shortcuts import render

# Create your views here.
# adress çubuğuna girilen url buradaki fonksiyonu tetikler ve çalıştırır.
# burada yazıcağımız fonksionlar sayfamızı render eder ve sayfaya hem bilgi gönderir hemde sayfadan bilgi alır

def index(request):
    
    return render(request,'index.html')
