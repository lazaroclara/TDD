# gerenciador_tarefas.py

class GerenciadorDeTarefas:

    def __init__(self):
        self.tarefas = []
        self._proximo_id = 1

    def _encontrar_tarefa_por_id(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa['id'] == tarefa_id:
                return tarefa
        return None

    def adicionar_tarefa(self, nome, descricao):
        [cite_start]
        if not nome or not nome.strip():
            raise ValueError("O nome da tarefa não pode ser vazio.")

        nova_tarefa = {
            'id': self._proximo_id,
            'nome': nome,
            'descricao': descricao,
            'status': 'em andamento'
        }
        self.tarefas.append(nova_tarefa)
        self._proximo_id += 1
        return nova_tarefa

    def marcar_como_concluida(self, tarefa_id):
        [cite_start]
        tarefa = self._encontrar_tarefa_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada.")

        if tarefa['status'] == 'concluída':
            return False  # Nenhuma alteração, já está concluída

        tarefa['status'] = 'concluída'
        return True

    def marcar_como_em_andamento(self, tarefa_id):
        [cite_start]
        tarefa = self._encontrar_tarefa_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada.")
        
        if tarefa['status'] == 'concluída':
             raise PermissionError("Não é possível marcar uma tarefa concluída como 'em andamento'.")

        tarefa['status'] = 'em andamento'
        return True

    def editar_tarefa(self, tarefa_id, novo_nome, nova_descricao):
        [cite_start]
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O novo nome da tarefa não pode ser vazio.")

        tarefa = self._encontrar_tarefa_por_id(tarefa_id)
        if not tarefa:
            raise ValueError("Tarefa não encontrada para edição.")

        tarefa['nome'] = novo_nome
        tarefa['descricao'] = nova_descricao
        return True

    def excluir_tarefa(self, tarefa_id):
        [cite_start]
        tarefa = self._encontrar_tarefa_por_id(tarefa_id)
        if not tarefa:
             raise ValueError("Tarefa não encontrada para exclusão.")
        
        self.tarefas.remove(tarefa)
        return True