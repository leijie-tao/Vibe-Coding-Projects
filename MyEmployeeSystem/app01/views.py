from django.shortcuts import render, redirect
from app01 import models  # <--- 导入模型，方便查数据库
from django import forms
from django.http import JsonResponse

def depart_list(request):
    """ 部门列表 """

    # 1. 去数据库搜所有部门 (相当于 SQL: SELECT * FROM app01_department)
    # queryset 是一个列表，里面装着所有查到的部门对象
    queryset = models.Department.objects.all()

    # 2. 把数据传给 HTML
    # context 字典里的 key ("departments") 就是 HTML 里要用的变量名
    return render(request, 'depart_list.html', {'departments': queryset})

def depart_add(request):
    """ 添加部门 """

    # 1. 如果是 GET 请求：直接展示空表单页面让用户填
    if request.method == "GET":
        return render(request, 'depart_add.html')

    # 2. 如果是 POST 请求：说明用户填完点提交了

    # 2.1 从请求包里拿到用户填写的 'title' 字段
    title = request.POST.get("title")

    # 2.2 保存到数据库
    models.Department.objects.create(title=title)

    # 2.3 保存成功后，让浏览器自动跳转回列表页
    return redirect("/depart/list/")


def depart_delete(request):
    """ 删除部门 """
    # 1. 获取用户通过 URL 传过来的 ID
    # 例如访问 /depart/delete/?nid=1，我们要拿到那个 1
    nid = request.GET.get('nid')

    # 2. 去数据库删除
    # filter(id=nid) 是查找，delete() 是删除
    models.Department.objects.filter(id=nid).delete()

    # 3. 删完跳回列表页
    return redirect('/depart/list/')


def depart_edit(request, nid):
    """ 编辑部门 """

    # 1. 根据 nid 去数据库找这个部门对象
    # first() 表示取第一个，找不到就是 None
    obj = models.Department.objects.filter(id=nid).first()

    # 如果是 GET 请求：显示页面，并把旧数据 obj 传过去
    if request.method == "GET":
        return render(request, 'depart_edit.html', {"obj": obj})

    # 如果是 POST 请求：用户改完提交了
    # 1. 获取用户提交的新标题
    title = request.POST.get("title")

    # 2. 更新数据库
    # update() 是专门用来更新的方法
    models.Department.objects.filter(id=nid).update(title=title)

    # 3. 跳转回列表页
    return redirect('/depart/list/')



from django.core.paginator import Paginator
def user_list(request):
    """ 员工列表 """
    # 抓取用户输入的搜索关键字（如果用户没搜，默认就是空字符串""）
    search_data = request.GET.get('q', "")
    #构造查询条件
    if search_data:
        # __contains 是 Django 的黑魔法，代表“包含” (相当于 SQL 里的 LIKE '%词%')
        # order_by('id') 保证了你之前的升序排列依然有效
        queryset = models.UserInfo.objects.filter(name__contains=search_data).order_by('id')
    else:
        # 如果没搜索，就查出所有人
        queryset = models.UserInfo.objects.all().order_by('id')
    # 去数据库查所有员工查出所有员工，并加个排序（.order_by('-id') 表示按 ID 倒序，后添加的员工排在最前面）

    # 2. 实例化分页器，第二个参数是“每页显示几条”。（我们设为 5 条，方便看效果）
    paginator = Paginator(queryset, 10)

    # 3. 去看看用户在网址栏里要了第几页？
    # 比如网址是 /user/list/?page=2，拿到的就是 2。如果不写，默认给第 1 页。
    page_number = request.GET.get('page', 1)

    # 4. 让分页器把那一页的数据对象拿出来
    page_obj = paginator.get_page(page_number)

    # 5. 把 page_obj 传给 HTML（注意：原来传的是 queryset，现在变了）
    return render(request, 'user_list.html', {"page_obj": page_obj,
        "search_data": search_data})

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]

    # 这一段是为了给所有输入框加 Bootstrap 样式 (看起来好看点)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

def user_add(request):
    """ 添加员工 (ModelForm 版本) """

    # GET 请求：展示空表单
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})

    # POST 请求：接收数据并校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，直接保存到数据库！
        # ModelForm 会自动处理外键关联，非常省事
        form.save()
        return redirect('/user/list/')

    # 如果数据校验失败（比如必填项没填），带着错误信息回到页面
    return render(request, 'user_add.html', {'form': form})


def user_delete(request, nid):
    """ 删除员工 """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def user_edit(request, nid):
    """ 编辑员工 """
    # 1. 先去数据库把这个员工的数据找出来
    page = request.GET.get("page", 1)
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 魔法 1：加上 instance=row_object，Django 会自动把查到的旧数据填入表单！
        # 连下拉框的默认选中项都会帮你选好！
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    # 魔法 2：POST 提交时，不仅要传新填的 data，还要传 instance
    # 这样 Django 就知道你不是要新建一行，而是要覆盖这行旧数据
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()  # 自动更新到数据库
        return redirect(f"/user/list/?page={page}")

    # 校验失败的话，带上错误信息重新显示页面
    return render(request, 'user_edit.html', {'form': form})


def login(request):
    """ 管理员登录 """
    if request.method == "GET":
        return render(request, 'login.html')

    # POST 请求：去数据库校验用户名和密码
    user = request.POST.get("username")
    pwd = request.POST.get("password")

    # 去 Admin 表里查有没有这个人
    admin_obj = models.Admin.objects.filter(username=user, password=pwd).first()

    if not admin_obj:
        # 找不到，返回错误信息
        return render(request, 'login.html', {"error_msg": "用户名或密码错误"})

    # 找到了！发放“通行证” (存入 Session)
    # 只要这行代码执行了，网站就“记住”他了
    request.session["info"] = {'id': admin_obj.id, 'name': admin_obj.username}

    # 登录成功，让他去管理后台首页（部门列表）
    return redirect('/depart/list/')


def logout(request):
    """ 注销退出 """
    # 清除当前浏览器的 Session 数据
    request.session.clear()

    # 踢回登录页面
    return redirect('/login/')


def chart_list(request):
    """ 图表展示页面 """
    return render(request, 'chart_list.html')


def chart_bar(request):
    """ 构造柱状图的数据 (从数据库查真实数据) """

    # 1. 准备空列表，用来装 X轴的部门名字，和 Y轴的员工人数
    x_axis_list = []
    data_list = []

    # 2. 去数据库查出所有的部门
    departments = models.Department.objects.all()

    # 3. 循环每一个部门，去统计它下面有几个人
    for depart in departments:
        # 把部门名字塞进 X 轴列表
        x_axis_list.append(depart.title)

        # 用 filter 找出属于这个部门的所有员工，然后用 count() 数一数有几个
        user_count = models.UserInfo.objects.filter(depart_id=depart.id).count()

        # 把人数塞进数据列表
        data_list.append(user_count)

    # 4. 按照 ECharts 需要的格式打包数据
    legend = ["员工人数"]
    series_list = [
        {
            "name": "员工人数",
            "type": "bar",
            "data": data_list
        }
    ]

    # 返回 JSON 给前端
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "x_axis": x_axis_list,
            "series_list": series_list
        }
    }

    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼图的数据：年龄分布 """

    # 1. 用 filter 和 count 统计各个年龄段的人数
    # lt 代表小于(less than)，gte 代表大于等于，gt 代表大于
    age_lt_25 = models.UserInfo.objects.filter(age__lt=25).count()
    age_25_to_35 = models.UserInfo.objects.filter(age__gte=25, age__lte=35).count()
    age_gt_35 = models.UserInfo.objects.filter(age__gt=35).count()

    # 2. 按照 ECharts 饼图需要的格式打包数据 (格式必须是 {"value": 数量, "name": 标签})
    series_data = [
        {"value": age_lt_25, "name": "25岁以下"},
        {"value": age_25_to_35, "name": "25到35岁"},
        {"value": age_gt_35, "name": "35岁以上"},
    ]

    result = {
        "status": True,
        "data": series_data
    }
    return JsonResponse(result)


def chart_line(request):
    """ 构造折线图的数据：每月入职人数趋势 """

    # 1. 查出所有员工
    users = models.UserInfo.objects.all()

    # 2. 用一个字典来记录每个月的人数，比如：{"2023-10": 2, "2023-11": 5}
    month_dict = {}
    for user in users:
        # 把入职时间转换成 "年-月" 格式的字符串
        month_str = user.create_time.strftime("%Y-%m")
        if month_str in month_dict:
            month_dict[month_str] += 1
        else:
            month_dict[month_str] = 1

    # 3. 把字典按月份先后排序
    sorted_months = sorted(month_dict.keys())
    # 按排好的月份，把对应的人数提取出来变成一个列表
    data_list = [month_dict[m] for m in sorted_months]

    result = {
        "status": True,
        "data": {
            "x_axis": sorted_months,
            "series_data": data_list
        }
    }
    return JsonResponse(result)