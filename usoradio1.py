from radio import radio
mi_radio=radio("sony")
desea_continuar=True
opc=0
print("que desea hacer 1.subir_volumen,2.bajar_volumen,3.subir_emisora,4.bajar_emisora,5.")
while desea_continuar:
	if mi_radio.encendido:
		if opc==1:
		mi_radio.subir_volumen
		if opc==2:
		mi_radio.bajar_volumen
		if opc==3:
		mi_radio.subir_emisoraFM
		if opc==4:
		mi_radio.bajar_emisoraFM
	else:
		mi_radio.apagado
		mi_radio.encender
		mi_radio.salir

