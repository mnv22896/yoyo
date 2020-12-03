
# -*- coding: utf-8 -*-

from models import Item
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'djecommerce.settings')
import django
django.setup()

def upload():
    q=Item.objects.get_or_create(discount_price=42112,title='hello',image='/img/shir.jpg',price=12)
    print ("in upload")
    
if __name__=='__main__':
    print("efore.uploa")
    upload()
    print("after upload")