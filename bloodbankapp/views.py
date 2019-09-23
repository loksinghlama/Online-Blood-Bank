from django.shortcuts import render
from django.http import HttpResponse
from .models import requestClass as ac, donated, stockinput as st
from django.utils import timezone

# Create your views here.
def home(request):
	
	return render(request,'home.html')

def stockinput(request):
	if request.method == "POST":
		name = request.POST['name']
		
		mobile = request.POST['mobile']
		
		address = request.POST['address']
		
		bloodgroup = request.POST['bloodgroup']
		
		add = st.objects.create(name = name, mobile = mobile, address = address, bloodgroup = bloodgroup)
		add.save()
		print('successfully added stock')
		return render(request,'stockinput.html')
	else:
		return render(request,'stockinput.html')

def stock(request):
	if request.method == "GET":
		obj = st.objects.all()
		return render(request,'stock.html', {'obj': obj})
	
def request(request):
	if request.method == "POST":
		name_request = request.POST['name_request']
		mobile_request = request.POST['mobile_request']
		address_request = request.POST['address_request']
		bloodgroup_request = request.POST['bloodgroup_request']
		email_request = request.POST['email_request']
		dateline_request = request.POST['dateline_request']
		print(email_request)
		
		request_blood = ac.objects.create(name_request=name_request, mobile_request=mobile_request, address_request=address_request, email_request=email_request, bloodgroup_request=bloodgroup_request, dateline_request=dateline_request)
		request_blood.save()
		# print('successfully requested blood')
		return render(request,'request.html')

	else:
		return render(request,'request.html')

def requestlist(request):
	if request.method == "GET":
		req = ac.objects.all()
		print(req)
		return render(request,'requestlist.html', {'req': req})
	if request.method == "POST":
		checkbox = request.POST.getlist('checkbox')

		b = ''
		lists = []

		for p in checkbox:
			b = st.objects.filter(name=p)

			for l in b:
				dict = {
				'stock_name':l.name,
				'stock_mobile':l.mobile,
				'stock_address':l.address,
				'stock_bloodgroup':l.bloodgroup
				}
				requestlist = ac.objects.create(name_request=l.name, mobile_request=l.mobile, address_request=l.address, bloodgroup_request=l.bloodgroup)
				requestlist.save()
				lists.append(dict)
		return render(request,'requestlist.html', {'b': b,'lists':lists})
	if request.method == "GET":
		b=st.objects.all()
		request_lists = ac.objects.all()
		context = {'b': b,'request_lists':request_lists}
		return render(request,'requestlist.html', context)


def donatedlist(request):
	if request.method == "POST":
		checkbox = request.POST.getlist('checkbox')
		a = ''
		lists = []
		donated_lists = donated.objects.all()
		for i in checkbox:
			a=ac.objects.filter(name_request=i)	
			# print(a,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
			for j in a:
				dictt={
					'name':j.name_request,
					'email':j.email_request,
					'mobile':j.mobile_request,
					'address':j.address_request,
					'bg':j.bloodgroup_request,
					'datee':j.dateline_request
				}
				donatedlist = donated.objects.create(donate_name=j.name_request, donate_email=j.email_request, donate_mobile=j.mobile_request, donate_address=j.address_request, donate_bloodgroup=j.bloodgroup_request)
				donatedlist.save()
				a= ac.objects.get(id=j.id)
				a.delete()
				lists.append(dictt)
		return render(request,'requestlist.html', {'a': a,'lists':lists,'donated_lists':donated_lists})
	if request.method == "GET":
		a=ac.objects.all()
		donated_lists = donated.objects.all()
		context = {'a': a,'donated_lists':donated_lists}
		return render(request,'donatedlist.html', context)

