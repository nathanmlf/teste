programa
{
	
	funcao inicio()
	{
		//Atividade 5 – Troca de Valores entre Variáveis
		//Declare duas variáveis x = 5 e y = 10.
		//Troque os valores entre elas, de modo que x fique com 10 e y com 5.
		//Exiba os novos valores.

		inteiro x, y, inverter

		x = 5
		y = 10

		escreva("Início do programa\n", "\n")
		escreva("Valor inicial de x: ", x)
		escreva("\nValor inicial de y: ", y ,"\n")

		escreva("\nInversão\n")
		inverter = x
		x = y
		y = inverter

		escreva("\nResultado da Inversão", "\n")
		escreva("\nNovo valor de x: ", x)
		escreva("\nNovo valor de y: ", y)
		

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 425; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */