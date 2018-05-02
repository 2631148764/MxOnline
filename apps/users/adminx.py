# -*- coding: utf-8 -*-
from .models import EmailVerifyRecord, Banner
import xadmin



class EmailVerifyRecordAdmin(object):
    # 定义要显示那些字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 定义搜索字段
    search_fields = ['code', 'email']
    # 定义筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)



class BannerAdmin(object):
    # 定义要显示那些字段
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 定义搜索字段
    search_fields = ['title', 'image', 'url', 'index']
    # 定义筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



xadmin.site.register(Banner, BannerAdmin)
