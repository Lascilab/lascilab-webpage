# Ideas
Esta es una serie de ideas para la página

## Página
 - Implementar el envio de correos
 - 
 
## Infraestructura
 - Construir los Unit Systemd o init.d para que los contenedores esten siempre arriba
 - Agregar Varnish para cache ya que es una página medianamente estática
 - Agregar redis/memcaché para hacer realidad la escalabilidad horizontal de la web
 - Agregar el stack de ELK (mas que todo Logstash y Kibana) para unificar los logs
 - Usar Vault+Counsul para proteger los secretos (contraseñas y certificados ssl)
 - Usar certificados SSL
 - Reemplazar Nginx por Trefick o por Nginx que este alerta de los contenedores que son creados dinámicamente
 - Usar Docker swarm para repartir la carga de todos los servicios
 - Hacer mas sencillo el CI/CD
 - Sacar el contenedor de HTCondor a un nuevo repo
