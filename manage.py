from flask.ext.script import Manager, prompt_bool
from beckton import app
from mongoengine import connect
from celery.task.control import discard_all as celery_discard_all


manager = Manager(app)

@manager.command
def reset():
    "Delete all data, reset everything"
    if prompt_bool("Are you absolutely certain you want to delete all this things?"):

      #reset mongo
      mongo_settings =  app.config['MONGODB_SETTINGS']
      db = connect(mongo_settings['DB'])
      db.drop_database(mongo_settings['DB'])
      print("Deleted all collections from database ...")

      #reset celery
      celery_discard_all()
      print("Deleted all pending tasks from the message que ...")

      print("Done")


if __name__ == "__main__":
    manager.run()