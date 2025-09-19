from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

#Endpoints:
#  POST /calcular_promedio: Cacula el promedio de una lista de numeros
#  GET  /obtener_ultimo_promedio: Devuelve el ultimo promedio calculado

#Configuracion del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Modelo para validar los datos de entrada.
class NumerosInput(BaseModel):
	numeros: List[float]

ultimo_promedio = None

#ENDPOINT
@app.POST("/calcular_promedio")
async def calcular_promedio(data: NumerosInput):
	try:
		if not data.numeros:
			logger.error("Empty list")
			raise HTTPException(status_code=400, detail="List cannot be empty.")

		promedio = sum(data.numeros)/len(data.numeros)
		global ultimo_promedio
		ultimo_promedio = promedio
		logger.info(f"Promedio Calculado: {promedio} para {data.numeros}")
		return {"promedio": promedio}

	except Exception as e:
		logger.error(f"Error calculating mean: {str(e)}.")
		raise HTTPException(status_code=500, detail="Internal Error.")

@app.GET("/ultimo_promedio")
async def obtener_ultimo_promedio():
	if ultimo_promedio is None:
		logger.warning("No previous mean.")
		raise HTTPException(status_code=404, detail="No previous mean.")
	return {"ultimo_promedio":ultimo_promedio}