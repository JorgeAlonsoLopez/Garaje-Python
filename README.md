# Gestión de un parking - Python

El programa se basa en la gestión de un parking.

En este tenemos dos zonas, la de administrador y la de los clientes.

Los clientes podrán ingresar y retirar sus vehículos, aportando los datos establecidos. Los datos necesarios para el cliente no abonado es el tipo de vehículo y su matricula para ingresar un vehículo y la matrícula, el nombre de la plaza y el PIN para retirarlo. En el caso de que el cliente esté abonado, necesita su matrícula y DNI para ingresar su vehículo y la matrícula, el nombre de la plaza y el PIN para retirarlo.

Si cliente no es un abonado, podrá descargar el ticket para obtener la información necesaria, tanto a la hora de ingresar como de retirar su vehículo. Este se descargará en el escritorio.  

Los administradores, para acceder, tiene que insertar la siguiente contraseña: 1234  

Podrán crear, modificar y eliminar abonos, obtener información de las plazas del parking, obtener una lista de abonos que caducan en un mes y año determinado o en los próximos 10 días y obtener una facturación procedente de los abonos, en un año determinado y de los tickets, entre dos fechas y horas determinadas.

Para crear un abono se le pedirá DNI, nombre y apellidos, nº de tarjeta, email, tipo y matrícula del vehículo, mensualidad del abono y su fecha de inicio.  
Para editar los datos de un abonado, se requiere del DNI y los datos a modificar: nombre y apellidos, email y nº de tarjeta.  
Para renovar un abono se necesita el DNI del abonado y la nueva mensualidad.  
La eliminación solo requiere del DNI.  



Para iniciar el programa, se ejecuta el ```main.py```
