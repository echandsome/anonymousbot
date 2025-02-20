import setuptools


setuptools.setup(

    name="anonymousbot",
    version="1",

    license="AGPL-3.0",

    author="echandsome",
    author_email="anonymous",

    install_requires=[
        "python-telegram-bot==21.4",
        "Pyyaml",
        "aiosqlite"
    ],

    packages=[
        "anonymousbot",
    ],

    entry_points={
        "console_scripts": [
            "anonymousbot = anonymousbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
