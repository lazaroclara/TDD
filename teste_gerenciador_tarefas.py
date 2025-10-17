# test_gerenciador_tarefas.py

import unittest
from gerenciador_tarefas import GerenciadorDeTarefas

class TestGerenciadorDeTarefas(unittest.TestCase):
    
    def setUp(self):
        self.gerenciador = GerenciadorDeTarefas()

    def test_01_adicionar_tarefa_com_sucesso(self):
        tarefa = self.gerenciador.adicionar_tarefa("Estudar TDD", "Preparar para a atividade.")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.assertEqual(self.gerenciador.tarefas[0]['nome'], "Estudar TDD")
        self.assertEqual(tarefa['status'], 'em andamento')

    def test_02_adicionar_tarefa_sem_nome(self):
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("", "Descrição sem nome.")

    def test_03_marcar_tarefa_como_concluida(self):
        tarefa = self.gerenciador.adicionar_tarefa("Fazer café", "Usar o pó novo.")
        resultado = self.gerenciador.marcar_como_concluida(tarefa['id'])
        self.assertTrue(resultado)
        self.assertEqual(tarefa['status'], 'concluída')

    def test_04_marcar_tarefa_ja_concluida(self):
        tarefa = self.gerenciador.adicionar_tarefa("Ler um livro", "Capítulo 5.")
        self.gerenciador.marcar_como_concluida(tarefa['id'])
        resultado = self.gerenciador.marcar_como_concluida(tarefa['id'])
        self.assertFalse(resultado)
        self.assertEqual(tarefa['status'], 'concluída')

    def test_05_marcar_tarefa_como_em_andamento(self):
        tarefa = self.gerenciador.adicionar_tarefa("Planejar o dia", "Reuniões e pausas.")
        tarefa['status'] = 'pausada'
        self.gerenciador.marcar_como_em_andamento(tarefa['id'])
        self.assertEqual(tarefa['status'], 'em andamento')

    def test_06_marcar_concluida_como_em_andamento(self):
        tarefa = self.gerenciador.adicionar_tarefa("Enviar email", "Confirmar reunião.")
        self.gerenciador.marcar_como_concluida(tarefa['id'])
        with self.assertRaises(PermissionError):
            self.gerenciador.marcar_como_em_andamento(tarefa['id'])

    def test_07_editar_tarefa_existente(self):
        tarefa = self.gerenciador.adicionar_tarefa("Nome Antigo", "Descrição Antiga")
        self.gerenciador.editar_tarefa(tarefa['id'], "Nome Novo", "Descrição Nova")
        self.assertEqual(tarefa['nome'], "Nome Novo")
        self.assertEqual(tarefa['descricao'], "Descrição Nova")

    def test_08_editar_tarefa_inexistente(self):
        with self.assertRaises(ValueError):
            self.gerenciador.editar_tarefa(999, "Nome", "Descrição")

    def test_09_excluir_tarefa_com_sucesso(self):
        tarefa = self.gerenciador.adicionar_tarefa("Tarefa a ser excluída", "...")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.gerenciador.excluir_tarefa(tarefa['id'])
        self.assertEqual(len(self.gerenciador.tarefas), 0)

    def test_10_excluir_tarefa_inexistente(self):
        with self.assertRaises(ValueError):
            self.gerenciador.excluir_tarefa(999)

if __name__ == '__main__':
    unittest.main(verbosity=2)