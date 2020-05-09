## The Curation object

Pycaprio uses the `Curation` object to model INCEpTION's documents, and has the following properties:

* `project_id`: Id of the project in which the curated document is located (integer).
* `document_id`: Id of the annotated document (integer).
* `document_state`: Statues of the curated document (string).

### List curated documents
Lists all the curated documents in an INCEpTION project.

You can provide a `Project` instance instead of a `project_id` as well.
You can provide a `Document` instance instead of a `document_id` as well.

Example:
```python
documents = client.api.curations(1, document_state = 'CURATION-COMPLETE') # Finished curations in project #1
print(documents) # [<Document #4: file.xmi (Project: 1)>]
```

### Download curated annotations
Downloads a curated document's annotation content.

You can specify the annotation's format via `annotation_format` (defaults to `webanno`).

You can provide a `Project` instance instead of a `project_id` as well.
You can provide a `Document` instance instead of a `document_id` as well.

Example:

```python
from pycaprio.mappings import InceptionFormat
# In case you want a specific curated document
curated annotation_content = client.api.curation(1, 4, annotation_format=InceptionFormat.WEBANNO) # Downloads test-user's annotations from document 4 of project 1
with open("downloaded_annotation", 'wb') as annotation_file:
    annotation_file.write(annotation_content)

```
or...

```python
# To download all curated documents, in case not all document have been curated (will cause error), you need to select the ones that have a document_state associated with curation:
from pycaprio.core.mappings import InceptionFormat, DocumentState
curation = []
for document in documents:
    if document.document_state in DocumentState.CURATION_IN_PROGRESS:
        curated content = client.api.curation(1, 4, annotation_format=InceptionFormat.WEBANNO)
        curations.append(curated content)
        for curation in curations:
            z = zipfile.ZipFile(io.BytesIO(curation))
            z.extractall('/your/path/')
```


### Upload curation
Uploads a curated document in INCEpTION. It requires the Id of the project, the Id of the document, the annotator's username and the annotation's content (io stream).

You can specify the annotation's format via `annotation_format` (defaults to `webanno`) and its state via `annotation_state` (defaults to `NEW`).

You can specify the document's state via `document_state`.
You can provide a `Project` instance instead of a `project_id` as well.
You can provide a `Document` instance instead of a `document_id` as well.
You can specify `content` which is the flat xmi file in byte format:

 ```python
from pycaprio.mappings import InceptionFormat
annotation_content = client.api.annotation(1, 4, 'test-user', annotation_format=InceptionFormat.WEBANNO)
z = zipfile.ZipFile(io.BytesIO(annotations))
z.extractall('/path/to/folder')
with open('/path/to/folder/file.xmi', 'rb') as f:
    xmi = f.read()
```

Example:

```python
from pycaprio.mappings import InceptionFormat
client.api.create_curation(1, 4, annotation_format = InceptionFormat.XMI, content = xmi, document_state = 'CURATION-IN-PROGRESS') # {"messages":[],"body":{"user":"CURATION_USER","state":"COMPLETE","timestamp":"2020-04-05T17:08:03+0000"}}
```


### Delete curations
Deletes an curation from a project.

You can provide a `Project` instance instead of a `project_id` as well.
You can provide a `Document` instance instead of a `document_id` as well.


Example:

```python
client.api.delete_curation(1,4) # Deletes curated document #4 from project #1
```

