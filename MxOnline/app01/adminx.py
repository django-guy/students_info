#coding=utf-8

__author__ = 'Huang Yuan Yuan'
__date__ = '2019/8/9 22:06'


# ------------------- 全局设置 ---------------------------------
import  xadmin

#   下面是添加主题功能，这样就能在界面上有主题功能设置的选项了
from xadmin import views  # 导入views模块
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册到xadmin中

# 后台系统名称页脚设置、设置后台菜单为收缩样式
class GlobalSetting(object):
    site_title = u'Admin'
    site_footer = u'Student Management Info'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSetting) # 注册到xadmin中

# --------------------全局设置 结束------------------------------------

class StudentAdmin(object):
    # 自定义在后台显示哪些字段
    list_display=('name','gender','banji','get_banji_name','desc','birthday')
    # 设置排序
    ordering = ['-nid']
    # 设置搜索字段，是like 匹配
    search_fields=['name','desc']
    # 筛选字段
    list_filter= ('name','desc','birthday')
    # 列表页直接可修改字段
    list_editable=('name','gender','desc')
    # 指定编辑页面不显示的字段
    exclude = ['nid']
    # 设置列表页面时间
    refresh_times = [60,120]


# 注册表到xadmin
from  app01 import models
# Register your models here.
xadmin.site.register(models.Student,StudentAdmin)


# 使用装饰器来注册
# -----------------------------------------
# 获取指定类中的所有的属性名, 剔除所有以_下划线开头的，剔作所有函数，剔除指定的属性
def getmyattr(classnmae):
    return  [ i  for i in  dir(classnmae)
              if  not i.startswith('_')
              and not  callable(getattr(classnmae,i))
              and i not in ('objects','pk','nid','genders','grades','class1s','classinfo','banji_id','student_set')
            ]
# print(getmyattr(models.BanJi))

# 课程
@xadmin.sites.register(models.Course)
class CourseAdmin(object):
    list_display = ['name',]
#班级
@xadmin.sites.register(models.BanJi)
class BanJiAdmin(object):
    list_display = ['name',]

# 教师
@xadmin.sites.register(models.Teacher)
class TeacherAdmin(object):
    list_display = ['name','gender','classes','introduce','desc']
    # 列表页直接可修改字段
    list_editable=('introduce','desc')

# 班级信息
@xadmin.sites.register(models.ClassInfo)
class ClassInfoAdmin(object):
    list_display = ['banji','get_banji_name','banzhuren','count','xuexiwy','shenghuowy','tiyuwy','wenyiwy','desc']


