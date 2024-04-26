# AWS Command Line Interface

[AWS CLI](https://aws.amazon.com/cli/)

## Credential Config

Create a credentials configuration file `~/.aws/credentials`.
Include the profile name, access id and key, then you may use a specific profile to access AWS resources with `--profile` option.

See [Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) for more details.

### Sample Credentials Format

```
[msc-s3-readonly]
aws_access_key_id = xxxxxxxxxxxxx
aws_secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
