# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Minemast(models.Model):
    mineid = models.AutoField(db_column='MineId', primary_key=True)  # Field name made lowercase.
    minecode = models.IntegerField(db_column='MINECODE')  # Field name made lowercase.
    mine = models.CharField(db_column='MINE', max_length=100)  # Field name made lowercase.
    minetype = models.CharField(db_column='Minetype', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mnlcode = models.CharField(db_column='Mnlcode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mineral = models.CharField(db_column='MINERAL', max_length=45)  # Field name made lowercase.
    mineraltype = models.CharField(db_column='MineralType', max_length=10)  # Field name made lowercase.
    lin = models.CharField(db_column='LIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=40)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=50)  # Field name made lowercase.
    pincode = models.CharField(db_column='PINCODE', max_length=8)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=30)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=40)  # Field name made lowercase.
    subregion = models.CharField(db_column='SUBREGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    owncode = models.CharField(db_column='Owncode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ownsort = models.CharField(db_column='OWNSORT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(max_length=80)
    opendate = models.CharField(db_column='OPENDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateofentry = models.CharField(db_column='DateOfEntry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    entrysource = models.CharField(db_column='EntrySource', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=1, blank=True, null=True)  # Field name made lowercase.
    verifiedby = models.CharField(db_column='VerifiedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    verify_date = models.CharField(db_column='Verify_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'minemast'



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
    code = models.TextField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    longname = models.TextField(db_column='LONGNAME', blank=True, null=True)  # Field name made lowercase.
    codetype = models.TextField(db_column='CODETYPE', blank=True, null=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='SHORTNAME', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codelib'


class Coscode(models.Model):
    coscode = models.CharField(db_column='COSCODE', primary_key=True, max_length=4)  # Field name made lowercase.
    longname = models.CharField(db_column='LONGNAME', unique=True, max_length=60)  # Field name made lowercase.
    coshead = models.CharField(db_column='COSHEAD', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coscode'


class Distcode(models.Model):
    distcode = models.CharField(db_column='DISTCODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=100, blank=True, null=True)
    dateofentry = models.DateTimeField(db_column='DateOfEntry', blank=True, null=True)  # Field name made lowercase.
    enteredby = models.CharField(db_column='EnteredBy', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distcode'


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


class Logs(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    time = models.CharField(max_length=45, blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    message = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'





# 


class Mnlcode(models.Model):
    mnlcode = models.CharField(db_column='MNLCODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mnlname = models.CharField(db_column='MNLNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mnltype = models.CharField(db_column='MNLTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mnlcode'


class Ownmast(models.Model):
    owncode = models.CharField(db_column='OWNCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ownname = models.CharField(db_column='OWNNAME', max_length=75, blank=True, null=True)  # Field name made lowercase.
    own_short = models.CharField(db_column='OWN_SHORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desig = models.CharField(db_column='DESIG', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mnltype = models.CharField(db_column='MNLTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=70, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='PINCODE', blank=True, null=True)  # Field name made lowercase.
    ho_tel = models.CharField(db_column='HO_Tel', max_length=150, blank=True, null=True)  # Field name made lowercase.
    owner_tel = models.CharField(db_column='Owner_Tel', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sector = models.TextField(db_column='SECTOR', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ownmast'


class Pincode(models.Model):
    pincode = models.IntegerField(db_column='Pincode')  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=45)  # Field name made lowercase.
    officetype = models.CharField(db_column='OfficeType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=55)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    circlename = models.CharField(db_column='CircleName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pincode'


class Rgncode(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    codetype = models.CharField(max_length=3)
    active = models.CharField(db_column='ACTIVE', max_length=1)  # Field name made lowercase.
    subregion = models.CharField(db_column='SUBREGION', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=50)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=50)  # Field name made lowercase.
    add1 = models.CharField(db_column='ADD1', max_length=80)  # Field name made lowercase.
    add2 = models.CharField(db_column='ADD2', max_length=80)  # Field name made lowercase.
    remarks = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rgncode'


class Rgncode2(models.Model):
    rgncode = models.CharField(db_column='RGNCODE', primary_key=True, max_length=3)  # Field name made lowercase.
    rgnname = models.CharField(db_column='RGNNAME', max_length=45)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1)  # Field name made lowercase.
    add1 = models.CharField(db_column='ADD1', max_length=150)  # Field name made lowercase.
    add2 = models.CharField(db_column='ADD2', max_length=150)  # Field name made lowercase.
    zonecode = models.CharField(db_column='ZONECODE', max_length=3)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rgncode2'


class Srgncode(models.Model):
    srgncode = models.CharField(db_column='SRGNCODE', primary_key=True, max_length=3)  # Field name made lowercase.
    srgnname = models.CharField(db_column='SRGNNAME', max_length=40)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1)  # Field name made lowercase.
    rgncode = models.CharField(db_column='RGNCODE', max_length=3)  # Field name made lowercase.
    zonecode = models.CharField(db_column='ZONECODE', max_length=3)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'srgncode'


class State2(models.Model):
    statecode = models.CharField(primary_key=True, max_length=2)
    statename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'state2'


class States(models.Model):
    statecode = models.TextField(db_column='Statecode', blank=True, null=True)  # Field name made lowercase.
    statename = models.TextField(db_column='StateName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'states'


class TestDtl(models.Model):
    idtest_dtl = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    age = models.CharField(max_length=2)
    dob = models.DateTimeField()
    state = models.TextField()
    coscode = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'test_dtl'


class Users(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    desig = models.CharField(max_length=45)
    workassigned = models.CharField(max_length=45)
    workcode = models.CharField(max_length=5)
    role = models.CharField(max_length=5)
    entered_by = models.CharField(max_length=45)
    entry_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Zonecode(models.Model):
    zonecode = models.CharField(db_column='ZONECODE', primary_key=True, max_length=3)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZONENAME', max_length=45)  # Field name made lowercase.
    add1 = models.CharField(db_column='ADD1', max_length=100)  # Field name made lowercase.
    add2 = models.CharField(db_column='ADD2', max_length=100)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zonecode'
