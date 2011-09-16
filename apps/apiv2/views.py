from djangorestframework.mixins import ListModelMixin, InstanceMixin, ReadModelMixin, RequestMixin
from djangorestframework.utils import as_tuple
from djangorestframework.views import ModelView, View
from apps.package.models import Package

LIST_LIMIT = 10

class PackageModelList(ModelView, RequestMixin):
    """A view which provides default operations for list and create, against a model in the database."""
    _suffix = 'List'
    queryset = Package.objects.all()[:LIST_LIMIT]
#
#    def get(self, request, *args, **kwargs):
#        print 'got kwargs', request.GET
#        return super(PackageModelList, self).get(request, *args, **request.GET)

    def get(self, request, *args, **kwargs):
        print 'listmodel params', self.PARAMS
        model = self.resource.model

        queryset = self.queryset if self.queryset else model.objects.all()

        if hasattr(self, 'resource'):
            ordering = getattr(self.resource, 'ordering', None)
        else:
            ordering = None

        if ordering:
            args = as_tuple(ordering)
            queryset = queryset.order_by(*args)
        return queryset.filter(**kwargs).filter(**self.PARAMS)

class ReadModelView(InstanceMixin, ReadModelMixin, ModelView):
    """A view which provides default operations for read/update/delete against a model instance."""
    _suffix = 'Instance'
