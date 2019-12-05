from dal import autocomplete

from backendapp.travels.models import City, InfoTravel

class TCAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = InfoTravel.objects.all()

        if self.q:
            qs = qs.filter(companyko__contains=self.q)

        return qs
