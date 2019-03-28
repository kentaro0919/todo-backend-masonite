""" A TodosController Module """
from masonite.request import Request
from app.Todo import Todo
from urllib.parse import urljoin


class TodosController:
    """Class TodosController
    """

    def __init__(self, request: Request):
        self.request = request

    def index(self):
        """Get / -> Todo.all()
        """
        return Todo.all()

    def create(self):
        """POST / -> new_todo
        
        """
        if self.request.input:
            print(self.request.input("title"))
            todo = Todo.create(
                order=self.request.input("order"),
                title=self.request.input("title"),
                completed=self.request.input("completed"),
            )
            todo.url = urljoin(
                "https://mysterious-thicket-31854.herokuapp.com",
                f"{self.request.path}{todo.id}",
            )

            todo.save()

        return todo

    def update(self, request: Request):
        """ /@id -> updated_todo
        """
        
        todo = Todo.find(request.param("id"))
        todo.title = self.request.input("title")
        todo.completed = self.request.input("completed")
        todo.order = self.request.input("order")
        todo.save()

        return todo

    def deleteAll(self):
        """Delete /  ->  Todo.all().delete()

        """

        for i in Todo.all():
            i.delete()

        return Todo.all()

    def show(self):
        """Get /@id -> todo
        """
        try:
            todo = Todo.find_or_fail(self.request.param("id"))
            return todo
        except:
            return []

    def delete(self):
        """Delete /@id ->  Todo.find().delete()
        """

        try:
            Todo.find_or_fail(self.request.param("id")).delete()
            return []
        except:
            return []
