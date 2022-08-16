# Programação orientada a objetos

## Por que usar Python orientado a objetos?

Com o Python sendo uma linguagem multiparadigma, por que escolheriamos especificamente proramar em POO?

- Reutilização de código.

- É de fácil legibilidade.

- Muito utilizado para códigos compartilhados e grandes projetos.

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
## Referências

[Python vs Java in OOP](https://realpython.com/oop-in-python-vs-java/)

[POO em Python](https://www.treinaweb.com.br/blog/orientacao-a-objetos-em-python)

