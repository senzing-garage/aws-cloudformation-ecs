# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
[markdownlint](https://dlaa.me/markdownlint/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

-

## [1.1.0] - 2022-08-29

### Changed in 1.1.0

- added SecondsBeforeTimeout setting
- converted to new images
- updated database version
- remove efs, apt, init container, and senzing install

## [1.0.17] - 2022-06-08

### Changed in 1.0.17

- updated resource names to allow for 21 char stack names
- updated readme to reflect stack name character limit
- added image versions to stack output
- changed UserPoolDomain to include random suffix
- updated to Senzing version 3.1.0
- updated docker images to latest stable versions

## [1.0.16] - 2022-05-1

### Changed in 1.0.16

- update images to 3.0.0
- update Senzing version to 3.0.0
- migrated from yum to apt installer
- remove "-withinfo" for loader and redoer
- update dashboards
- update to 3.0.0 paths
- add new truth set
- create new truth set data sources
- update certificate python to 3.8 and add `-1.0.2` to the filename `self-signed-certificate.zip`
- redoer queue parameters: ApplicationAutoScalingScalingPolicyRedoerLoader targetValue = 20
- add private API server URL

## [1.0.14] - 2022-03-08

### Changed in 1.0.14

- removed Jupyter
- removed flow logs
- updated docker image versions

## [1.0.13] - 2022-02-01

### Changed in 1.0.13

- added new cloudwatch dashboards

## [1.0.12] - 2022-02-01

### Changed in 1.0.12

- updated yum container

## [1.0.11] - 2021-12-01

### Changed in 1.0.11

- fixed naming issue with dashboard

## [1.0.10] - 2021-11-19

### Changed in 1.0.10

- updated senzing version
- updated stream-loader version
- fixed pass role condition

## [1.0.9] - 2021-11-01

### Changed in 1.0.9

- extended subnet range

## [1.0.8] - 2021-10-25

### Changed in 1.0.8

- added XTERM env var

## [1.0.7] - 2021-10-20

### Changed in 1.0.7

- updated to latest image versions

## [1.0.6] - 2021-10-04

### Changed in 1.0.6

- updated lambda function error reporting

## [1.0.5] - 2021-09-15

### Changed in 1.0.5

- images updated to latest version
- updated to Senzing version 2.8.2
- support WSS for the web app
- security enhancements based on marketplace findings
- standardize parameter order
- update Senzing version
- remove redoer use of EFT

## [1.0.4] - 2021-08-13

### Changed in 1.0.4

- Updated to remove old dependencies
- Removed duplicative initialization

## [1.0.3] - 2021-08-13

### Changed in 1.0.3

- Updated to use postgres client 1.1.0

## [1.0.2] - 2021-08-09

### Changed in 1.0.2

- Updated for release to S3 bucket

## [1.0.1] - 2021-06-21

### Changed in 1.0.1

- Automatically set database timeout action
- senzing-api-server uses SENZING_ENGINE_CONFIGURATION_JSON
- Improved cognito email
- Updated readme to match

## [1.0.0] - 2021-05-17

### Added to 1.0.0

- Senzing 2.6.0
- `Condition:` keys
- `SqsRedoerDeadLetter`

## [0.7.6] - 2021-05-13

### Changed in 0.7.6

- Improved autoscaling of redoer-loader
- Introduction of SSHD-max ECS Task Definition
- Compatibility with [aws-cloudformation-ecs-senzing-stack-basic](https://github.com/Senzing/aws-cloudformation-ecs-senzing-stack-basic)

## [0.7.5] - 2021-05-10

### Fixed in 0.7.5

- Give error when email not entered

## [0.7.4] - 2021-05-07

### Fixed in 0.7.4

- Senzing API Server heartbeat over private network

## [0.7.3] - 2021-05-05

### Changed in 0.7.3

- Changed Senzing API Server Memory to 16384 and CPU to 2048

## [0.7.2] - 2021-04-28

### Changed in 0.7.2

- Improved READMEs
- Removed commented code.
- Added S3 policies
- Renamed databases to have `-cluster` suffix
- Update graphic to show additional use of AWS SQS

## [0.7.1] - 2021-04-20

### Changed in 0.7.1

- Multi-region support for Lambda function on S3

## [0.7.0] - 2021-04-16

### Changed in 0.7.0

- Updated to `senzingapi-2.5.0-21104`
- Migrate from senzingdata-v1 to senzingdata-v2
  - Required by senzingapi-2.5.0
- Updated docker image versions:
  - public.ecr.aws/senzing/stream-loader:1.7.5

## [0.6.2] - 2021-04-15

### Added in 0.6.2

- Last version to support senzingapi-2.4.x and below
  - using senzingdata-v1
- An SQS queue for redo records.
- Multiple "redo-loaders" reading from the redo queue.

### Changed in 0.6.2

- Queue names

## [0.6.1] - 2021-04-12

### Changed in 0.6.1

- Shortened target group name

## [0.6.0] - 2021-04-12

### Added in 0.6.0

- Use of HTTPS protocol
  - Generation of self-signed certificate to support HTTPS access
- Use of AWS Cognito for authentication
- Route-based URLs to services.  Replacing port-based routing.
- Added comments in cloudformation.yaml for AWS Console locations

### Changed in 0.6.0

- Refactored `SENZING_ENGINE_CONFIGURATION_JSON` into SSM parameter.
- Updated to `senzingapi-2.4.2-21097`
- Updated docker image versions:
  - public.ecr.aws/senzing/entity-search-web-app:2.2.3
  - public.ecr.aws/senzing/init-container:1.6.9
  - public.ecr.aws/senzing/senzing-api-server:2.5.0
  - public.ecr.aws/senzing/stream-loader:1.7.3

## [0.5.1] - 2021-03-18

### Changed in 0.5.1

- Reorganized (alphabetized) AWS Resource declarations.

## [0.5.0] - 2021-03-16

### Added in 0.5.0

- Use of `SENZING_G2CONFIG_GTC` and `senzing/g2configtool`

### Changed in 0.5.0

- "[Truth Set](https://s3.amazonaws.com/public-read-access/TestDataSets/SenzingTruthSet/truth-set.json)" now used as sample data.
- Formatted JSON for easier modification
- Updated docker image versions:
  - public.ecr.aws/senzing/init-container:1.6.8
  - public.ecr.aws/senzing/sshd:1.1.0

## [0.4.0] - 2021-03-12

### Added in 0.4.0

- Added `slow_start.duration_seconds`
- Optional importing of sample data

### Changed in 0.4.0

- stream-producer now specifies `SENZING_DEFAULT_DATA_SOURCE` and `SENZING_DEFAULT_ENTITY_TYPE`
  - Removed from stream-loader
- Updated to senzingapi-2.4.1-21064
- Updated docker image versions:
  - public.ecr.aws/senzing/stream-loader:1.7.2
  - public.ecr.aws/senzing/stream-producer:1.4.0
  - public.ecr.aws/senzing/xterm:1.1.0

## [0.3.0] - 2021-02-26

### Added in 0.3.0

- Support for "WithInfo" Queue.

## [0.2.10] - 2021-02-19

### Changed in 0.2.10

- Updated docker image versions:
  - public.ecr.aws/senzing/init-container:1.6.6
  - public.ecr.aws/senzing/redoer:1.3.5
  - public.ecr.aws/senzing/senzing-api-server:2.3.2
  - public.ecr.aws/senzing/stream-loader:1.7.1
  - public.ecr.aws/senzing/stream-producer:1.3.3
  - public.ecr.aws/senzing/xterm:1.0.5
  - public.ecr.aws/senzing/yum:1.1.4

## [0.2.9] - 2021-02-17

### Changed in 0.2.9

- Add parameter acknowledging an insecure system.

## [0.2.8] - 2021-02-16

### Changed in 0.2.8

- Docker image URL changed from `public.ecr.aws/d5v4a2g3` to `public.ecr.aws/senzing`

## [0.2.7] - 2021-02-10

### Added in 0.2.7

- `SENZING_SKIP_DATABASE_PERFORMANCE_TEST` environment variable set in Xterm and Sshd containers.
  Already exists in Stream-loader.

## [0.2.6] - 2021-02-08

### Added in 0.2.6

- Change from DockerHub-based image registry to AWS-ECR-based registry

## [0.2.5] - 2021-02-05

### Added in 0.2.5

- Added `/var/opt/senzing` access to `senzing/stream-producer`

## [0.2.4] - 2021-02-03

### Added in 0.2.4

- `SshUsername` output variable

### Changed in 0.2.4

- Updated to latest Docker images
  - senzing/init-container:1.6.5
  - senzing/stream-loader:1.7.0
  - senzing/stream-producer:1.3.1
  - senzing/entity-search-web-app:2.2.1
- Changed output variable names to collate better
  - `ApiServerHeartbeatUrl` is now `UrlApiServerHeartbeat`
  - `JupyterUrl` is now `UrlJupyter`
  - `SwaggerUrl` is now `UrlSwagger`
  - `WebAppUrl` is now `UrlWebApp`
  - `XtermUrl` is now `UrlXterm`
- Modified host in URLs from `senzing.github.io` to `hub.senzing.com`

## [0.2.3] - 2021-01-21

### Fixed in 0.2.3

- Changed ARN references
- Added AccountID output

## [0.2.2] - 2021-01-05

### Fixed in 0.2.2

- Modified DependsOn values
- Disabled Public IP addresses

## [0.2.1] - 2021-01-04

### Fixed in 0.2.1

- Modified DependsOn values
- Disabled Jupyter by default.  Keeps crashing.
- Added missing Tags

## [0.2.0] - 2020-12-31

### Added to 0.2.0

- Support Senzing database cluster
- Autoscale Senzing API Server and Entity Search Web App
- Generate random password for SSHD container
- Remove Key/Value pairs that specify default values

## [0.1.0] - 2020-12-30

### Added to 0.1.0

- Base functionality
- For testing, all services active
- Single AWS Aurora Postgres Serverless database
