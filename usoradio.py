class radio():
	def __init__ (self,marca):
		self.marca=marca
		self.encendido=False
		self.en_FM=True
		self.emisora_AM=0
		self.emisora_FM=88.0
		self.volumen=0
	def encender(self):
		self.encendido=True	
	def apagar(self):
		self.encendido=False
	def subir_volumen(self):
		if self.volumen >= 100:
			self.volumen=100
		else:
			self.volumen+=5
	def bajar_volumen(self):
		if self.volumen <=0:
			self.volumen=0
		else:
			self.volumen-=5
				self.emisora_AM+40
	def subir_emisora(self):
		if not self.emisora_AM:
			if self.emisora_FM>=88.0:
				self.emisora_FM=107.5
			else:
				self.emisora_FM+.5
		else:
			if not emisora_FM:
				self.emisora_AM>=1300
				self.emisora_AM=300
			else:
				self.emisora_AM+40

	def bajar_emisora (self):
		if  self.emisora_AM<=1300:
			self.emisora_AM=300
		else:
			self.emisora_AM-40
		else:
			if not self.emisora_FM:
				self.emisora_FM<=107.5
				self..emisora_FM=88.0
			else:
				self.emisora_FM-.5


		
		



