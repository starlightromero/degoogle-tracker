from flask_login import UserMixin, current_user
from degoogle_app import db, login_manager, bcrypt


@login_manager.user_loader
def load_user(user_id):
    """Get current logged in user."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """User model."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=True, unique=True)

    def __repr__(self):
        """User returns username."""
        return f"User('{self.username}')"

    def set_password(self, password):
        """Set user's password as hash."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Check if given password matches hashed password."""
        return bcrypt.check_password_hash(self.password, password)


class Google(db.Model):
    """Google model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="google")

    def __repr__(self):
        """Google returns name."""
        return self.name


class Alternative(db.Model):
    """Alternative model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    google_id = db.Column(db.Integer, db.ForeignKey("google.id"))
    google = db.relationship("Google", backref="alternative", uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="alternative")

    def __repr__(self):
        """Alternative returns name."""
        return self.name
