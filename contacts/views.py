from .forms import ContactForm
from django.views.generic import FormView
from django.contrib import messages


class ContactView(FormView):
    template_name = 'contacts/contacts.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        messages.success(self.request, 'Заявка успешно отправлена!')
        return super().form_valid(form)
