from django.shortcuts import render, HttpResponse, redirect
from app01.models import Book


# Create your views here.
def add(request):
    # book_list = Book.objects.create(title='白蛇传',price='11.11',pub_date='2012-12-12',publish='出版社出版社',is_pub=1)
    # book_list = Book(title='西厢记',price='11.11',pub_date='2011-11-12',publish='垃圾出版社')
    # book_list.save()
    return HttpResponse('增加成功')


def query(request):
    # obj = Book.objects.all()
    # print(obj)
    # obj = Book.objects.filter().first()
    # print(obj)
    # obj = Book.objects.filter().last()
    # print(obj)
    # obj = Book.objects.filter(price=12.12)
    # print(obj)
    # ret = Book.objects.all()[2]
    # print(ret)
    # ret = Book.objects.exclude(nid = 3)
    # print(ret)
    # ret =Book.objects.all().order_by("price").reverse()
    # print(ret)
    # ret = Book.objects.all().count()
    # print(ret)
    # ret = Book.objects.all().values_list('title','price')
    # print(ret)
    # ret = Book.objects.all().filter(title__startswith="py",pub_date__year=2017,pub_date__month=8)
    # print(ret)
    # ret = Book.objects.all().filter(price__in=[50,100,150])
    # print(ret)
    # ret = Book.objects.all().filter(price__gt=200)
    # print(ret)
    # ret = Book.objects.all().filter(price__range=[100,200])
    # print(ret)
    # ret = Book.objects.all().filter(publish="人民出版社").order_by("price")
    # print(ret)
    # ret = Book.objects.all().filter(price__gt=200)
    # print(ret)
    # ret = Book.objects.all().exclude(price=100).values_list("title")
    # print(ret)
    #
    return HttpResponse('查看成功')


def index(request):
    ret = Book.objects.all()
    print(ret)
    return render(request, "index.html", {"ret": ret})


def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        pub_date = request.POST.get("pub_date")

        ret = Book.objects.create(title=title, price=price, publish=publish, pub_date=pub_date)

        return redirect("/index/")
    return render(request, "addbook.html")


def change(request, id):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        pub_date = request.POST.get("pub_date")
        Book.objects.filter(nid=id).update(title=title, price=price, publish=publish, pub_date=pub_date)
        return redirect("/index/")
    book_obj = Book.objects.get(nid=id)
    print(book_obj)
    return render(request, "change.html", {'book_obj': book_obj})


def delete(request, id):
    Book.objects.filter(nid=id).delete()

    return redirect("/index/")
