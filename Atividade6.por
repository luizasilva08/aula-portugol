programa {
  funcao inicio() {
    real nota1, nota2, nota3, media

    escreva("Digite a primeira nota: ")
    leia(nota1)

    escreva("Digite a segunda nota: ")
    leia(nota2)

    escreva("Digite a terceira nota: ")
    leia(nota3)

    media = (nota1 + nota2 + nota3) / 3

    escreva("A média das 3 notas foi: ", media)

    se (media>=7 e media<=10)
    {escreva("\nAprovado!")}

    senao se (media<7 e media>5)
    {escreva("\nExame")}

    senao se (media<6)
    {escreva("\nReprovado")}

    senao
    {escreva("\nMédia inválida")}
    
  }
}
