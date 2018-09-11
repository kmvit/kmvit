from .models import StaticInfo

def static_info_processor(request):
    if StaticInfo.objects.first():
        obj = StaticInfo.objects.first()
        phone = obj.phone
        phone_mobile = obj.phone_mobile
        address = obj.address
        site_title = obj.site_title
        logo = obj.logo
        email = obj.email
        footer_company_info = obj.footer_company_info
        return {'phone': phone,
            'phone_mobile': phone_mobile,
            'site_title':site_title,
            'address': address,
            'site_title':site_title,
            'logo':logo,
            'email':email,
            'footer_company_info': footer_company_info,
            }
