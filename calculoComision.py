nombre = input("Bienvenido, cual es tu nombre? :");
monto = input("Cuanto es el monto que has logrado vender? :");

numb = float(monto);
comision = numb*(13/100);
redondeo = round(comision);

print (f"{nombre} y monto que te corresponde por venta la comision es (13%) equivalente a {redondeo}... ");

