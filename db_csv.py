"""
###¿Qué valor en Kind tiene un error de ortografía que podría confundir a usuarios de la API?
WWW. ALIGATOR


###El siguiente bloque se repite en get_one, update y delete:
if mascota id not in db:
	raise HTTPException (status code=404, detail="Mascota

WWW. Extraerlo a una función auxiliar
	_get_or_404(mascota_id)	

###¿Cuál es el tipo de retorno declarado de la función create()?
WWW. dict

##¿Qué importación falta en operations.py si se quisiera usar MascotaResponse como tipo de retorno de create()?
WWW. from model import Mascota Response	

##¿Qué restricción impone Field(ge=0) sobre el campo age?
WWW. Que sea mayor o igual a O


##¿Qué ocurre si se llama a create() dos veces con datos idénticos de mascota?
WWW. Crea dos registros con IDs distintos


##¿Qué hace esta línea en update()?
updates = {k: v fork, v in data.model dump().items() if

WWW. Filtra solo los campos que fueron enviados con valor


##¿Qué problema tendría el filtro en update() si se escribiera if v en lugar de if v is not None, al actualizar age a 0?
WWW. El valor O sería descartado por ser falsy, ignorando la actualización 


##En MascotaUpdate, ¿por qué todos los campos son opcionales (l
None = None)?

WW. Para soportar actualizaciones parciales (PATCH)  


"""