# -*- coding: utf-8 -*-

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
import xadmin



class UserAskAdmin(object):
    # 定义要显示那些字段
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 定义搜索字段
    search_fields = ['name', 'mobile', 'course_name']
    # 定义筛选字段
    list_filter = ['name', 'mobile', 'course_name', 'add_time']



xadmin.site.register(UserAsk, UserAskAdmin)



class CourseCommentsAdmin(object):
    # 定义要显示那些字段
    list_display = ['user','course','comments','add_time']
    # 定义搜索字段
    search_fields = ['user','course','comments']
    # 定义筛选字段
    list_filter = ['user','course','comments','add_time']



xadmin.site.register(CourseComments, CourseCommentsAdmin)



class UserFavoriteAdmin(object):
    # 定义要显示那些字段
    list_display = ['user','fav_id','fav_type','add_time']
    # 定义搜索字段
    search_fields = ['user','fav_id','fav_type']
    # 定义筛选字段
    list_filter = ['user','fav_id','fav_type','add_time']



xadmin.site.register(UserFavorite, UserFavoriteAdmin)



class UserMessageAdmin(object):
    # 定义要显示那些字段
    list_display = ['user','message','has_read','add_time']
    # 定义搜索字段
    search_fields = ['user','message','has_read']
    # 定义筛选字段
    list_filter = ['user','message','has_read','add_time']



xadmin.site.register(UserMessage, UserMessageAdmin)



class UserCourseAdmin(object):
    # 定义要显示那些字段
    list_display = ['user','course','add_time']
    # 定义搜索字段
    search_fields = ['user','course']
    # 定义筛选字段
    list_filter = ['user','course','add_time']



xadmin.site.register(UserCourse, UserCourseAdmin)
