# PackageUpdater

This task is used to update packages. It is a wrapper around the ScriptRunner task.

## Example

```json
{
  "name": "Update Python",
  "type": "PackageUpdater",
  "script": {
    "script": "pacman -Syu python --noconfirm",
    "lang": "bash",
    "interactive": false
  },
  "get_installed_version_script": {
    "script": "pacman -Q python | cut -d ' ' -f 2",
    "lang": "bash",
    "interactive": false
  },
  "get_latest_version_script": {
    "script": "pacman -Si python | grep Version | cut -d ':' -f 2 | tr -d ' '",
    "lang": "bash",
    "interactive": false
  },
  "depends_on": []
}
```

## Properties

| Property                        | Type     | Description                                                    | Required | Default |
|:--------------------------------|:---------|:---------------------------------------------------------------|:---------|:--------|
| name                            | string   | The name of the task.                                          | Yes      |         |
| type                            | string   | The type of the task.                                          | Yes      |         |
| script                          | Script   | The script to run to update the package.                       | Yes      |         |
| get\_installed\_version\_script | Script   | The script to run to get the installed version of the package. | Yes      |         |
| get\_latest\_version\_script    | Script   | The script to run to get the latest version of the package.    | Yes      |         |
| depends_on                      | string[] | The names of the tasks that this task depends on.              | No       | []      |
