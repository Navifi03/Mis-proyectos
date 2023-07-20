package org.educacionit;

import java.util.Scanner;

public class program {

	public static void main(String[] args) {
		System.out.println("Hola Mundo");
		
		// EJEMPLO 1 TIpos de datos primitivos :*//
		int i =20;
		System.out.println("el valor de i es "+i);
           // EJEMPLO 2 TIpos de datos objeto  :
		//scanner in = new scanner(sytem.in);
		//EJEMPLO 3 TIpos de datos objeto especias (string)
		//string hm ="HolaMundo";
		//// es lo mismo que hacer string hm =new strting ("Hola Mundo")
		//EJEMPLO 4
		Scanner in =new Scanner (System.in);
		System.out.println("ingrese su nombre");
		String nombre = in.nextLine();
		System.out.println("ingrese su apellido");
		String apellido = in.nextLine();
		System.out.println("ingrese su edad");
		String edad = in.nextLine();
		System.out.println("Hola" + nombre +" "+ apellido +" de "+ edad +"años");
		in.close();
		//Ejemplo 5 - Mas Orientado a objetos/*
				//Scanner int1 = new Scanner(System.in);/*
				//persona pers = new persona();
				//System.out.println("Ingrese su nombre:");
				//pers.nombre = int1.nextLine();
				
				//System.out.println("Ingrese su apellido:");
				//pers.apellido = in.nextLine();
				//
				//System.out.println("Ingrese su edad:");
				//pers.edad = int1.nextInt();
				
			//System.out.println("Hola " + pers.nombre + " " + pers.apellido +" de " + pers.edad + " años");/*
		
	         //Ejemplo 6- para bien el tema de las referencias 
			//	pers.nombre = "Juan";
				//persona persAux = pers;
				//persAux.nombre = "Pedro";
				//System.out.println(pers.nombre);
				
			
		
	}
}
