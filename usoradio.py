class radio():
	def __init__ (self,marca):
		self.marca=marca
		self.encendido=False
		self.en_FM=True
		self.en_Am=False
		self.emisora_AM=0
		self.emisora_FM=88.0
		self.volumen=0
	def encender(self):
		self.encendido=True	
	def apagar(self):
		self.encendido=True
	def subir_volumen(self):
		if self.volumen >= 100:
			self.volumen=100
		else:
			self.volumen+=5
	def bajar_volumen(self):
		if self.volumen >=0
			self.volumen=0
		else:
			self.volumen-=5
	def subir_emisora(self):
		if not self.en_Am:
			if 	self.emisora_AM<=1300
				self.emisora_AM=300
			elif:
