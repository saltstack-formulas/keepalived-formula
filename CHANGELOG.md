# Changelog

## [0.4.4](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.3...v0.4.4) (2019-10-12)


### Bug Fixes

* **rubocop:** add fixes using `rubocop --safe-auto-correct` ([](https://github.com/saltstack-formulas/keepalived-formula/commit/ce52e09))


### Continuous Integration

* **kitchen:** change `log_level` to `debug` instead of `info` ([](https://github.com/saltstack-formulas/keepalived-formula/commit/676b623))
* **kitchen:** install required packages to bootstrapped `opensuse` [skip ci] ([](https://github.com/saltstack-formulas/keepalived-formula/commit/eaaaf9e))
* **kitchen:** use bootstrapped `opensuse` images until `2019.2.2` [skip ci] ([](https://github.com/saltstack-formulas/keepalived-formula/commit/3419a72))
* **kitchen+travis:** replace EOL pre-salted images ([](https://github.com/saltstack-formulas/keepalived-formula/commit/2de0ca2))
* **platform:** add `arch-base-latest` ([](https://github.com/saltstack-formulas/keepalived-formula/commit/39f1205))
* merge travis matrix, add `salt-lint` & `rubocop` to `lint` job ([](https://github.com/saltstack-formulas/keepalived-formula/commit/ff62d0b))
* merge travis matrix, add `salt-lint` & `rubocop` to `lint` job ([](https://github.com/saltstack-formulas/keepalived-formula/commit/0645ea6))
* use `dist: bionic` & apply `opensuse-leap-15` SCP error workaround ([](https://github.com/saltstack-formulas/keepalived-formula/commit/2cb407f))
* **travis:** merge `rubocop` linter into main `lint` job ([](https://github.com/saltstack-formulas/keepalived-formula/commit/49892c0))
* **yamllint:** add rule `empty-values` & use new `yaml-files` setting ([](https://github.com/saltstack-formulas/keepalived-formula/commit/0b782d6))

## [0.4.3](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.2...v0.4.3) (2019-08-27)


### Code Refactoring

* **pillar:** sync map.jinja with template-formula ([96fe445](https://github.com/saltstack-formulas/keepalived-formula/commit/96fe445))

## [0.4.2](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.1...v0.4.2) (2019-08-25)


### Documentation

* **readme:** fix indentation ([52c1359](https://github.com/saltstack-formulas/keepalived-formula/commit/52c1359))

## [0.4.1](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.0...v0.4.1) (2019-08-25)


### Documentation

* **readme:** add testing section ([bbc0f7b](https://github.com/saltstack-formulas/keepalived-formula/commit/bbc0f7b))

# [0.4.0](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.3.0...v0.4.0) (2019-08-10)


### Continuous Integration

* **kitchen+travis:** modify matrix to include `develop` platform ([a9cadb3](https://github.com/saltstack-formulas/keepalived-formula/commit/a9cadb3))


### Features

* **yamllint:** include for this repo and apply rules throughout ([9e29ffa](https://github.com/saltstack-formulas/keepalived-formula/commit/9e29ffa))

# [0.3.0](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.2.0...v0.3.0) (2019-05-13)


### Features

* **semantic-release:** implement an automated changelog ([51f872e](https://github.com/saltstack-formulas/keepalived-formula/commit/51f872e))
