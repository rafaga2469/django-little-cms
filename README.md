# django-little-cms

[Por Rafael Ricardo Pinto - https://www.linkedin.com/](https://www.linkedin.com/in/rafael-ricardo-pinto-díaz-508017123) 

Este paquete incluye [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/#) cómo componente para campos de texto enriquecido.

<br>

Simple y eficaz módulo CMS que se integra al admin de django  

<br>

## 💡 Pre-requisitos

   [Python 3.10](https://www.python.org/downloads/release/python-3105/)
   <br>
   [Django 4.0.6](https://docs.djangoproject.com/en/4.0/releases/4.0.6/)


## Instalación

 1. Instale o agregue sjango-little-cms a su ambiente de python
 
	  `pip install django-little-cms`
  
 3. Agregue `'littlecms'` al parámetro `INSTALLED_APPS`.
 4. Agregue las siguientes aplicaciones al parámetro `INSTALLED_APPS`.
	
       	'django_bootstrap5',
       	'ckeditor',
       	'ckeditor_uploader',
       	'colorfield',
       	'fontawesomefree',
 5. Agregue `'littlecms.context_processors.menuOptions',` al atributo `'context_processors'` del parámetro `TEMPLATES`
 6. Es importante definir los parámetros `MEDIA_ROOT` y `MEDIA_URL` así cómo `CKEDITOR_UPLOAD_PATH` los cuales son requeridos por [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/#) para el cargue de imágenes dentro de los campos de texto enriquecido.
 
		 #Media parameters
		 
		 MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
		 MEDIA_URL = '/media/'
		 
		 #django-ckeditor parameters
		 CKEDITOR_UPLOAD_PATH = "uploads/"
6. Incluya las siguientes rutas en el archivo `urls.py` del proyecto
		
		path('', include(littlecms_urls)),
		path('ckeditor/', include(ckeditor_urls)),
7. Ejecute las migraciones del proyecto
		`python manage.py migrate littlecms`

