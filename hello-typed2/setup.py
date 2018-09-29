from setuptools import setup


setup(
    name="hello-typed2",
    version="0.0.1",
    packages=["hello"],
    package_data={
        "hello": ["py.typed", "*.pyi"],
    },
)
