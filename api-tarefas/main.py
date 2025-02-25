from flask import Flask, request

app= Flask(__name__)

tarefas = [
    {
        "id":1,
        "titulo":"Estudar Javascript",
        "descrição": "Estudar Javascript para aprender a construir apps",
        "status": "em andamento",
        "Comentários":"Esse é muito legal de fazer, e eu estou gostando muito",
        "DatadeInicio":"28/1/2024",
        "PrevisãodeTermino":"12/12/2025"
    },
    {
      "id":2,
      "titulo": "estudar Flask",
      "descrição":"Estudar Flask para aprender sobre web services",
      "status": "não iniciado",
        "Comentários":"Esse é dificil mas acho que vou conseguir terminar na data prevista",
        "DatadeInicio":"27/6/2024",
        "PrevisãodeTermino":"15/12/2026"

    }
]

@app.route ('/')
def index():
    return 'Olá User'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route ("/tasks/<int:task_id>", methods = ['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas :
        if tarefa.get('id') == task_id :
            return tarefa
    return'tarefa não encontrada'
@app.route( '/tasks', methods = ['POST'])
def create_task():
    task = request.json
    ultimo_id= tarefas[-1].get('id')+1
    task['id'] =ultimo_id
    tarefas.append(task)
    return task
@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['status'] = task_body.get('status')
    task_search['descrição'] = task_body.get('descrição')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tarefas
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return {"mensagem": f"Tarefa com ID {task_id} foi excluída com sucesso."}, 200

    return {"erro": "Tarefa não encontrada."}, 404

if __name__ == '__main__':
    app.run(debug=True)