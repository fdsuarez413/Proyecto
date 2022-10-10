from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from modulos.models import PQRS

class Mail:
    

    @staticmethod
    def send_complete_pqrs(user):
        subject = 'PQRS'
        template = get_template('mails/complete.html')
        
        content = template.render({
            'user': user
        })
        
        message = EmailMultiAlternatives(subject, 
                                         'Gracias por registrar su PQRS, muy pronto será contestada',
                                         settings.EMAIL_HOST_USER,
                                         [user.email])
        
        message.attach_alternative(content, 'text/html')
        message.send()