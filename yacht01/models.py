from django.db import models
from django.core.validators import FileExtensionValidator
from validate_email import validate_email
from django.core.exceptions import ValidationError


# Create your models here.
def check_email_address_validity(email_address):
    """
    Given a string, determine if it is a valid email address using
    Django's validate_email() function.
    """

    try:
        validate_email(email_address)
        valid_email = True

    except ValidationError:
        valid_email = False

    return valid_email


class Contact(models.Model):
    '''
    Contact form model
    '''
    name = models.CharField(
        'name', max_length=50,
        help_text='Введите Ваше имя'
        )
    user_email = models.EmailField(
        'Email', max_length=70,
        blank=False, help_text='Ваш Email',
        validators=[check_email_address_validity, ]
        )
    subject = models.CharField(
        'Subject', max_length=250,
        help_text='Тема сообщения'
        )
    message = models.TextField(
        'Message', max_length=1000,
        help_text='Введите текст сообщения до 1000 символов'
        )
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.date, self.name, self.user_email)

    class Meta:
        ordering = ['date']


class Portfolio(models.Model):
    '''
    images and video in portfolio section
    '''
    description = models.CharField(
        'Description', max_length=255, help_text='Мета описание',
        )
    alt = models.CharField('Alt', max_length=255, help_text='alt text')
    order = models.IntegerField('order', unique=True, )
    image = models.ImageField(upload_to='portfolio/', blank=True,)
    video = models.FileField(
        upload_to='videos/', null=True, blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', ]
            )]
        )
    show = models.BooleanField(default=False,)

    def clean(self):
        """
        Ensure that only one of image and video can be set.
        """
        if self.image and self.video:
            raise ValidationError("Можно загрузить только видео или фото")
        elif not self.image and not self.video:
            raise ValidationError("Необходимо добавить фото или видео")

    def __str__(self):
        return '%s, %s, %s, %s' % (
            self.order, self.description, self.image, self.show
            )

    class Meta:
        ordering = ['order']
