from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,View
from getname import random_name
from docker import Client
import string
import datetime

# Create your views here.

class Index(TemplateView):
    template_name = 'thesis/index.html'
    
class Docker(View):
    def get(self, request):
        cli = Client(base_url='unix://var/run/docker.sock')
        nombre = "htcondor"+(''.join(ch for ch in random_name('cat') if ch.isalpha())).lower()
        #fecha = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # https://docker-py.readthedocs.io/en/latest/hostconfig/
        # host_config= 
        #    cli.create_host_config(cap_drop=['MKNOD'], pids_limit= , cpuset_cpus (str), mem_limit="256m"
        #            cpu_shares (int), cpu_period (int), cpu_group (int), memswap_limit (str or int))
        #            sysctls(?)
        container = cli.create_container(image="htcondor:latest", name=nombre, hostname=nombre,
                                          ports=["3000"], 
                                          labels={"container": "htcondor", "createdat":"hoy"})
        netId = cli.inspect_network('lascilabwebpage_default')
        cli.connect_container_to_network(container["Id"],netId["Name"])
        cli.start(container=container.get('Id'))
        return render(request, "thesis/lobby.html", {
            'contenedor' : nombre
        })
        #return redirect('/condor/'+nombre+'/')
