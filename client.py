import requests
import logging
from typing import List, Union

#configuracion del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CalculadoraCliente:
    def __init__(self, base_url: str="http://127.0.0.1:8000"):
        sef.base_url = base_url

    def calcular_promedio(self, numeros:List[Union[int, float]]) -> float:
        try:
            response = requests.post(f"{self.base_url}/calcular_promedio", json={"numeros": numeros})
            if response.status_code != 200:
                logger.error(f"Request ERROR: {response.status_code} - {response.text}")
                raise ValueError(f"API ERROR: {response.text}")
            
            resultado = response.json()
            logger.info(f"Promedio recibido: {resultado['promedio']}")
            return resultado["promedio"]
        
        except requests.ConnectionError:
            logger.error("Cannot connect to the API.")
            raise ConnectionError("Cannot connect to the API.")

    def obtener_ultimo_promedio(self) -> float:
        try:
        	response = requests.get(f"{self.base_url}/ultimo_promedio")
        	if response.status_code != 200:
        		logger.error(f"Request Error: {response.status_code} - {response.text}")
        		raise ValueError(f"API Error: {response.text}")

        	resultado = response.json();
        	logger.info(f"ultimo_promedio recibido: {resultado[ultimo_promedio]}")
        	return resultado[ultimo_promedio]

        except requests.ConnectionError:
        	logger.error("Cannot connect to the API")
        	raise ConnectionError("Cannot connect to the API")

if __name__ == "__main__":
	cliente = CalculadoraCliente()
	try:
		promedio = cliente.calcular_promedio([1,2,3,4,5])
		print(f"Promedio calculado: {promedio}")

		ultimo = cliente.obtener_ultimo_promedio()
		print(f"Ultimo promedio: {ultimo}")

	except (ValueError, ConnectionError) as e:
		print(f"WARNING ERROR: {str(e)}")
