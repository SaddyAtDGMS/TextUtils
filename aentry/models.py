from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class AentryAccDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    minename = models.CharField(max_length=100)
    acc_date = models.DateTimeField()
    killed = models.IntegerField()
    injured = models.IntegerField()
    coscode = models.CharField(max_length=4)
    minecode = models.ForeignKey('AentryMineDetails', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aentry_acc_detail'


class AentryMineDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    minecode = models.CharField(max_length=12)
    minename = models.CharField(max_length=100)
    ownercode = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'aentry_mine_details'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Codelib(models.Model):
    code = models.TextField(db_column='CODE', blank=True, null=False, )  # Field name made lowercase.
    longname = models.TextField(db_column='LONGNAME', blank=True, null=True)  # Field name made lowercase.
    codetype = models.TextField(db_column='CODETYPE', blank=True, null=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='SHORTNAME', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codelib'





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'








# class mine_details(models.Model) :
#     minecode = models.CharField(max_length=12)
#     minename = models.CharField(max_length=100)
#     ownercode = models.CharField(max_length=5)

#     def __str__(self):
#         return self.name

# class acc_detail(models.Model) :
#     minecode = models.ForeignKey(mine_details, on_delete=models.CASCADE)
#     minename = models.CharField(max_length=100)
#     acc_date = models.DateTimeField("Accident Date")
#     killed = models.IntegerField(default=0)
#     injured = models.IntegerField(default=0)
#     coscode = models.CharField(max_length=4)

    # def __str__(self):
    #     return self.name


