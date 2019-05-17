#include <stdio.h>
#include <math.h>

int main(){
	int n = 4;
	float xp, yp, entradaEjemplo = 0, resultado = 0, valorUsuario = 0;
	float expSup = 0, expInf = 0, auxExpIf = 0, r = 0, b, a;
	float x[] = {2, 3, 2.5, 3.1};
	float y[] = {3, 4, 3, 6};

	for (int i=0; i<n; i++){
		xp += x[i];
		yp += y[i];
	}
	printf("Sumatorias:\n\t:X+: %.2f\n\t:Y+: %.2f\n", xp, yp);

	xp = xp/n;
	yp = yp/n;

	printf("\nLos Prima:\n\t:Xp: %.2f\n\t:Yp: %.2f\n", xp, yp);

	for (int i=0; i<n; i++){
		expSup += (x[i] - xp) * (y[i] - yp);    // Expresion Superior (expSup)
		expInf += pow((x[i] - xp), 2.0);				// Expresion Inferior (expInf)
		auxExpIf += pow((y[i] - yp), 2.0);
	}

	b = expSup / expInf;
	printf("\n b = %.2f",b);

	a = yp - (b * xp);
	printf("\n a = %.2f",a);

	r = expSup / sqrt(expInf * auxExpIf);

	printf("\n R = %.2f", r);

	printf("\n---------------------------------------\n");

	//do{
	//printf("Ingrese: "); scanf("%f", &valorUsuario);
	//entradaEjemplo = 6;
	//resultado = a + (b * valorUsuario);
	//resultado = a + b * entradaEjemplo;
	//printf("resultado: %.4f", resultado);
	//}while(!(valorUsuario == 101.0));

	return 0;
}
