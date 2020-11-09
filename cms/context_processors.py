from .models import NewsPost, Project, Advertisement, ContentManagement, Project, Popup
from django.db.models import Sum


def common(request):
    project = None
    if ContentManagement.objects.first() is not None:
        featured_project = ContentManagement.objects.first().featured_project
        project = Project.objects.annotate(sum=Sum('projectdonation__amount')).get(id=featured_project.id)

    kwargs = {
        'context_news': NewsPost.objects.all()[:3],
        'context_projects': Project.objects.all(),
        'context_ad': Advertisement.objects.order_by("?").first(),
        'context_content': ContentManagement.objects.first(),
        'featured_project': project,
        'context_popups': Popup.objects.all(),
    }
    return kwargs