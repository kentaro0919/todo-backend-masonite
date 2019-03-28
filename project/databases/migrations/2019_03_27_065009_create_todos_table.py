from orator.migrations import Migration


class CreateTodosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('todos') as table:
            table.increments('id')
            
            table.char('title', 256).nullable()
            table.boolean('completed').default(False)
            table.char('url', 256).nullable()
            table.integer('order').nullable()
            
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('todos')
