import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django_fieldsets_inlines-jat',
    version='0.1',
    author='Jat',
    author_email='jat@gmail.com',
    description='Mixin inlines and fieldsets in Django admin.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javware/django-fieldsets-inlines-jat",
    packages=['fieldsets_with_inlines'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.4'
)
