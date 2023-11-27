# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .models import Operation

# @receiver(post_save, sender=Operation)
# def send_operation_notification(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             'Новая операция',
#             f'Произведена новая операци #{instance.id}.',
#             'desert0613@mail.ru',
#             ['amkazennov99@gmail.com'],
#             fail_silently=False,
#         )