package numeros;

import java.util.Scanner;

public class calculadora {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a=0,b=0,res=0;
		String sel = null;		
		try (Scanner tec = new Scanner(System.in)) {
			System.out.println("Selecione la opcion\n");
			System.out.println("+ suma"
					+ "\n-: Resta"
			        +"\n*: Multiplicacion"
			        +"\n/*: Division");
			sel=tec.next();
			switch (sel){
			case "+":
				System.out.println("ha seleccionado suma\n");
				System.out.println("ingrese el primer número");
				a=tec.nextInt();
				System.out.println("ingrese el segundo número");
				b=tec.nextInt();
				res=a+b;
				System.out.println(a+"+"+b+"= "+ res);
				break;
				
				case "-":
				System.out.println("ha seleccionado Resta\n");
				System.out.println("ingrese el primer número");
				a=tec.nextInt();
				System.out.println("ingrese el segundo número");
				b=tec.nextInt();
				res=a-b;
				System.out.println(a+"-"+b+"="+ res);
				break;
				
				case "*":
					System.out.println("ha seleccionado Multiplicacion \n");
					System.out.println("ingrese el primer número");
					a=tec.nextInt();
					System.out.println("ingrese el segundo número");
					b=tec.nextInt();
					res=a*b;
					System.out.println(a+"*"+b+"="+ res);
					break;
					
					
				case "/":
					System.out.println("ha seleccionado Division \n");
					System.out.println("ingrese el primer número");
					a=tec.nextInt();
					System.out.println("ingrese el segundo número");
					b=tec.nextInt();
					res=a/b;
					System.out.println(a+"/"+b+"="+ res);
					break;
					
					default:
						System.out.println("Esa opcion no existe");
					
				
			
			

}
		}

    }
}
