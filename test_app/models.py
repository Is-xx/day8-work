from django.db import models


class Teacher(models.Model):
    gender_choices = (
        (0, '男'),
        (1, '女'),
    )

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)
    pic = models.ImageField(upload_to='pic/', default='pic/11.jpg')

    class Meta:
        db_table = 'drf_teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % ('教师对象', self.username)
