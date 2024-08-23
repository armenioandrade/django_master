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

Hoje criamos as views, views são o que o python retorna para o template. O processo é relativamente simples. 
O que vai ser retornado vc configura no arquivo views.py. Caso vc vá retornar um template, o que e o normal, vc precisa
criar uma pasta 'Templates' no seu projeto e criar um html lá dentro. 
Além disso vc precisa criar uma rota para o que será exibido no arquivo 'urls.py'. 
Fizemos tb a leitura do que está no banco para exibição no html utilizando uma linguagem própria de interpretação do python no html.
Arquivos alterados: 
views.py
urls.py
templates/cars.html

Adicionamos o arquivo .gitignore para ignorar o diretório .venv

Hoje evoluímos a view, adicionamos um base_template e um template novo. 
Dessa forma conseguimos uma apresentação melhor. Pontos principais: 
1. Metodo da view fazendo consultas utilizando 'query params' do http. 

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search)
    print(search)
    return render(request, 
                  'cars.html', 
                  {'cars': cars})

search = request.GET.get('search') = Essa linha obtém o valor que o usuário passar no search da url. 
cars = Car.objects.filter(model__icontains=search) = Essa linha faz uma busca no banco filtrando pelo model o que estiver vindo do
search. 'icontains' ignora camelcase mas não ignora acentuação

2. Ao criar o base template coloque-o numa pasta 'templates' detnro de apps. Altere o arquivo settings pra ficar dessa forma
...
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["app/templates"],
...

3. No template novo foi incluído um form que contém uma action {% url action = cars_list %}
...
<form method="GET" action="{% url 'cars_list' %}">
...
esse form envia para o servidor http, o django, uma request via GET. Com o search e a action
A action 'cars_list' precisa ser configurada no 'urls.py' dessa forma
path("cars/", cars_view, name='cars_list'),

É como um apelido para o arquivo cars_view. Na view isso é tratado assim:
...
def cars_view(request): #Metodo que recebe a requisição
    cars = Car.objects.all().order_by('model') #Carrega variavel com todos os carros ordenados pelo modelo de A-Z
    search = request.GET.get('search') #Variavel para capturar o que vem do search. /?search='teste'... 'teste' seria capturado
    if search:
        cars = Car.objects.filter(model__icontains=search) #Se search contiver algo, busque por ele
    print(search) #print meu só pra testar, desnecessário
    return render(request,  
                  'cars.html', 
                  {'cars': cars}) #renderiza de volta para o usuario o resultado do que foi buscado ou não. Se nada buscado, imprime tudo
...