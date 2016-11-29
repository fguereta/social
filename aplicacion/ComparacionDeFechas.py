# -*- coding: utf-8 *-* 
import datetime


def ComparacionDeFecha(desde,hasta,fecha):
	d=datetime.datetime.strptime(desde,'%d/%m/%Y').date()
	h=datetime.datetime.strptime(hasta,'%d/%m/%Y').date()
	f=datetime.datetime.strptime(fecha,'%d/%m/%Y').date()
	
	if f>=d and f<=h:
			
		return   True #Retorna True si la fecha se encuentra en el peorido
	else:
		return  False

