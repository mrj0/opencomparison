from package.models import Package
from package.models import Category
from decimal import Decimal
import datetime

def load():
    category1, created = Category.objects.get_or_create(
        id=1,
        created=datetime.datetime(2010, 8, 14, 22, 47, 52),
        modified=datetime.datetime(2010, 9, 12, 22, 42, 58, 53698),
        title=u'App',
        slug=u'apps',
        description=u'Small components used to build projects. An app is anything that is installed by placing in settings.INSTALLED_APPS.',
        title_plural=u'Apps',
        show_pypi=True,
    )

    package2, created = Package.objects.get_or_create(
        id=2,
        created=datetime.datetime(2010, 8, 14, 23, 9, 44),
        modified=datetime.datetime(2011, 9, 8, 23, 5, 9, 463518),
        title=u'Django Uni-Form',
        slug=u'django-uni-form',
        category=category1,
        repo_description=u'Django forms are easily rendered as tables, paragraphs, and unordered lists. However, elegantly rendered div based forms is something you have to do by hand. The purpose of this application is to provide a tag and filter that lets you quickly render forms in a div format while providing an enormous amount of capability to configure and control the rendered HTML.',
        repo_url=u'https://github.com/pydanny/django-uni-form',
        repo_watchers=450,
        repo_forks=74,
        repo_commits=0,
        pypi_url=u'http://pypi.python.org/pypi/django-uni-form',
        pypi_downloads=30863,
        participants=u'pydanny,jtauber,ojii,maraujop,j0hnsmith,mvaerle,agentk,johnthedebs,issackelly,skyl,sorki,acdha,DarylAntony,bmihelac,akaihola,jjmaestro,Narsil,brosner,adamcupial,philwo,boardman,arowla',
        created_by=None,
        last_modified_by=None,
        pypi_home_page=None,
    )

    category2, created = Category.objects.get_or_create(
        id=2,
        created=datetime.datetime(2010, 8, 14, 22, 48, 52),
        modified=datetime.datetime(2010, 9, 12, 22, 43, 4, 426686),
        title=u'Framework',
        slug=u'frameworks',
        description=u'Large efforts that combine many python modules or apps. Examples include Django, Pinax, and Satchmo. Most CMS falls into this category.',
        title_plural=u'Frameworks',
        show_pypi=True,
    )

    package25, created = Package.objects.get_or_create(
        id=25,
        created=datetime.datetime(2010, 8, 17, 2, 25, 16, 648485),
        modified=datetime.datetime(2011, 9, 8, 23, 10, 34, 478203),
        title=u'Pinax',
        slug=u'pinax',
        category=category2,
        repo_description=u'a Django-based platform for rapidly developing websites',
        repo_url=u'https://github.com/pinax/pinax',
        repo_watchers=1363,
        repo_forks=235,
        repo_commits=0,
        pypi_url=u'http://pypi.python.org/pypi/Pinax',
        pypi_downloads=0,
        participants=u'brosner,jezdez,jtauber,lukeman,paltman,transifex,issackelly,winhamwr,dstufft,bmihelac',
        created_by=None,
        last_modified_by=None,
        pypi_home_page=None,
    )


