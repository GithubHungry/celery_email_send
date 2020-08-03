from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .tasks import send_spam_email


# Create your views here.


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)  # Нежелательно передавать объекты
        return super().form_valid(form)
