from django.db import models
from common.models import MicoModel
from django.utils.translation import gettext_lazy as _
import html
from djsingleton.models import SingletonModel, SingletonActiveModel


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to='sliders')
    title_1 = models.CharField(max_length=50)
    title_2 = models.CharField(max_length=30, blank=True, null=True)
    short_desc = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title_1


class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'News Categories'


class NewsPost(MicoModel):
    category = models.ForeignKey(NewsCategory, null=True, blank=True,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='newsposts')
    time = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    date = models.DateField()
    keywords = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_short_text(self):
        return self.description[:100]


class Resource(MicoModel):
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)
    published_by = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=(
        ('Annual Reports', 'Annual Reports'),
    ))
    resource_file = models.FileField(upload_to='resources')
    description = models.TextField()
    access_level = models.CharField(choices=(
        ('Public', 'Public'),
        ('Directors Only', 'Directors Only'),
    ), max_length=30, default='Public')

    def __str__(self):
        return self.title


class Policy(MicoModel):
    class Meta:
        app_label = "cms"
        verbose_name = _('Policy')
        verbose_name_plural = _('Policies')

    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)

    Terms, Privacy, Refund = ('Terms', 'Privacy', 'Refund')
    type = models.CharField(choices=(
        (Terms, 'Terms of Use'),
        (Privacy, 'Privacy Policy'),
        (Refund, 'Refund Policy'),
    ), max_length=30, default=Terms)

    published = models.BooleanField("Publish", default=True)
    description = models.TextField()

    date_updated = models.DateField(_("Date Updated"), auto_now=True)
    date_created = models.DateField(_("Date Updated"), auto_now=True)

    def __str__(self):
        return self.title


# added subject field to the model
class Contact(MicoModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=500, default='address line 1')
    address_line_2 = models.CharField(max_length=500, default='address line 2')
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teams')
    designation = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Trustee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teams')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Message(models.Model):
    message_by = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='messages')
    message = models.TextField()

    def __str__(self):
        return self.message_by


class History(models.Model):
    image = models.ImageField(upload_to='history')
    name = models.CharField(max_length=50)
    is_director = models.BooleanField(default=False)
    is_chairman = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    start_year = models.BigIntegerField(default=1990)
    end_year = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Histories'


class Event(models.Model):
    thumbnail = models.ImageField(upload_to='events')
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    description = models.TextField()
    organized_by = models.CharField(max_length=200, default='Mico Foundation')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', ]

    def get_short_text(self):
        return self.description[:100]


class BOD(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teams')
    designation = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Work(models.Model):
    icon = models.ImageField(upload_to='works')
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    detail = models.TextField()

    def __str__(self):
        return self.title

    def get_short_text(self):
        return self.detail[:100]


class Project(models.Model):
    thumbnail = models.ImageField(upload_to='projects')
    project_name = models.CharField(max_length=200)
    slug = models.SlugField()
    detail = models.TextField()
    goal = models.IntegerField(default=0)
    icon = models.ImageField(upload_to='icon',
                             default='icon/donateclassroom.png')

    def __str__(self):
        return self.project_name


class MissionValue(models.Model):
    icon = models.ImageField(upload_to='mission')
    title = models.CharField(max_length=100)
    short_desc = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Endowment Types'
        verbose_name = 'Endowment Type'


class Advertisement(models.Model):
    image = models.ImageField(upload_to='ads')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Popup(models.Model):
    image = models.ImageField(upload_to='popup')
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    description = models.TextField()
    button_link = models.URLField(null=True, blank=True)
    button_text = models.CharField(max_length=100)
    short_desc_for_top = models.TextField(default='')

    def __str__(self):
        return self.title_1


class Gallery(models.Model):
    news = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='newsgallery')

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name_plural = 'Galleries'


class HomepageManagement(models.Model):
    chairman_name = models.CharField(max_length=200)
    chairman_message = models.TextField()
    chairman_photo = models.ImageField(upload_to='chairmanphoto')
    message_link = models.URLField()
    project_1 = models.ForeignKey(Project, on_delete=models.PROTECT,
                                  related_name='project1')
    project_2 = models.ForeignKey(Project, on_delete=models.PROTECT,
                                  related_name='project2')
    project_3 = models.ForeignKey(Project, on_delete=models.PROTECT,
                                  related_name='project3')

    def __str__(self):
        return "Click to edit homepage content"


class Endowment(models.Model):
    endowment_type = models.ForeignKey(FAQ, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ContentManagement(models.Model):
    history_description = models.TextField()
    mission_banner = models.ImageField(upload_to='missionbanner')
    sponsorship_who_we_are = models.TextField()
    sponsorship_banner = models.ImageField(upload_to='sponsorshipbanner',
                                           null=True, blank=True)
    sponsorship_banner_text = models.TextField(default='')
    sponsorship_become_sponsor_image = models.ImageField(
        upload_to='sponsorshipbanner', null=True, blank=True)
    sponsorship_become_sponsor_title = models.CharField(max_length=300,
                                                        default='')
    sponsorship_become_sponsor_text = models.TextField(default='')
    endowment_text = models.TextField(default='')
    featured_project = models.ForeignKey(Project, on_delete=models.PROTECT,
                                         null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    about_description = models.TextField(default='')
    donate_page_banner = models.ImageField(upload_to='doantebanner', null=True,
                                           blank=True)
    donate_step1_title = models.CharField(max_length=200, default='')
    donate_step1_text = models.TextField(default='')
    donate_step2_title = models.CharField(max_length=200, default='')
    donate_step2_text = models.TextField(default='')
    donate_step3_title = models.CharField(max_length=200, default='')
    donate_step3_text = models.TextField(default='')
    workwithus_banner = models.ImageField(upload_to='workwithusbanner',
                                          null=True, blank=True)
    workwithus_banner_title = models.CharField(max_length=300, default='')
    workwithus_banner_text_1 = models.TextField(default='')
    workwithus_banner_text_2 = models.TextField(default='')
    getinvolved_banner = models.ImageField(upload_to='getinvolvedbanner',
                                           null=True, blank=True)
    getinvolved_banner_title = models.CharField(max_length=500, default='')
    getinvolved_banner_text = models.TextField(default='')

    def __str__(self):
        return "Click here to edit"


# added subject field to the model
class WorkWithUs(MicoModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=500, default='address line 1')
    address_line_2 = models.CharField(max_length=500, default='address line 2')
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# added subject field to the model
class Sponsorship(MicoModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=500, default='address line 1')
    address_line_2 = models.CharField(max_length=500, default='address line 2')
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class GetInvolvedImage(models.Model):
    image = models.ImageField(upload_to='getinvolved')
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.caption
