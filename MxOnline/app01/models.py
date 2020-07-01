from django.db import models

# Create your models here.
# 学生
class Student(models.Model):
    genders=((1, u'男'), (2, '女'))

    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=512,null=False,verbose_name="名字")  # null默认就是False
    gender=models.IntegerField(choices=genders,verbose_name="性别")  # null默认就是False
    banji=models.ForeignKey(to='BanJi',to_field='nid',verbose_name="所属班级")
    # null=True 表示数据库可为空 ,blank=True表示填写表单时可为空
    birthday=models.DateField(blank=True,null=True,verbose_name="出生日期")
    desc=models.CharField(max_length=1024,default='默认描述。。。',verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="插入时间")

    class Meta: # 用于在XADMIN中显示表名
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    # 重载__str__方法
    def __str__(self):
        return "学生 {0}".format(self.name)

    # 获取班级名称,xadmin样式类中，显示列表中写可以这个函数名，
    def get_banji_name(self):
        return self.banji.name
    get_banji_name.short_description='班级名'

    # 重载save_models 方法
    def save_models(self):
        print('000000000000000000')
        obj=self.new_obj
        obj.save()

        if obj.banji is not None:
            print('11111111111')
            obj.banji.count=Student.objects.filter(banji=obj.banji).count()
            obj.banji.save()


# 班级
class BanJi(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=125,verbose_name="班级")  # null默认就是False
    class Meta: # 用于在XADMIN中显示表名
        verbose_name = "班级"
        verbose_name_plural = verbose_name

    # 重载__str__方法
    def __str__(self):
        return "{0}".format(self.name)

# 课程
class Course(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=512,verbose_name="课程名")  # null默认就是False

    class Meta: # 用于在XADMIN中显示表名
        verbose_name = "课程"
        verbose_name_plural = verbose_name
    # 重载__str__方法
    def __str__(self):
        return '{0}'.format(self.name)

# 教师
class Teacher(models.Model):
    genders=((1, u'男'), (2, '女'))

    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=512,null=False,verbose_name="名字")  # null默认就是False
    gender=models.IntegerField(choices=genders,verbose_name="性别")  # null默认就是False
    # null=True 表示数据库可为空 ,blank=True表示填写表单时可为空
    birthday=models.DateField(blank=True,null=True,verbose_name="出生日期")
    introduce = models.CharField(max_length=2560, blank=True, null=True, verbose_name="教师介绍")
    classes=models.ManyToManyField(to='Course' ,blank=True,verbose_name="所教课程")
    desc=models.CharField(max_length=1024,blank=True,null=True,verbose_name="备注")
    in_time = models.DateField(blank=True,null=True,verbose_name="入职日期")
    out_time = models.DateField(blank=True, null=True, verbose_name="离职日期")

    class Meta: # 用于在XADMIN中显示表名
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    # 重载__str__方法
    def __str__(self):
        return "教师 {0}".format(self.name)

# 班级信息
class  ClassInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    # 班级
    banji=models.OneToOneField(to="BanJi",to_field="nid",verbose_name="班级")
    # 班主任
    banzhuren = models.ForeignKey(to='Teacher',to_field='nid',blank=True,null=True,verbose_name="班主任")
    # 班级人数
    count=models.IntegerField(verbose_name="班级人数")
    # 学习委员
    xuexiwy = models.CharField(max_length=123, blank=True, null=True, verbose_name="学习委员")
    # 生活委员
    shenghuowy = models.CharField(max_length=123, blank=True, null=True, verbose_name="生活委员")
    # 体育委员
    tiyuwy = models.CharField(max_length=123, blank=True, null=True, verbose_name="体育委员")
    # 文艺委员
    wenyiwy = models.CharField(max_length=123, blank=True, null=True, verbose_name="文艺委员")
    # 备注
    desc = models.CharField(max_length=1024,  blank=True, null=True, verbose_name="备注")

    class Meta: # 用于在XADMIN中显示表名
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法
    def __str__(self):
        return '班级信息 {0}'.format(self.banji)

    # 获取班级名称,xadmin样式类中，显示列表中写可以这个函数名，
    def get_banji_name(self):
        return self.banji.name
    get_banji_name.short_description='班级名'