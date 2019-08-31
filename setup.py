from setuptools import setup, find_packages

VERSION = {"VERSION": '1.0'}

setup(name='bert_ner',
      version=VERSION["VERSION"],
      description='bert_ner',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.6',
      ],
      license='Apache',
      packages=find_packages(exclude=["*.tests", "*.tests.*",
                                      "tests.*", "tests"]),
      install_requires=[
      ],
      include_package_data=True,
      python_requires='>=3.6.1',
      zip_safe=False)
