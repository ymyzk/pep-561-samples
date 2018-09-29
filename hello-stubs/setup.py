from setuptools import setup


setup(
    name="hello-stubs",
    version="0.0.1",
    packages=["hello-stubs"],
    package_data={
        "hello-stubs": ["*.pyi"],
    },
    install_requires=[
        "hello==0.0.1",
    ],
)
