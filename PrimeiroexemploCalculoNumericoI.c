/*
 * gyhuijokpl.c
 * 
 * Copyright 2017 Laura Costa Pereira Miranda <lauracpm@laura>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

void decimais(){
	system("clear");
	int d,i,cont=0;
	float r,num,mult;
	printf("Conversao para binario de numeros decimais, digite o numero:\n");
	scanf("%f",&num);
	printf("Numero em binario:\n");
	printf("0.");
	for(i=0;i<100;i++){
		if(cont==0){
			mult=2*num;
			d= mult;
			r=mult-d;
			num=r;
			printf("%d",d);
			if(num==0){
				printf("\nConverge na %d interacao", i);
				cont++;
			}
		}
	}
}

void inteiros(){
	system("clear");
	int i, num, div, r,cont=0,v[100],j=0,s;
	printf("Conversao para binario de numeros inteiros, digite o numero:\n");
	scanf("%d",&num);
	for(i=0;i<100;i++){
		if(cont==0){
			div=num/2;
			r=num%2;
			num=div;
			if(num==0){
				cont++;
				printf("Converge na %d interacao", i);			
			}
			v[j]=r;
			j++;
		}
	}
	s=j;
	printf("\nNumero em binario:\n");
	for(j=s-1;j>=0;j--){
		printf("%d",v[j]);
	}
}




int main(int argc, char **argv)
{
	char opc;
	printf("Conversao para binario");
	printf("\nDigite a opcao:");
	printf("\nI - Inteiro\n");
	printf("D - Decimal\n");
	scanf("%c",&opc);
	opc=toupper(opc);
	if(opc=='I'){
		inteiros();
	}else{
		decimais();
	}



	return 0;
}

