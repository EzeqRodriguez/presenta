
from django.db import models

# class Tarjeta(models.Model):
#     customer_id = models.IntegerField(unique=True, blank=True, null=True)
#     numero_tarjeta = models.IntegerField(blank=True, null=True)
#     cvv = models.IntegerField(blank=True, null=True)
#     fecha_otorgamiento = models.IntegerField(blank=True, null=True)
#     fecha_expiracion = models.IntegerField(blank=True, null=True)
#     tipo_tarjeta = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'TARJETA'


# class AuditoriaCuenta(models.Model):
#     old_id = models.TextField(blank=True, null=True)  # This field type is a guess.
#     new_id = models.TextField(blank=True, null=True)  # This field type is a guess.
#     old_balance = models.TextField(blank=True, null=True)  # This field type is a guess.
#     new_balance = models.TextField(blank=True, null=True)  # This field type is a guess.
#     old_iban = models.TextField(blank=True, null=True)  # This field type is a guess.
#     new_iban = models.TextField(blank=True, null=True)  # This field type is a guess.
#     old_type = models.TextField(blank=True, null=True)  # This field type is a guess.
#     new_type = models.TextField(blank=True, null=True)  # This field type is a guess.
#     user_action = models.TextField(blank=True, null=True)  # This field type is a guess.
#     created_at = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'auditoria_cuenta'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class CaracteristicasClientes(models.Model):
#     customer_id = models.IntegerField(unique=True, blank=True, null=True)
#     tipo_cliente = models.IntegerField(blank=True, null=True)
#     tipo_cuenta = models.IntegerField(blank=True, null=True)
#     marca_tarjeta = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'caracteristicas_clientes'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField(blank=True, null=True)
    customer_surname = models.TextField(blank=True, null=True)  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


# class DireccionClientes(models.Model):
#     id_clientes = models.IntegerField(blank=True, null=True)
#     direccion = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'direccion_clientes'


# class DireccionEmpleados(models.Model):
#     id_empleado = models.IntegerField(blank=True, null=True)
#     direccion = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'direccion_empleados'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_flag = models.PositiveSmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Empleado(models.Model):
#     employee_id = models.IntegerField()
#     employee_name = models.TextField()
#     employee_surname = models.TextField()
#     employee_hire_date = models.TextField()
#     employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
#     branch_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'empleado'


# class Movimientos(models.Model):
#     id_movimiento = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
#     numero_cuenta = models.IntegerField(blank=True, null=True)
#     monto = models.IntegerField(blank=True, null=True)
#     tipo_operacion = models.TextField(blank=True, null=True)
#     hora = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'movimientos'


# class Prestamo(models.Model):
#     loan_id = models.IntegerField()
#     loan_type = models.TextField()
#     loan_date = models.TextField()
#     loan_total = models.IntegerField()
#     customer_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'prestamo'


# class Sucursal(models.Model):
#     branch_id = models.IntegerField()
#     branch_number = models.BinaryField()
#     branch_name = models.TextField()
#     branch_address_id = models.IntegerField()
#     direcciones = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sucursal'
