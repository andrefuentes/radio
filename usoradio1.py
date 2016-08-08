from radio import radio
mi_radio=radio("sony")
desea_continuar=True
opc=0
print("que desea hacer 1.subir_volumen,2.bajar_volumen,3.subir_emisoraFM,4.bajar_emisoraFM,5.3.subir_emisoraaM,4.bajar_emisoraAM")
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
		if opc==5:
			mi_radio.bajar_emisoraAM
		if opc==6:
			mi_radio.subir_emisoraAm

	else:
		print(mi_radio.apagado)
		print(mi_radio.encender)
		print(mi_radio.salir)

