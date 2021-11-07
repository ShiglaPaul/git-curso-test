#from django.test import TestCase
from .models import Type
# Create your tests here.
#Listar
#select * from tabla
query=Type.objects.all()
print(query)
#insercion
t=Type()
t.name='Administrador'
t.save()
#----------
t=Type(name='Administrador').save()
#Edicion
t=Type.objects.get(id=1)
print(t.name)
print("hola mundo")
#filter permitehacer filtros es como like en sql
#los que contengan pre
#que contengan letras especificas si es mayuscula que sea mayscula y visceversa
obj=Type.objects.filter(name__contais='pre')
print(obj)
#que excluyan mayuscula o minucula con tal de ue tenga esa palabre
obj=Type.objects.filter(name__icontais='pre')
#las q empiezan con
obj=Type.objects.filter(name__startwith='pre')
#las que terminen con
obj=Type.objects.filter(name__endswith='pre')
#in las que se encuentre en losvectore q se encuenren
obj=Type.objects.filter(name__in=['viva','hola'])
#contar 
obj=Type.objects.filter(name__in=['viva','hola']).count()
#sale el codigo de la consulta sql q estamos ejecutando
obj=Type.objects.filter(name__in=['viva','hola']).query
#exclude cierto id
obj=Type.objects.filter(name__endswith='va').exclude(i=5)

