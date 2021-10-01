from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('downloads/',views.downloads,name="downloads"),
    path('holidays/',views.holidays,name="holidays"),
    path('contact/',views.contact,name="contact"),
    path('map/',views.map,name="map"),
    path('related_links/',views.related_links,name="related_links"),
    path('about/',views.about,name="about"),
    path('iec/',views.iec,name="iec"),
    path('fee/',views.fee,name="fee"),
    path('check_list/',views.check_list,name="check_list"),
    path('aayat_niryaat/',views.aayat_niryaat,name="aayat_niryaat"),
    path('status_holders/',views.status_holders,name="status_holders"),
    path('tenders/',views.tenders,name="tenders"),
    path('trade_notices/',views.trade_notices,name="trade_notices"),
    path('application_status/',views.application_status,name="application_status"),
    path('what_is_new/',views.what_is_new,name="what_is_new"),

    path('trade_notices/',views.trade_notices,name="trade_notices"),
    path('eodc/',views.eodc,name="eodc"),
    path('epcg_authorisations/',views.epcg_authorisations,name="epcg_authorisations"),
    path('performance/',views.performance,name="performance"),
    path('major_export/',views.major_export,name="major_export"),
    path('commodity_board/',views.commodity_board,name="commodity_board"),
    path('photo_gallery/',views.photo_gallery,name="photo_gallery"),
    path('feedback/',views.feedback,name="feedback"),
    path('faq/',views.faq,name="faq")
]