import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-school-work-program",
    description="Meta package for open-synergy-ssi-school-work-program Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_school_work_program',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
