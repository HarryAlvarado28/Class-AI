#Esta version del codigo, no es posible ejecutarla directamente en la Pi en este momento ya que
#no se ha instalado el X sobre esta para ejecutar aplicaciones graficas.
#Este proyecto se puede ejecutar sobre un pc directamente para probarlos

from SimpleCV import *   # Importamos liberias para el control de la Camara
import time 			# Importamos librerias para el control de tiempo

display = SimpleCV.Display() # Iniciamos objeto de la clase que desplegara un Display en pantalla
cam = SimpleCV.Camera(1)    # Seleccionamos el dispositivo que ha sido habilitado para la camara
normaldisplay = True  # Variable que inicia el sistema con el display en modo normal

# Se trae las opciones de la camara
#print "Propiedades de la camara:", cam.getAllProperties()

# Se valida la existencia de un display y se procesa la imagen
while display.isNotDone():
	# Confirma si se presiona o no el clic derecho y aplica el cambio de display a la version segmentada
	if display.mouseRight:
		normaldisplay = not(normaldisplay)
		print "Display Mode:", "Normal" if normaldisplay else "Segmented"
		# Toma una captura de la camara
	img = cam.getImage().flipHorizontal()
	#Selecciona el color predominante "Negro para este caso"
	dist = img.colorDistance(SimpleCV.Color.WHITE).dilate(2)
	# Dentro de la escala de grises, selecciona los mas altos "Oscuros"
	segmented = dist.stretch(215,230)
	# Busca los blobs disponibles sobre la segmentacion
	blobs = segmented.findBlobs()
	if blobs:
		# Si encuentra blobs, saca los que son circulos  con una calibracion
		circles = blobs.filter([b.isCircle(0.35) for b in blobs])
		if circles:
			# Pinta en pantalla un circulo al rededor del que se ha encontrado previamente
			# Imprime las cordenadas del objeto en pantalla
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.RED,2)
			print "X:",circles[-1].x , "Y:", circles[-1].y, "Radio:", circles[-1].radius()
	if normaldisplay:
		img.show()
	else:
		segmented.show()