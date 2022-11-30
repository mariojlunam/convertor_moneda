

def convert_currency(currency_input_code: str, currency_input_amount: float, currency_output_code: str) -> float:
	
	# Dictionario con valores de conversion de cada moneda
	# Data de google al 29/11/2022
	USD_RATE = {"EUR": 1.03, "BS": 10.7126, "COP": 4811.09 , "BRL": 5.27}

	# Chequear si soportamos la conversion de la moneda input
	if currency_input_code not in USD_RATE and currency_input_code != "USD":

		print(f"Programa no soporta la conversion de moneda {currency_input_code}")

		exit()

	elif currency_input_code == currency_output_code:

		print(f"Programa no soporta la conversiones entre la misma moneda {currency_input_code}")

		exit()

	if currency_input_code == "USD":

		# Acceder valor de dictionario usando el codigo de la moneda como key para buscar el valor de conversion
		rate_conversion = USD_RATE[currency_output_code]

		# Aplicar conversion usando la cantidad establecida por el usuario
		amount_converted = currency_input_amount * rate_conversion

		return amount_converted

	else : 

		# Acceder valor de dictionario usando el codigo de la moneda como key para buscar el valor de conversion
		rate_conversion = USD_RATE[currency_input_code]

		# Aplicar conversion usando la cantidad establecida por el usuario
		amount_converted = currency_input_amount / rate_conversion

		return amount_converted

# Input de usuario ("DE MONEDA", "MONTO" "A MONEDA")
amount_converted = convert_currency("USD", 12, "USD")

print(amount_converted)