from django.apps import AppConfig


class TestdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testdb'
    verbose_name = 'Операции'

# class OperationsConfig(AppConfig):
#     name = 'operations'
#     verbose_name = 'Operations'

#     def ready(self) -> None:
#         import operations.signals