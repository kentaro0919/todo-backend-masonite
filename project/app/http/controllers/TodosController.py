""" A TodosController Module """
from masonite.request import Request
from app.Todo import Todo
from urllib.parse import urljoin


class TodosController:
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def index(self):
        """Get /
        """
        return Todo.all()

    def create(self):
        """Post /
        'title', 'completed', 'url', 'order'
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
        todo = Todo.find(request.param("id"))
        todo.title = self.request.input("title")
        todo.completed = self.request.input("completed")
        todo.order = self.request.input("order")
        todo.save()

        return todo

    def deleteAll(self):
        """Delete all existing resource listing
        ex. Delete().route("/destroy", {{ class }})
        """

        for i in Todo.all():
            i.delete()

        return Todo.all()

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", {{ class }}
        """
        try:
            todo = Todo.find_or_fail(self.request.param("id"))
            return todo
        except:
            return []

    def delete(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", {{ class }})
        """

        try:
            Todo.find_or_fail(self.request.param("id")).delete()
            return []
        except:
            return []
