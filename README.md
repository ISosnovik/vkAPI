# VK API

This is an ultimate library for **vk.com** API written in Python.

## Installation
Just: 
```bash
git clone https://github.com/ISosnovik/vkAPI
cd vkAPI
python setup.py install
```

## General use

To begin with:

```python
from vkapi.methods import *
```

You can use it exactly as it is described [here](https://vk.com/dev/methods).
For example:

```python
users.get(user_ids=1, fields='city')
#[{'city': 2, 'first_name': 'Pavel', 'last_name': 'Durov', 'uid': 1}]
```

## Access Token

Some methods use `access_token`. It shouldn't be passed as a parameter to method. Nevertheless, it is defined as a class property `token` in `vkapi.vkapi.AccessToken` class. Just set it at the beginnig:
 
```python
from vkapi.methods import *
from vkapi import AccessToken

AccessToken.token = 'h3r3-1s-th3-4cc3ss-t0k3n'
account.getInfo(fields='country')
```
And that is it.

## Documentation

All methods are provided with short description and reference to the official documentation. If you forget something, just call `help` or `shift + tab + tab` for *__Jupyter Notebook__* and you will get the description:

```profile
Help on function resolveScreenName in module vkapi.methods.utils:

resolveScreenName(screen_name=None)
    Detects a type of object (e.g., user, community, application)
    and its ID by screen name.
    https://vk.com/dev/utils.resolveScreenName
```

## Examples
There are several [examples](https://github.com/ISosnovik/vkAPI/tree/master/examples) of use of *__vkapi__*.

+ [Public Methods](https://github.com/ISosnovik/vkAPI/blob/master/examples/Public%20methods.ipynb)
+ [Getting a Token](https://github.com/ISosnovik/vkAPI/blob/master/examples/Getting%20a%20token.ipynb)
+ [Private Methods](https://github.com/ISosnovik/vkAPI/blob/master/examples/Private%20methods.ipynb)
+ [Execute](https://github.com/ISosnovik/vkAPI/blob/master/examples/Execute.ipynb)

