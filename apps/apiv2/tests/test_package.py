from django.core.urlresolvers import reverse
import json
from django.test import TestCase
from apiv2.tests import data


class PackageV2Tests(TestCase):
    def setUp(self):
        data.load()

    def test_01_root_packages(self):
        url_pkg1 = reverse('api2-package-root-resource')
        response_pkg1 = self.client.get(url_pkg1)
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json = response_pkg1.content
        packages = json.loads(raw_json)
        self.assertEqual(len(packages), 2)
        
    def test_02_root_packages_search(self):
        url_pkg1 = reverse('api2-package-root-resource')
        response_pkg1 = self.client.get(url_pkg1, {'slug': 'package2'})
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json = response_pkg1.content
        packages = json.loads(raw_json)
        print raw_json
        self.assertEqual(len(packages), 1)
        
    def test_03_packages_usage(self):
        url_pkg1 = reverse('api2-package-resource', kwargs={'slug': 'django-uni-form'})
        response_pkg1 = self.client.get(url_pkg1)
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json_pkg1 = response_pkg1.content
        pkg_1 = json.loads(raw_json_pkg1)
        usage_count_pkg1 = int(pkg_1['usage_count'])
        self.assertEqual(usage_count_pkg1, self.pkg1.usage.count())

        # do the same with pkg2
        url_pkg2 = reverse('api2-package-resource', kwargs={'slug': 'pinax'})
        response_pkg2 = self.client.get(url_pkg2)
        # check that the request was successful
        self.assertEqual(response_pkg2.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json_pkg2 = response_pkg2.content
        pkg_2 = json.loads(raw_json_pkg2)
        usage_count_pkg2 = int(pkg_2['usage_count'])
        self.assertEqual(usage_count_pkg2, self.pkg2.usage.count())

    def test_package_post(self):
        url_pkg1 = reverse('api2-package-resource', kwargs={'slug': 'django-uni-form'})
        response_pkg1 = self.client.post(url_pkg1, {'title': 'asdf'})
        self.assertEqual(response_pkg1.status_code, 405) # not allowed

    def test_package_delete(self):
        url_pkg1 = reverse('api2-package-resource', kwargs={'slug': 'django-uni-form'})
        response_pkg1 = self.client.delete(url_pkg1)
        self.assertEqual(response_pkg1.status_code, 405) # not allowed
