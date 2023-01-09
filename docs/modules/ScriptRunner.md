# ScriptRunner

This task is used to run scripts. See the [Script documentation](docs/models/Script.md) for more
information about which languages are supported and how they are run.

## Example

```json
{
  "name": "Hello World",
  "type": "ScriptRunner",
  "script": {
    "script": "echo 'Hello World!'",
    "lang": "bash",
    "interactive": false
  },
  "depends_on": []
}
```

## Properties

| Property   | Type     | Description                                           | Required | Default |
|:-----------|:---------|:------------------------------------------------------|:---------|:--------|
| name       | string   | The name of the task.                               | Yes      |         |
| type       | string   | The type of the task.                               | Yes      |         |
| script     | Script   | The script to run.                                    | Yes      |         |
| depends_on | string[] | The names of the tasks that this task depends on. | No       | []      |
