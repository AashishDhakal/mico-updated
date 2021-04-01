from django.db import models
from common.models import MicoModel
from cms.models import Project
import uuid


# Create your models here.
class Causes(MicoModel):
    thumbnail = models.ImageField(upload_to='causes')
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    goal = models.IntegerField()
    icon = models.ImageField(upload_to='icon',
                             default='icon/donateclassroom.png')

    def __str__(self):
        return self.title

    def get_short_text(self):
        return self.description[:100]


class ProjectDonation(MicoModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    donation_id = models.CharField(max_length=100, default='')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    amount = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True, blank=True)
    method = models.CharField(max_length=50, choices=(
        ('paypal', 'paypal'),
        ('card', 'card'),
        ('offline', 'offline'),
    ))
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CausesDonation(MicoModel):
    cause = models.ForeignKey(Causes, on_delete=models.PROTECT,
                              related_name='causedonation')
    donation_id = models.CharField(max_length=100, default='')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    amount = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True, blank=True)
    method = models.CharField(max_length=50, choices=(
        ('paypal', 'paypal'),
        ('card', 'card'),
        ('offline', 'offline'),
    ))
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Transaction(MicoModel):
    order_id = models.CharField(max_length=100)
    response_code = models.CharField(max_length=10)
    reason_code = models.CharField(max_length=10)
    reason_code_desc = models.CharField(max_length=500)
    currency = models.CharField(max_length=6, blank=True, null=True)
    reference_no = models.CharField(max_length=100)
    padded_card_no = models.CharField(max_length=100)
    auth_code = models.CharField(max_length=100)
    cvv2_result = models.CharField(max_length=100)
    original_response = models.CharField(max_length=20)
    signature = models.CharField(max_length=500)

    def __str__(self):
        return self.order_id
