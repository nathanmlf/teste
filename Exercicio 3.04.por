programa {
    funcao inicio() 
    {
        real notaFinal

        escreva("Aluno, informe a sua nota final: ")
        leia(notaFinal)

        se (notaFinal >= 7) 
        {
            escreva("Você foi aprovado, boas férias!!")
        }
        senao 
        {
            se (notaFinal >= 5) 
            {
                se (notaFinal <= 6.9) 
                {
                    escreva("Infelizmente, você está de recuperação.")
                }
            }
            senao 
            {
                escreva("Sentimos muito, você foi reprovado.")
            }
        }
    }
}

//Peça ao usuário sua nota final.
//Se a nota for maior ou igual a 7, exiba "Aprovado".
//Se for entre 5 e 6.9, exiba "Recuperação".
//Se for menor que 5, exiba "Reprovado".