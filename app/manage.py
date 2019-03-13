from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import , db


manager = Manager(run)  
migrate = Migrate(run, db)

 
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()