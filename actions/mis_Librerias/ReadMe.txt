Importar uno o mas Modulos desde la misma carpeta al "proyecto".py que estemos trabajando :
 comando :: import <Nombre_Archivo>   // Sin el .py

Importar uno o mas Modulos desde otra carpeta al "proyecto".py que estemos trabajando :
  comando: from <NombreCarpeta_DondeSeEncuetra> import <Nombre_Archivo> //El sin el .py ( <Nombre_Archivo>.py ) 


Para que pueda encontrar y se puedan importar los Modulos "<nombrearch>.py" ::

	Por consola :: echo > __init__.py   ("echo >" es el comando para crear archivos por consola)

	Otras formas::
Drirectamente creandolo desde el entorno(VSC|PyCharm) o con un arch de texto y le cambiamos la extencion a "__init__.py"

[Nota]::
__init__.py  , al crear este archivo, podemos importar (cualquier modulo) sin problemas ya que el directorio
que lo tenga , esta habilitado para importar librerias  (en nuestro caso "mis_librerias")