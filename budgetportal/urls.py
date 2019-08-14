from adminplus.sites import AdminSitePlus

from budgetportal.views import openspending_csv, about, events, videos, terms_and_conditions, search_result, resources, \
    guides, dataset_landing_page, dataset_category_data, dataset_data, glossary, faq, contributed_datasets_list, \
    contributed_dataset, dataset_category_migrated, dataset_migrated, infrastructure_project_list, \
    dataset_landing_page_json, dataset_landing_page_yaml, dataset_category_yaml, dataset_category_json, dataset_json, \
    contributed_datasets_list_json, contributed_dataset_json
from discourse.views import sso
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from . import views
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from . import bulk_upload

admin.site = AdminSitePlus()
admin.autodiscover()

CACHE_SECS = 0


def permission_denied(request):
    raise PermissionDenied()


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/focus.yaml', cache_page(CACHE_SECS)(views.focus_preview)),

    # National and provincial treemap data
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<phase_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.homepage)),

    # Preview pages
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/previews'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<government_slug>[\w-]+)'
        '/(?P<phase_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.department_preview)),

    # Consolidated
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/consolidated.yaml', cache_page(CACHE_SECS)(views.consolidated_treemap)),

    # Home Page
    url(r'^(?P<financial_year_id>\d{4}-\d{2}).yaml$',
        cache_page(CACHE_SECS)(views.year_home)),

    # Search results
    url(r'^(?P<financial_year_id>\d{4}-\d{2})/search-result.yaml',
        cache_page(CACHE_SECS)(views.FinancialYearPage.as_view(
            slug='search-result',
        ))),

    # Department list as CSV
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/departments.csv$', cache_page(CACHE_SECS)(views.department_list_csv)),

    # Department list for sphere as CSV
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/(?P<sphere_slug>[\w-]+)'
        '/departments.csv$',
        cache_page(CACHE_SECS)(views.department_list_for_sphere_csv)),

    # Programme list as CSV
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/(?P<sphere_slug>[\w-]+)'
        '/programmes.csv$', cache_page(CACHE_SECS)(views.programme_list_csv)),

    # Authentication
    url(r'^accounts/email.*', permission_denied),
    url(r'^accounts/', include('allauth.urls')),

    # SSO Provider
    url(r'^(?P<client_id>\w+)/sso$', sso),

    # CSV
    url(r'^csv/$', openspending_csv, name='openspending_csv'),

    # Admin
    url(r'^admin/', admin.site.urls),
    url(r'^admin/bulk_upload/template', bulk_upload.template_view),

    # Budget Portal
    url(r'^about/?$', about, name="about"),
    url(r'^events/?$', events, name="events"),
    url(r'^videos/?$', videos, name="videos"),
    url(r'^terms-and-conditions/?$', terms_and_conditions, name="terms-and-conditions"),
    url(r'^resources/?$', resources, name="resources"),
    url(r'^glossary/?$', glossary, name="glossary"),
    url(r'^faq/?$', faq, name="faq"),
    url(r'^guides/?$', guides, name="guides", kwargs={'slug': 'index'}),
    url(r'^guides/(?P<slug>[-\w]+)/?$', guides, name="guides"),

    # Dataset landing page
    url(r'^datasets/?$', dataset_landing_page, name="dataset-landing-page"),
    url(r'^datasets.json$', dataset_landing_page_json, name="dataset-landing-page-json"),
    url(r'^datasets.yaml$', cache_page(CACHE_SECS)(views.dataset_landing_page_yaml)),

    url(r'^datasets/contributed/?$', contributed_datasets_list, name="contributed-datasets"),
    url(r'^datasets/contributed.json$', contributed_datasets_list_json, name="contributed-datasets-json"),

    url(r'^datasets/contributed/(?P<dataset_slug>[-\w]+)/?$', contributed_dataset, name="contributed-dataset"),
    url(r'^datasets/contributed/(?P<dataset_slug>[-\w]+).json$', contributed_dataset_json, name="contributed-dataset"),

    # Dataset categories
    url(r'^datasets/(?P<category_slug>[-\w]+)/?$', dataset_category_migrated, name="dataset-category"),
    url(r'^datasets/(?P<category_slug>[-\w]+).json?$', dataset_category_json, name="dataset-category-json"),
    url(r'^datasets/(?P<category_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.dataset_category_yaml)),

    # Detaset detail
    url(r'^datasets/(?P<category_slug>[-\w]+)/(?P<dataset_slug>[-\w]+)/?$', dataset_migrated, name="dataset"),
    url(r'^datasets/(?P<category_slug>[-\w]+)/(?P<dataset_slug>[-\w]+).json?$', dataset_json, name="dataset-json"),
    url(r'^datasets/(?P<category_slug>[\w-]+)/(?P<dataset_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.dataset_yaml)),

    url(r'^(?P<financial_year_id>\d{4}-\d{2})/search-result/?$', search_result, name="search-result"),

    # Infrastructure projects
    url(r"^infrastructure-projects/?$", infrastructure_project_list, name="infrastructure-project-list"),
    url(r'^infrastructure-projects.yaml$', cache_page(CACHE_SECS)(views.infrastructure_projects_overview_yaml)),
    url(r'^json/infrastructure-projects.json$', cache_page(CACHE_SECS)(views.infrastructure_projects_overview_json)),
    url(r'^infrastructure-projects/(?P<project_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.infrastructure_project_detail)),

    # Department List
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/departments$', cache_page(CACHE_SECS)(views.department_list)),
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/departments.yaml', cache_page(CACHE_SECS)(views.department_list_yaml)),
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/departments.json', cache_page(CACHE_SECS)(views.department_list_json)),
    # Department detail
    url(r'^(?P<financial_year_id>\d{4}-\d{2})/national/departments/(?P<department_slug>[\w-]+)$',
        cache_page(CACHE_SECS)(views.department_migrated),
        kwargs={'sphere_slug': 'national', 'government_slug': 'south-africa'}),
    url(r'^(?P<financial_year_id>\d{4}-\d{2})/national/departments/(?P<department_slug>[\w-]+).yaml$',
        cache_page(CACHE_SECS)(views.department_yaml),
        kwargs={'sphere_slug': 'national', 'government_slug': 'south-africa'}),
    url(r'^(?P<financial_year_id>\d{4}-\d{2})/national/departments/(?P<department_slug>[\w-]+).json',
        cache_page(CACHE_SECS)(views.department_json),
        kwargs={'sphere_slug': 'national', 'government_slug': 'south-africa'}),

    url(r'^(?P<financial_year_id>[\w-]+)'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<government_slug>[\w-]+)'
        '/departments'
        '/(?P<department_slug>[\w-]+)$', cache_page(CACHE_SECS)(views.department_migrated)),
    url(r'^(?P<financial_year_id>[\w-]+)'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<government_slug>[\w-]+)'
        '/departments'
        '/(?P<department_slug>[\w-]+),json$', cache_page(CACHE_SECS)(views.department_json)),
    url(r'^(?P<financial_year_id>[\w-]+)'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<government_slug>[\w-]+)'
        '/departments'
        '/(?P<department_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.department_yaml)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
