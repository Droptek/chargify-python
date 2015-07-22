from setuptools import setup


setup(
    name='chargify-python',
    version='0.1',
    url='http://github.com/hindsightlabs/chargify-python',
    license='MIT',
    author='Steven Wei',
    author_email='steve@hindsightlabs.com',
    description='A Chargify API client written in Python.',
    long_description=open("README.md").read(),
    py_modules=['chargify'],
    zip_safe=False,
    platforms='any',
    test_suite='test_chargify.suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
