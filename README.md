# Parcial-Devops

## Intrucciones

### Contruccion de la imagen
docker build -t py_hola_mundo:latest .

### Ejecucion de contenedor de la imagen
docker run -d -p 8000:8000 --name py_hola_mundo  py_hola_mundo:latest

### Uso
Abre tu navegador y pega la siguiente direccion localhost:8000/hola_mundo