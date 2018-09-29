# PEP 561 Sample Packages
This repository contains sample packages for demonstrating usage of PEP 561.

## Contents
### `hello`: Untyped (normal) package
```python
# hello/__init__.py
def say_hello(name):
    print(f"Hello, {name}")
```

### `hello-stubs`: Stub-only package for `hello`
```python
# hello-stubs/__init__.pyi
def say_hello(name: str) -> None: ...
```

### `hello-typed1`: Typed version of `hello` package (Type hints are written using annotations)
```python
# hello/__init__.py
def say_hello(name: str) -> None:
    print(f"Hello, {name}")
```

### `hello-typed2`: Typed version of `hello` package (Type hints are written as stub files)
```python
# hello/__init__.py
def say_hello(name):
    print(f"Hello, {name}")
```
```python
# hello/__init__.pyi
def say_hello(name: str) -> None: ...
```

### `sample.py`: A very simple program which uses `hello` package
```python
import hello

hello.say_hello("John")
hello.say_hello(12345)
```

## Demo
```shell
$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
Collecting mypy==0.630 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/32/8c/a668527fe2ea69f3a03fc4d895e12b6cb2eb1bb62d61cfe8ff4142395d3a/mypy-0.630-py3-none-any.whl
Collecting mypy-extensions==0.4.1 (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/4d/72/8d54e2b296631b9b14961d583e56e90d9d7fba8a240d5ce7f1113cc5e887/mypy_extensions-0.4.1-py2.py3-none-a
ny.whl
Collecting typed-ast==1.1.0 (from -r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/d3/08/80b868edff228089469b535add832567a7c79fb6971111ac6271bc3eb06d/typed_ast-1.1.0-cp37-cp37m-macosx_10
_9_x86_64.whl
Installing collected packages: typed-ast, mypy-extensions, mypy
Successfully installed mypy-0.630 mypy-extensions-0.4.1 typed-ast-1.1.0
```

### Untyped package
```shell
(venv) $ pip install ./hello
Processing ./hello
Installing collected packages: hello
  Running setup.py install for hello ... done
Successfully installed hello-0.0.1

(venv) $ mypy sample.py
sample.py:1: error: Cannot find module named 'hello'
sample.py:1: note: (Perhaps setting MYPYPATH or using the "--ignore-missing-imports" flag would help)
```

### Untyped package + stub-only packages
```shell
(venv) $ pip install ./hello-stubs
Processing ./hello-stubs
Installing collected packages: hello-stubs
  Running setup.py install for hello-stubs ... done
Successfully installed hello-stubs-0.0.1

(venv) $ mypy sample.py
sample.py:5: error: Argument 1 to "say_hello" has incompatible type "int"; expected "str"

(venv) $ pip uninstall -y hello hello-stubs
Uninstalling hello-0.0.1:
  Successfully uninstalled hello-0.0.1
Uninstalling hello-stubs-0.0.1:
  Successfully uninstalled hello-stubs-0.0.1
```

### Typed package using annotations
```shell
(venv) $ pip install ./hello-typed1
Processing ./hello-typed1
Installing collected packages: hello-typed1
  Running setup.py install for hello-typed1 ... done
Successfully installed hello-typed1-0.0.1

(venv) $ mypy sample.py
sample.py:5: error: Argument 1 to "say_hello" has incompatible type "int"; expected "str"

(venv) $ pip uninstall -y hello-typed1
Uninstalling hello-typed1-0.0.1:
  Successfully uninstalled hello-typed1-0.0.1
```

### Typed package using stub files
```shell
(venv) $ pip install ./hello-typed2
Processing ./hello-typed2
Installing collected packages: hello-typed2
  Running setup.py install for hello-typed2 ... done
Successfully installed hello-typed2-0.0.1

(venv) $ mypy sample.py
sample.py:5: error: Argument 1 to "say_hello" has incompatible type "int"; expected "str"

(venv) $ pip uninstall -y hello-typed2
Uninstalling hello-typed2-0.0.1:
  Successfully uninstalled hello-typed2-0.0.1
```

## License
This repository is licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed). See [LICENSE](LICENSE) also.

## Links
- [PEP 561 -- Distributing and Packaging Type Information](https://www.python.org/dev/peps/pep-0561/)
