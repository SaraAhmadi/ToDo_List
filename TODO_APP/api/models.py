from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    password = db.Column(db.String(60),nullable=False)
    todo = db.relationship('Todo', backref='author')
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password":self.password,
            "todo": self.todo,
        }
    
    def get_id(self):
       return (self.id)
  
    def __repr__(self):
        return '<User %r>' % self.username
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)    
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))    
    status =db.Column(db.String, default="To do")    
    due_date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "title":self.title,
            "description": self.description,
            "author": self.author,
            "status": self.status,
            "due_date": str(self.due_date.strftime('%d-%m-%Y'))
        }
