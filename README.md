# Evernote helper:
Helps to interact with your notes and notebooks.

### How to execute:

- Download or clone [repo](https://github.com/Ash2803/evernote-example)
- You must have Python 2.7 installed;
- Create the virtual environment using command:
```
virtualenv --python=path/to/python2.7 evernote-env
```
- Install the requirements using command:
```
pip install -r requirements.txt
``` 

Create `.env` and setup next variables
```
EVERNOTE_CONSUMER_KEY
EVERNOTE_CONSUMER_SECRET
EVERNOTE_PERSONAL_TOKEN
JOURNAL_TEMPLATE_NOTE_GUID
JOURNAL_NOTEBOOK_GUID
INBOX_NOTEBOOK_GUID
SANDBOX=False
```
- `EVERNOTE_CONSUMER_KEY` and `EVERNOTE_CONSUMER_SECRET`  you can get [here](https://dev.evernote.com/#apikey);
- `EVERNOTE_PERSONAL_TOKEN` you can get [here](https://sandbox.evernote.com/api/DeveloperToken.action),
you need to create an account.
- `JOURNAL_NOTEBOOK_GUID` - any notebook, you can create in your sandbox;
- `JOURNAL_TEMPLATE_NOTE_GUID` - can be referred to `JOURNAL_NOTEBOOK_GUID`;
- `INBOX_NOTEBOOK_GUID` - default notebook;

## list_notebooks.py
Returns list of notebooks in string format:
```
{notebook.guid} - {notebook.name}
```

## dump_inbox.py
Parse notes from notebook.

### def get_notebook_list()
Return notes from notebook, default quantity of returning notes set to 10.

## add_note_to_journal.py
Adds new note with date based on other note GUID.
You need to set `JOURNAL_TEMPLATE_NOTE_GUID` and `JOURNAL_NOTEBOOK_GUID` values.
- To execute run:
```
python add_note_to_journal.py "YYYY-MM-DD"
```
Returns
```
Title Context is:
{
    "date": "2022-01-17", 
    "dow": "понедельник"
}
Note created: {note_title}
Done
```


This code review was done for educational purposes at online-course for web-developers [dvmn.org](https://dvmn.org/)
