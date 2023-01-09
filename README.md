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

### Tasks

Each task that PyDo can run is a task. Tasks are defined in the `$CONFIG/tasks` directory.
Each task is defined by a single .json file with the minimum syntax:

| Property | Type   | Description             | Required | Default |
|:---------|:-------|:------------------------|:---------|:--------|
| name     | string | The name of the task. | Yes      |         |
| type     | string | The type of the task. | Yes      |         |

```json
{
    "name": "task_name",
    "type": "task_type"
}
```

Other properties may be required depending on the task type. See
the [task documentation](docs/tasks/Tasks.md) for more information.
