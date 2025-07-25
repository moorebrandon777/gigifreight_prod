from django.contrib import messages
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.core.mail import send_mail


from shipment.models import Shipment, Package

class HomeView(TemplateView):
    template_name = 'frontend/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return HttpResponseRedirect(reverse_lazy('shipment:n_dashboard'))
            else:
                return HttpResponseRedirect(reverse_lazy('shipment:dashboard'))
        return super().dispatch(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'frontend/about.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return HttpResponseRedirect(reverse_lazy('shipment:n_dashboard'))
            else:
                return HttpResponseRedirect(reverse_lazy('shipment:dashboard'))
        return super().dispatch(request, *args, **kwargs)

class ContactView(TemplateView):
    template_name = 'frontend/contact.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return HttpResponseRedirect(reverse_lazy('shipment:n_dashboard'))
            else:
                return HttpResponseRedirect(reverse_lazy('shipment:dashboard'))
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            send_mail(
                'Message From '+name+' <'+email+'>',
                message,
                'delivery@gigifreight.org',
                ['delivery@gigifreight.org'],
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully, we will get back to you as soon as possible')
        except:
            messages.error(request, 'There was an error while trying to send your email, please try again')

        finally:
            return HttpResponseRedirect(reverse_lazy('frontend:contact'))


def TrackingView(request):
    if request.method == 'POST':
        tracking_code = request.POST.get('tracking_code')
        shipments = Shipment.objects.filter(tracking_number=tracking_code).union(Package.objects.filter(tracking_number=tracking_code) )
          
        
        if shipments.exists():
            return render(request, 'frontend/tracking.html', {'shipments':shipments}) 
        else:
            messages.error(request, "Invalid tracking code. Please check the code and try again. please make sure no spaces in between the letters")
            return redirect('frontend:home')
    return redirect('frontend:home')
    # return render(request, 'frontend/tracking.html') 