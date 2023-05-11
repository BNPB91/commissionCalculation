nombre = input("Bienvenido, cual es tu nombre? :");
monto = input("Cuanto es el monto que has logrado vender? :");

numb = float(monto);
comision = numb*(13/100);
redondeo = round(comision);

print (f"{nombre}!... El monto que te corresponde de acuerdo a la venta obtenida es de ${redondeo} (Equivalente al 13% de Comision)... ");
