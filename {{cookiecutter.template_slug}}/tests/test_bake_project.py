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

        assert license_stub in result.project_path.joinpath('LICENSE').read_text()

        for key in license_stubs.keys():
            assert not result.project_path.joinpath(f'LICENSE.{key}').exists()
