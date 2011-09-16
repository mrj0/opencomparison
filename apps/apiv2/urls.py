from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from django.conf.urls.defaults import patterns, url
from apps.apiv2.resources import PackageResource
from apps.apiv2.views import PackageModelList

urlpatterns = patterns(
    'apiv2.views',

    url(r'^package/$', PackageModelList.as_view(resource=PackageResource), name='api2-package-root-resource'),
    url(r'^package/(?P<slug>[-\w]+)/$', InstanceModelView.as_view(resource=PackageResource), name='api2-package-resource'),

#    url(r'^package/$', PackageRootResource.as_view(), name='api2-package-root-resource'),
#    url(r'^package/(?P<slug>[-\w]+)/$', PackageResource.as_view(), name='api2-package-resource'),
#
#    url(r'^category/$', CategoryRootResource.as_view(), name='api2-category-root-resource'),
#    url(r'^category/(?P<slug>[-\w]+)/$', CategoryResource.as_view(), name='api2-category-resource'),
#
#    url(r'^grid/$', GridRootResource.as_view(), name='api2-grid-root-resource'),
#    url(r'^grid/(?P<slug>[-\w]+)/$', GridResource.as_view(), name='api2-grid-resource'),
#
#    url(r'^grid/(?P<slug>[-\w]+)/packages/$', GridPackageRootResource.as_view(), name='api2-grid-packages-resource'),
#
#    url(r'^package-of-the-week/$', DpotwResource.as_view(), name='api2-dpotw-resource'),
#
#    url(r'^grid-of-the-week/$', GotwResource.as_view(), name='api2-gotw-resource'),
)
