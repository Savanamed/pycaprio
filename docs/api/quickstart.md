## Requirements
For `pycaprio` to be able to access the API, you will need the API to be activated and have a user with
the `ROLE_REMOTE` role assigned. You can find more on how to achieve this [here](https://inception-project.github.io//releases/0.11.2/docs/admin-guide.html#sect_remote_api).

## Creating the pycaprio client

The `pycaprio` client needs the inception host and the username and the password of the remote user you want to use.


You can specify these information either by environmental variables or by explicitly passing the values as arguments to the client:

### Environmental variables (preferred way)
```
export INCEPTION_HOST=http://your-inception-host.com
export INCEPTION_USERNAME=remote-user
export INCEPTION_PASSWORD=password
```
And then in your python code:

```python
from pycaprio import Pycaprio
client = Pycaprio()
```

### Passing the values as parameters
```python
from pycaprio import Pycaprio
client = Pycaprio("http://your-inception-host.com", authentication=("remote-user", "password"))
```
