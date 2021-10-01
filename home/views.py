from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def downloads(request):
    return render(request,'downloads.html')

def holidays(request):
    return render(request,'holidays.html')

def contact(request):
    return render(request,'contact.html')

def map(request):
    return render(request,'map.html')

def related_links(request):
    return render(request,'related_links.html')

def about(request):
    return render(request,'about.html')

def iec(request):
    return render(request,'iec.html')

def fee(request):
    return render(request,'fee.html')

def check_list(request):
    return render(request,'check_list.html')


def aayat_niryaat(request):
    return render(request,'aayat_niryaat.html')

def status_holders(request):
    return render(request,'status_holders.html')

def application_status(request):
    return render(request,'application_status.html')

def what_is_new(request):
    return render(request,'what_is_new.html')

def tenders(request):
    return render(request,'tenders.html')

def trade_notices(request):
    return render(request,'trade_notices.html')

def eodc(request):
    return render(request,'eodc.html')

def epcg_authorisations(request):
    return render(request,'epcg_authorisations.html')

def performance(request):
    return render(request,'performance.html')

def major_export(request):
    return render(request,'major_export.html')

def commodity_board(request):
    return render(request,'commodity_board.html')

def photo_gallery(request):
    return render(request,'photo_gallery.html')

def feedback(request):
    return render(request,'feedback.html')

def faq(request):
    return render(request,'faq.html')
