from setuptools import setup

try:
  verstr = open('webui/_version.py', "rt").read()
except:
  raise RuntimeError("cannot read version file")

setup(
    # Application name:
    name="flask_puppet",

    # Version number (initial):
    version=verstr,

    # Application author details:
    author="Matt Cadorette",
    author_email="mattc@puppet.com",

    # Packages
    packages=["webui"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/ipcrm/flask_puppet",

    description="Example App",

    # Dependent packages (distributions)
    install_requires=[
      'Flask==0.10.1',
      'Flask-Testing==0.4.2',
      'itsdangerous==0.24',
      'Jinja2==2.8',
      'MarkupSafe==0.23',
      'Werkzeug==0.11.9',
    ],
)
