from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import CausesDonation, ProjectDonation
from django.core.mail import send_mail
from django.template.loader import render_to_string


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        donation = None
        if ipn.custom == 'cause':
            donation = get_object_or_404(CausesDonation, uuid=ipn.invoice)
        elif ipn.custom == 'project':
            donation = get_object_or_404(ProjectDonation, uuid=ipn.invoice)
        if donation.amount == ipn.mc_gross:
            donation.status = 'Paid'
            donation.save()
            send_mail(
                subject="Mico Foundation Donation Receipt",
                from_email="info@themicofoundationja.com",
                recipient_list=[donation.email, ],
                message='Donation Receipt',
                html_message=render_to_string('donation_receipt.html', {
                    'donation': donation,
                }),
                fail_silently=True,
            )
