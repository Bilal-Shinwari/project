from FlaskApp import app, db

print("Creating the database...")
with app.app_context():
    db.create_all()
print("Database created successfully.")
