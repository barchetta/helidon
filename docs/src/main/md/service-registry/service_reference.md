The following section lists all services and modules that provide them,
grouped by module.

Note: this is a work in progress, not listing the full set of contracts
yet!

- [Common Config](#helidon-common-config)

- [Scheduling](#helidon-scheduling)

- [Validation](#helidon-validation)

# Module `io.helidon.common.config`

| Contract | Weight | Name qualifier | Description |
|----|----|----|----|
| `io.helidon.common.config.Config` | `80` | N/A | Common config instance (empty) |

# Module `io.helidon.scheduling`

| Contract | Weight | Name qualifier | Description |
|----|----|----|----|
| `io.helidon.scheduling.TaskManager` | `90` | N/A | Management of scheduled tasks |

# Module `io.helidon.validation`

| Contract | Weight | Name qualifier | Description |
|----|----|----|----|
| `java.time.Clock` | `90` | N/A | Clock used to check calendar related constraints, defaults to current time-zone |
| `io.helidon.validation.TypeValidation` | `90` | N/A | Methods to validate type annotated with `@Validation.Validated` |
| `io.helidon.validation.spi.ConstraintValidatorProvider` | `70` | Named by the constraint annotation type (for each built-in constraint) | Constraint validator providers for each built-in constraint |
