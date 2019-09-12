## The Document object

Pycaprio uses the `Annotation` object to model INCEpTION's documents, and has these properties:

* `project_id`: Id of the project in which the annotated document is located.
* `document_id`: Id of the annotated document.
* `user_name`: Annotator's username.
* `annotation_state`: State in which the annotation is in.
* `timestamp`: Annotation's creation date.


### List annotations
Lists all the annotations in an INCEpTION's document.

Example:
```python
annotations = client.api.annotations(1, 4) # Annotations in document #4 in project #1
print(annotations) # [<Annotation by test-user (Project: 1, Document: 4)>, <Annotation by leonardo-dicaprio (Project: 1, Document: 4)>]
```

### Download annotation
Downloads a document's annotation content.

Example: 

```python
annotation_content = client.api.annotation(1, 4, 'test-user') # Downloads test-user's annotations on document 4 on project 1

with open("downloaded_annotation", 'wb') as annotation_file:
    annotation_file.write(annotation_content)
```

### Upload document
Uploads a document to a project in INCEpTION. It needs the Id of the project, the name of the document and the content of it (io stream).
You can specify the document's format via `document_format` (defaults to `webanno`).
You can specify the document's state via `state` (defaults to `NEW`).
 
Example:

```python
from pycaprio.core.mappings import DocumentFormats, DocumentStatus
with open("document") as document_file:
    new_document = client.api.create_document(1, "Test document name", document_file, document_format=DocumentFormats.WEBANNO, state=DocumentStatus.IN_PROGRESS)
print(new_document) # <Document #5: Test document name (Project: 1)>
```

### Delete document
Deletes a document from a project.

Example:

```python
client.api.delete_document(1, 4) # Deletes document #4 from project #1
```
