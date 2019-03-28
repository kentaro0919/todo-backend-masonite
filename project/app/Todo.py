"""Todo Model"""

from config.database import Model
from orator.orm import  accessor

class Todo(Model):
    """Todo Model"""
    __fillable__ = ['title', 'completed', 'url', 'order']
    
    @accessor
    def completed(self):
        """self.completed -> True or False
        """
        completed = self.get_raw_attribute('completed')
        return False if completed == 0 else True


