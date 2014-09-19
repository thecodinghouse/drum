
from django.conf import settings
from django.forms.models import modelform_factory
from django.forms import ValidationError

from drum.links.models import Link


BaseLinkForm = modelform_factory(Link, fields=["title", "content", "description"])


class LinkForm(BaseLinkForm):

    def clean(self):
        
        description = self.cleaned_data.get("description", None)
        if not description:
            raise ValidationError("Either a link or description is required")
        return self.cleaned_data
