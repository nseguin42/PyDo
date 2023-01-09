# PyDo

A flexible script for doing tasks with dependencies.

Currently in pre-pre-alpha. Probably doesn't work without some bandaid fixes. Everything will change
without notice.

## Requirements

- Python 3.11+
- Pipenv

## Usage

- `pipenv update` to setup a virtual environment with the required packages.
- `pipenv run python pydo/main.py` to run the script. Pass `--help` to see all options.

## Configuration

All configuration is done through .json files in the config directory `$CONFIG` (
default: `$CONFIG = pydo/settings`).

### Modules

Each task that PyDo can run is a module. Modules are defined in the `$CONFIG/modules` directory.
Each module is defined by a single .json file with the minimum syntax:

| Property | Type   | Description             | Required | Default |
|:---------|:-------|:------------------------|:---------|:--------|
| name     | string | The name of the module. | Yes      |         |
| type     | string | The type of the module. | Yes      |         |

```json
{
    "name": "module_name",
    "type": "module_type"
}
```

Other properties may be required depending on the module type. See
the [module documentation](docs/modules/Modules.md) for more information.
