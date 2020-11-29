# VHL-Hunter
## Ejecución
Requiere nodejs instalado. 
Dependencias: 
<ul>
  <li>body-parser: 1.19.0</li>
  <li>express: 4.17.1</li>
  <li>mongoose: 5.10.15</li>
  <li>nodemon: 2.0.6</li>
</ul>
Una vez en el directorio: <br>

```bash
npm start
```

## Uso
El backend corre en el puerto 3800. 
Tiene implementadas las rutas de consulta a la base de datos: 
## getMutation
Devuelve una sola mutación, según el nombre ingresado como parámetro: <br>

```web
http://localhost:3800/api/getMutation/:mutationName?
```

## getCases
Devuelve un listado con los casos en los que se ha visto involucrada la mutación, ingresada como parámetro:

```web
http://localhost:3800/api/getCases/:mutationName?
```

## getEffects
Devuelve un listado con los efectos que posee determinada mutación, ingresada como parámetro: 

```web
http://localhost:3800/api/getEffects/:mutationName?
```

## getVHL
Devuelve un listado con los tipos de vhl que posee determinada mutación, ingresada como parámetro: 

```web
http://localhost:3800/api/getVHL/:mutationName?
```

## getMutationsbyEffect
Devuelve un listado de mutaciones con un efecto asociado, ingresado como parámetro: 

```web
http://localhost:3800/api/getMutationsbyEffect/:effect?
```

## getMutationsbyRisk
Devuelve un listado de mutaciones con un riesgo clínico asociado, ingresado como parámetro: 

```web
http://localhost:3800/api/getMutationsbyRisk/:risk?
```

## getMutationsbyRisk
Devuelve un listado de mutaciones según un tipo de mutación, ingresado como parámetro: 

```web
http://localhost:3800/api/getMutationsbyType/:mutationType?
```

## getMutationsbyVHL
Devuelve un listado de mutaciones según un tipo de vhl asociado, ingresado como parámetro: 

```web
http://localhost:3800/api/getMutationsbyVHL/:vhl?
```

## getVHLtotal
Devuelve un listado de todos los tipos de VHL encontrados en la base de datos: 

```web
http://localhost:3800/api/getVHLTotal/
```

## getEffectsTotal
Devuelve un listado de todos los efectos encontrados en la base de datos: 

```web
http://localhost:3800/api/getEffectsTotal/
```
