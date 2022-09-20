# 姓名：刘超
# 开发时间：2022/6/14 17:12
# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe
import copy
"""
自定义的分页组件，以后如果想要使用这个分页组件，你需要做如下几件事：

在视图函数中：
    def pretty_list(request):

        # 1.根据自己的情况去筛选自己的数据
        queryset = models.PrettyNum.objects.all()

        # 2.实例化分页对象
        page_object = Pagination(request, queryset,page_size=5) #每页5个数据

        context = {
            "queryset": page_object.page_queryset,  # 分完页的数据
            "page_string": page_object.html()       # 生成页码
        }
        return render(request, 'pretty_list.html', context)

在HTML页面中

    {% for obj in queryset %}
        {{obj.xx}}
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>

"""


class Pagination(object):

    def __init__(self,request,queryset,page_size = 10,page_param="page",plus = 5):
        """
            :param request: 请求的对象
            :param queryset: 符合条件的数据（根据这个数据给他进行分页处理）
            :param page_size: 每页显示多少条数据
            :param page_param: 在URL中传递的获取分页的参数，例如：/etty/list/?page=12
            :param plus: 显示当前页的 前或后几页（页码）
        """
        # print(page_size)

        # copy.deepcopy(data) 为深度复制
        quert_dict = copy.deepcopy(request.GET)
        quert_dict._mutable = True
        self.quert_dict = quert_dict

        self.page_param = page_param
        # 根据用户访问的页码访问第page页数据，计算出起止页码
        # page 为用户访问的当前页数
        page = request.GET.get(page_param,"1")   # 如果没有输入值默认为1
        if page.isdecimal():  # 如果page是整数
            page = int(page)
        else:     # 其他数据类型
            page = 1
        # print(page,type(page))
        self.page = page
        self.page_size = page_size
        # page_start和page_end为起止页
        page_start = (page - 1) * page_size
        page_end = page * page_size
        # print(page_start,page_end)
        # print(type(queryset))
        self.page_start = page_start
        self.page_end = page_end
        # page_queryset为起止页的所有数据
        self.page_queryset = queryset[self.page_start:self.page_end]    # page_start:page_end 切片操作

        # 数据总条数
        total_count = queryset.count()
        # divmod(91,10) = (9,1)  9是整除结果，1为余数
        total_page_count, div = divmod(total_count, page_size)
        if div:  # 如果div不是0说明有余数，total_page_count=total_page_count+1
            total_page_count = total_page_count + 1
        # total_page_count 为总页码数
        self.total_page_count = total_page_count

        # 计算：显示当前页的前5页、后5页 (加上当前页，一共显示11页)
        # plus = 5
        self.plus = plus


    def html(self):

        '''
                <li><a href="?page=1">1</a></li>
                <li><a href="?page=2">2</a></li>
                <li><a href="?page=3">3</a></li>
                <li><a href="?page=4">4</a></li>
                <li><a href="?page=5">5</a></li>
        '''

        # 未防止页数超过极值
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据比较少，都没有达到11页的情况
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据比较多，> 11页

            # 当前页码<5时 （小极值）
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页码>5页
                if (self.page + self.plus) > self.total_page_count:  # 当前页码+5 > 总页码 （大极值）
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        # 首页
        # 在url地址中添加一个参数，https:localhost:8000/pretty_list/?page=11&q=999
        self.quert_dict.setlist(self.page_param,[1]) # 在page=11的基础上加上q=999
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.quert_dict.urlencode()))

        # prev = '<li><a href="?page={}">上一页</a></li>'.format(1)

        # 上一页
        if self.page > 1:
            self.quert_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.quert_dict.urlencode())
            # prev = '<li><a href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            self.quert_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.quert_dict.urlencode())
            # prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
        page_str_list.append(prev)

        # 页码（前5页，当前页，后5页）
        for i in range(start_page, end_page + 1):  # [1,total_page_count+1)
            self.quert_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.quert_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.quert_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.quert_dict.setlist(self.page_param, [self.page + 1])
            after = '<li><a href="?{}">下一页</a></li>'.format(self.quert_dict.urlencode())
        else:
            self.quert_dict.setlist(self.page_param, [self.total_page_count])
            after = '<li><a href="?{}">下一页</a></li>'.format(self.quert_dict.urlencode())
        page_str_list.append(after)

        # 尾页
        self.quert_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.quert_dict.urlencode()))

        page_search_str = '''
               <li>
                   <form style="float: left;margin-left: 20px;" method="get">
                       <div class="input-group" style="width: 200px;">
                           <input type="text" name="page" style="border-radius: 0;position: relative;float: left;display: inline-block;"
                                           class="form-control" placeholder="页码">
                               <span class="input-group-btn">
                                   <button style="border-radius: 0;" class="btn btn-default" type="submit">
                                       跳转
                                       </button>
                               </span>
                       </div>
                   </form>
               </li>
           '''
        page_str_list.append(page_search_str)
        page_string = mark_safe("".join(page_str_list))
        return page_string
