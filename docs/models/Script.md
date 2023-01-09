# Script

This object represents a runnable script.

## Example

```json
{
  "script": "echo 'Hello World!'",
  "lang": "bash",
  "interactive": false
}
```

## Properties

| Property    | Type    | Description                                     | Required | Default |
|:------------|:--------|:------------------------------------------------|:---------|:--------|
| script      | string  | The script to run.                              | Yes      |         |
| lang        | string  | The language of the script.                     | Yes      |         |
| interactive | boolean | Whether the script should be run interactively. | No       | false   |

## Script Languages

| Language | Description | Supports Interactive |
|:---------|:------------|:--------------------:|
| bash     | Bash        |  :heavy_check_mark:  |
| sh       | sh          |  :heavy_check_mark:  |
