from setuptools import setup


setup(
    name="xmrto_wrapper",
    version="0.0.1",
    author="Norman Moeschter-Schenck",
    author_email="norman.moeschter@gmail.com",
    url="https://github.com/normoes/xmrto_wrapper",
    description=("Interact with XMR.to, create and track your orders."),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
    install_requires=["requests>=2.22.0"],
    py_modules=["xmrto_wrapper"],
)