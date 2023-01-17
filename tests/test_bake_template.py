import random
from chance import chance

license_stubs = {
    'Apache-2.0': 'Apache License',
    'BSD-3-Clause': 'BSD License',
    'GPL-3.0': 'GNU General Public License',
    'MIT': 'MIT License',
    'MPL-2.0': 'Mozilla Public License'
}


def test_bake_license(cookies):
    for license_id, license_stub in license_stubs.items():
        result = cookies.bake(extra_context={'license_id': license_id})

        if result.exception:
            print(result.exception)

        assert license_stub in result.project_path.joinpath('LICENSE').read_text()

        for key in license_stubs.keys():
            assert not result.project_path.joinpath(f'LICENSE.{key}').exists()


def test_bake_readme(cookies):
    license_id = chance.pickone([key for key in license_stubs.keys()])

    context = {
        'template_name': f'{chance.word().capitalize()} {chance.word().capitalize()}',
        'template_slug': chance.word(),
        'template_description': chance.sentence(),
        'author_email': chance.email(),
        'license_id': license_id,
        'license_fullname': chance.name(),
        'license_year': random.randint(2000, 2022),
        'github_user': chance.name()
    }

    result = cookies.bake(extra_context=context)

    readme = result.project_path.joinpath('README.md').read_text()

    assert context['template_name'] in readme
    assert context['template_description'] in readme
    assert f'https://github.com/{context["github_user"]}/{context["template_slug"]}' in readme

    assert license_stubs[license_id] in readme
    assert f'Copyright (C) {context["license_year"]} {context["license_fullname"]} <{context["author_email"]}>' in readme
