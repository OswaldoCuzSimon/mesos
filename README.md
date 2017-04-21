# mesos

## Synopsis
Este repositorio es un conjunto de Jobs de Mesos para calendarizar con Marathon

## Rendimiento de Mesos vs CentOS
Para comparar el rendimiento se ejecuto un script en python que imprime una succesion de numeros de uno hasta n-1
se realizaron 2 experimentos uno con n = 1,000,000 y otro con n = 10,000,000
cada experimento se ejecuto en Mesos y en CentOS

El script que se ejecuto es [hello_mesos.py](https://github.com/OswaldoCuzSimon/mesos/blob/master/hello_mesos.py)
La definicion del Job es [hello_mesos.json](https://github.com/OswaldoCuzSimon/mesos/blob/master/hello_mesos.json)

Cada experimiento se repitio tres veces y se obtuvo de cada repeticion:

Tiempo real: tiempo que tardo el proceso desde que se ejecuto hasta que termino

Tiempo sys:  tiempo  que ocupó el CPU en el proceso

## Arquitectura de Mesos

|host| funcion   |      cpu      |  ram |
|------|----------|:-------------:|------:|
|10.110.70.47 |  master | intel i5 Quad Core| 4 GB |
|10.110.70.100|  slave  | intel i5 Quad Core| 4 GB |
|10.110.70.32 |  slave  | intel i5 Quad Core| 4 GB |
|10.110.70.89 |  slave  | intel i5 Quad Core| 4 GB |

## Procedimiento

#### Comando para ejecutar un Job nuevo a marathon
```shell
curl -X POST http://10.110.70.47:8080/v2/apps -d @hello_mesos.json -H "Content-type: application/json"
```

#### Comando para ejecutar un script de python en CentOS
```shell
/usr/bin/time -f "\t%U user,\t%S system,\t%e real" python hello_mesos.py
```

## Resultados
Los tiempos estan expresados en segundos

### Experimento con n = 1,000,000

|id rep| tiempo   |      Mesos      |  CentOS |
|------|----------|:-------------:|------:|
|1| real | 0.419 | 20.17  |
|1|  sys | 0.026 | 2.58   |
|2| real | 0.496 | 20.20  |
|2|  sys | 0.026 | 2.98   |
|3| real | 0.609 | 20.06  |
|3|  sys | 0.043 | 2.78   |

### Experimento con n = 10,000,000

|id rep| tiempo   |      Mesos      |  CentOS |
|------|----------|:-------------:|------:|
|1| real | 4.706 | 225.67 |
|1|  sys | 0.185 | 29.41  |
|2| real | 3.856 | 225.89 |
|2|  sys | 0.202 | 30.07  |
|3| real | 4.848 | 225.56 |
|3|  sys | 0.176 | 30.09  |

## Conclusiones

Como se puede observar en los resultados Mesos ejecuta el script en un tiempo 
considerablemente menor.

El script en Mesos corre hasta 48 veces mas rapido
