from abc import ABC, abstractmethod

# classe pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def matricula(self):
        return self.__matricula

    @abstractmethod
    def exibir_detalhes(self):
        pass


# usuario comum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.__livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.__livros_emprestados) < 3 and livro.disponivel:
            self.__livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} não pode emprestar mais livros.")

    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} indisponivel '{livro.titulo}'.")

    def exibir_detalhes(self):
        print(f"Usuário: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")
        print(f"Livros emprestados: {[livro.titulo for livro in self.__livros_emprestados]}")

class Administrador(Pessoa):
    def exibir_detalhes(self):
        print(f"Administrador: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

    def cadastrar_livro(self, titulo, autor, ano):
        return Livro(titulo, autor, ano)


class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @abstractmethod
    def exibir_detalhes(self):
        pass

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor)
        self.__ano = ano
        self.__disponivel = True

    @property
    def ano(self):
        return self.__ano

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self.__disponivel = valor

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}")


# Sistema de Biblioteca
class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def exibir_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.__livros:
            if livro.disponivel:
                livro.exibir_detalhes()

    def exibir_usuarios_com_livros(self):
        print("Usuários com livros emprestados:")
        for usuario in self.__usuarios:
            if isinstance(usuario, UsuarioComum):
                usuario.exibir_detalhes()


# Exemplo de uso
if __name__ == "__main__":
    # Criando a biblioteca
    biblioteca = Biblioteca()

    # Criando um administrador
    admin = Administrador("Leonardo", 20, "A054")

    # Cadastrando livros
    livro1 = admin.cadastrar_livro("Harry Potter", "leonardo vieira", 2020)
    livro2 = admin.cadastrar_livro("Ladrão de Raios", "Alice Vieira", 2018)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Criando um usuário comum
    usuario = UsuarioComum("Lucas", 22, "U023")
    biblioteca.adicionar_usuario(usuario)

    # Realizando empréstimos
    usuario.emprestar_livro(livro1)
    usuario.emprestar_livro(livro2)

    # Exibindo relatórios
    biblioteca.exibir_livros_disponiveis()
    biblioteca.exibir_usuarios_com_livros()

    # Devolvendo livro
    usuario.devolver_livro(livro1)

    # Exibindo relatórios atualizados
    biblioteca.exibir_livros_disponiveis()
    biblioteca.exibir_usuarios_com_livros()
