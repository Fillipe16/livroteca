import unittest
from LivroDAO import LivroDAO

class LivroDAOTest(unittest.TestCase):

    livroDAO = LivroDAO()

    def test_deveriaRetornarLivroQuandoIdForValido(self):

        id = 1

        livroValido = LivroDAOTest.livroDAO.buscarPorId(id)


        self.assertEqual(id, livroValido.getId())

    def test_naoDeveriaRetornarLivroQuandoIdForInvalido(self):

        id = 5

        livroInvalido = LivroDAOTest.livroDAO.buscarPorId(id)

        self.assertFalse(livroInvalido)
    
unittest.main()