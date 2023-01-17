import os

from dotenv import load_dotenv

load_dotenv()


class Settings():

    EVERNOTE_CONSUMER_KEY = os.environ['EVERNOTE_CONSUMER_KEY']
    EVERNOTE_CONSUMER_SECRET = os.environ['EVERNOTE_CONSUMER_SECRET']
    EVERNOTE_PERSONAL_TOKEN = os.environ['EVERNOTE_PERSONAL_TOKEN']
    JOURNAL_TEMPLATE_NOTE_GUID = os.environ['JOURNAL_TEMPLATE_NOTE_GUID']
    JOURNAL_NOTEBOOK_GUID = os.environ['JOURNAL_NOTEBOOK_GUID']
    INBOX_NOTEBOOK_GUID = os.environ['INBOX_NOTEBOOK_GUID']
    SANDBOX = os.environ["SANDBOX"]
