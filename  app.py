from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import os

# دالة العرض الرئيسية التي ستعرض صفحة HTML
@view_config(route_name='home', renderer='templates/mytemplate.html')
def home_view(request):
    return {}

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    with Configurator() as config:
        # تعريف مسار الصفحة الرئيسية
        config.add_route('home', '/')
        # تضمين Jinja2 كقالب
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.jinja2')
        # إعداد الملفات الثابتة
        config.add_static_view(name='static', path=os.path.join(here, 'static'))
        # البحث عن دوال العرض
        config.scan()
        # إنشاء تطبيق WSGI
        app = config.make_wsgi_app()
    
    from waitress import serve
    # تشغيل التطبيق على المنفذ 6543
    serve(app, host='0.0.0.0', port=6543)