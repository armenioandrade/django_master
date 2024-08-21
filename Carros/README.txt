Processo de criação de um projeto Django
1. Criar a pasta do projeto, nesse caso Carros
2. Dentro de carros executar: 'django-admin startproject app .'
Professor instruiu dessa maneira porque essa pasta 'app' é o coração do projeto, algo como a main
3.'python manage.py startapp cars'. Vai ser criada uma pasta 'cars' que é uma app do Django
4. No arquivo settings.py adicione uma linha com o nome da app dentro de 'Installed Apps' ficando assim:

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cars",
]

5.'python manage.py makemigrations'. Esse comando vai ler o projeto inteiro e preparar pra dar o migrate
6.'python manage.py migrate'. Esse comando é o que vai executar as migrations
7.'python manage.py createsuperuser'. Esse comando vai oferecer um wizard pra criar um usuário admin do painel django na porta 8000
8.'python manage.py runserver'. Esse comando vai iniciar o projeto localhost:8000. localhost:8000/admin vai para o painel de admin
9. Depois eu criei a classe Car dentro de models.py. Essa classe herda de models e contém várias coisas pra criar campos no banco. Essa classe Car vai ser basicamente o espelho de uma tabela do banco de dados.
10. Em seguida rodamos novamente o makemigrations e migrate para ler o projeto e aplicar mudanças

11. Em seguida cadastrei essa classe dentro de admin.py

from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin): #Aqui to herdando de Model Admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #Aqui eu to dizendo o que vai aparecer no listar do admin
    search_fields = ('model',) #Aqui eu to dizendo pelo o que eu quero buscar

admin.site.register(Car, CarAdmin) #Aqui eu to tipo dando um commit pra aplicar esse perfil na tabela cars

Hoje adicionamos um campo 'plate' e 'photo' para a class Car, além disso criamos uma class 'Brand' e apontamos o campo 
'brand' da classe 'Car' como uma ForeignKey para a classe Brand.

Também mexemos no campo settings para traduzir a pagina de administração para 'pt-br' e mudamos o fuso-horário para 'America/Recife'

Ao criar o campo Brand é necessário editar o arquivo 'admin.py' para criar a classe com as permissões dessa tabela

Ao criar o campo photo foi necessário mexer no arquivo 'settings.py' e 'urls.py'. Nos dois arquivos foram adicionados essas linhas

settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
