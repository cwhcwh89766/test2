import views
urls = [
        (r'/$',views.index),
        (r'/login',views.login),
        (r'/(\w*/)*(\w*\.html)$',views.load_html),
        (r'/(\w*/)*(\w*\.(jpg|jpeg|bmp|gif|png))$',views.load_picture),
        # (r'/(\w*/)*(\w*\.css)$',views.load_css),
        # (r'/(\w*/)*(\w*\.js)$',views.load_js),
    ]