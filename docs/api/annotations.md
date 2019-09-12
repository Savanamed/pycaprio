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
You can specify the annotation's format via `annotation_format` (defaults to `webanno`).

Example: 

```python
from pycaprio.core.mappings import DocumentFormats
annotation_content = client.api.annotation(1, 4, 'test-user', annotation_format=DocumentFormats.WEBANNO) # Downloads test-user's annotations on document 4 on project 1

with open("downloaded_annotation", 'wb') as annotation_file:
    annotation_file.write(annotation_content)
```

### Upload annotation
Uploads an annotation to a document in INCEpTION. It needs the Id of the project, the Id of the document, the annotator's username and the content of it (io stream).
You can specify the annotation's format via `annotation_format` (defaults to `webanno`).
You can specify the annotation's state via `annotation_state` (defaults to `NEW`).
 
Example:

```python
from pycaprio.core.mappings import DocumentFormats, AnnotationStatus
with open("annotation") as annotation_file:
    new_annotation = client.api.create_annotation(1, 4, 'leonardo-dicaprio', annotation_format=DocumentFormats.WEBANNO, annotation_state=AnnotationStatus.ANNOTATION_IN_PROGRESS)
print(new_annotation) # <Annotation by leonardo-dicaprio (Project: 1, Document: 4)>
```

### Delete annotation
Deletes a document from a project.

Example:

```python
client.api.delete_annotation(1, 4, 'leonardo-dicaprio') # Deletes annotation made by leonardo-dicaprio on document #4 from project #1
```
