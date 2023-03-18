Actividad 2 Francisco Javier Pérez Salas A01748965

Para poder crear la imagen debemos seguir los siguientes pasos:

1. Ejecutar el comando: docker build -t app .

//Use el puerto 8000 ya que ocupo los puertos 3000 y 5000 para mi trabajo

2. Ejecutar el comando: docker run -p 8000:8000 -d app

3. Desde su navegador ingresar a: localhost:8000

4. Probar la aplicación desde el localhost

    a) El nombre del usuario debe empezar con Mayuscula
    
    b) La contraseña debe contener letras y numeros
    
    c) El template de Login es reutilizado, solo lo ajuste a los requerimientos del la actividad 


5. Para detener la image Ejecutamos el siguiente comando: docker container ls

6. Copiamos el ID de nuestra imagen llamada app ya que lo ocuparemos en el siguiente paso

7. Ejecutamnos el comando: docker stop "pegamos el id"
