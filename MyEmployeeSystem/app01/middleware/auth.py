from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """ 登录拦截中间件 """

    def process_request(self, request):
        # 1. 排除不需要保安检查的页面 (比如登录页本身，不然会死循环)
        if request.path_info in ["/login/"]:
            return  # return None 意味着放行，让他继续往后走

        # 2. 检查他的兜里有没有我们发的“通行证” (Session)
        info_dict = request.session.get("info")

        if info_dict:
            # 身上有通行证，说明登录过了，放行
            return

        # 3. 没通行证？直接踢回登录页面！
        return redirect('/login/')