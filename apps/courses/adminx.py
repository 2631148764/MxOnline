# -*- coding: utf-8 -*-
from .models import Course, Lesson, Video, CourseResource
import xadmin
from xadmin import views


class BaseSetting(object):
    # 开启主题
    enable_themes = True
    # 开启更多主题
    use_bootswatch = True

class GlobalSettings(object):
    # 表头
    site_title = '慕学后台管理系统'
    # 也脚
    site_footer = '慕学在线网'
    # 默认收起所有app
    menu_style = 'accordion'

class CourseAdmin(object):
    # 定义要显示那些字段
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # 定义搜索字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    # 定义筛选字段
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']



class LessonAdmin(object):
    # 定义要显示那些字段
    list_display = ['course', 'name', 'add_time']
    # 定义搜索字段
    search_fields = ['course', 'name']
    # 定义筛选字段
    list_filter = ['course__name', 'name', 'add_time']



class VideoAdmin(object):
    # 定义要显示那些字段
    list_display = ['lesson', 'name', 'add_time']
    # 定义搜索字段
    search_fields = ['lesson', 'name']
    # 定义筛选字段
    list_filter = ['lesson', 'name', 'add_time']



class CourseResourceAdmin(object):
    # 定义要显示那些字段
    list_display = ['course', 'name', 'dowload', 'add_time']
    # 定义搜索字段
    search_fields = ['course', 'name', 'dowload']
    # 定义筛选字段
    list_filter = ['course', 'name', 'dowload', 'add_time']



xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)