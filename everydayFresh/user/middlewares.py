# coding:utf-8


class UrlMiddleware(object):
    def process_view(self, request, view_name, view_args, view_kwargs):

        if request.path not in [
            '/user/register/',
            '/user/register_handle/',
            '/user/register_valid/',
            '/user/login/',
            '/user/login_handle/',
            '/user/logout/',
            '/user/islogin/',
        ]:
            request.session['last_path'] = request.get_full_path()
