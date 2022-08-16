
<h1 align="center"> Programação Orientada a Objetos </h1>

<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/92533013/184757634-89de0ae8-5904-463a-95ce-2313e9dda979.png" />
</p>




## Por que usar Python orientado a objetos?

Com o Python sendo uma linguagem multiparadigma, por que escolheriamos especificamente proramar em POO?

- Reutilização de código.

- É de fácil legibilidade.

- Muito utilizado para códigos compartilhados e grandes projetos.

- Não é necessário se prender exclusivamente em POO, você pode usar procedural ou funcional complementando seu código.

## Diferenças entre Python e Java

O Python, muito diferente do java não se prende a tipos, o que acelera o objetivo, na maioria das vezes.
Também existe uma infinidade de bibliotecas, o que torna o python ainda mais simples, e, muitas vezes, abstraindo o programador de grande parte da lógica.


## Sintaxe
### ~~Peço perdão pois gosto de usar ponto e vírgula em Python~~
#### Declaração da classe e atributos

```
class Cachorro:
  def __init__(self, nome, raca, idade):
      self.nome = nome;
      self._raca = raca;
      self.__idade = idade;
 ```
Acima nos declaramos a classe cachorro e seu construtor.

Também pode ser notado que declaramos seus atributos dentro do construtor utilizando o "self", que é o equivalente do "this" do Java.

Os underscoree em atributos do Python servem para determinar os modificadores de acesso, onde:
- Sem underscore significa public.
- 1 underscore significa protected.
- 2 underscores significa private.


### Métodos

```
def latir(self):
  print("woof");
```

### Instancia
```
cachorro1 = Cachorro("Dogson", "yorkshire", 5);
```

### Acesso
```
print(cachorro1.nome);
cachorro.latir(self);
```

### Getters e Setters

```
@property
def nome(self):
  return self._nome;
```
o property indica que o método é um getter

```
@nome.setter
def nome(self, nome):
  self.nome = nome;
```
o nome.setter está definindo um setter para o nome.

## Exemplo

Aqui eu trago dois simples códigos, um escrito em Python procedural, o outro, orientado a objetos, ambos baseados no jogo "Pedra, papel e tesoura".

A intenção nessa comparação não é mostrar a superioridade de uma ou outra, mas sim mostrar as diferenças.

Esse também não é um uso onde o POO se destaque, foi feito exclusivamente a fins didáticos e não explora 1% das possibilidades da orientação a objetos.

- [Procedural](https://github.com/elc117/t5-2022a-lchesani-oop-python/tree/main/Procedural)

- [POO](https://github.com/elc117/t5-2022a-lchesani-oop-python/tree/main/POO)

## Conclusão

Nota-se que a utilização em POO funciona muito bem quanto a organização, mesmo em um programa tão pequeno, em projetos maiores a diferença é ainda maior, visto que o mesmo código é utilizado por vários desenvolvedores.

Também é válido apontar como o código em POO é extremamente mútavel, sendo bem menos sucetível a problemas caso modificações sejam feitas.


## Referências

[Python vs Java in OOP](https://realpython.com/oop-in-python-vs-java/)

[POO em Python](https://www.treinaweb.com.br/blog/orientacao-a-objetos-em-python)

[O que são objetos e como instanciá-los](https://www.youtube.com/watch?v=2noSw2TWZao)

