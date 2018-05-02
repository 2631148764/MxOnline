# -*- coding: utf-8 -*-
from .models import CityDict, CourseOrg, Teacher
import xadmin



class CityDictAdmin(object):
    # 定义要显示那些字段
    list_display = ['name', 'desc', 'add_time']
    # 定义搜索字段
    search_fields = ['name', 'desc']
    # 定义筛选字段
    list_filter = ['name', 'desc', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)



class CourseOrgAdmin(object):
    # 定义要显示那些字段
    list_display = ['name', 'desc', 'fav_nums', 'click_num','image','address','city','add_time']
    # 定义搜索字段
    search_fields = ['name', 'desc', 'fav_nums', 'click_num','image','address','city']
    # 定义筛选字段
    list_filter = ['name', 'desc', 'fav_nums', 'click_num','image','address','city','add_time']



xadmin.site.register(CourseOrg, CourseOrgAdmin)



class TeacherAdmin(object):
    # 定义要显示那些字段
    list_display = ['org', 'name', 'work_years', 'work_company','work_position','points','click_num','fav_nums','add_time']
    # 定义搜索字段
    search_fields = ['org', 'name', 'work_years', 'work_company','work_position','points','click_num','fav_nums']
    # 定义筛选字段
    list_filter = ['org', 'name', 'work_years', 'work_company','work_position','points','click_num','fav_nums','add_time']


xadmin.site.register(Teacher, TeacherAdmin)
