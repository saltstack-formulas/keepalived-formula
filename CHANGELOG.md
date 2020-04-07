# Changelog

## [0.5.1](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.5.0...v0.5.1) (2020-04-07)


### Bug Fixes

* **service:** restart service if config changes ([0490489](https://github.com/saltstack-formulas/keepalived-formula/commit/0490489614ef1374dadce88c734b8dadfe701f5f)), closes [#37](https://github.com/saltstack-formulas/keepalived-formula/issues/37)

# [0.5.0](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.5...v0.5.0) (2020-04-06)


### Bug Fixes

* **libtofs:** “files_switch” mess up the variable exported by “map.jinja” [skip ci] ([e01cd28](https://github.com/saltstack-formulas/keepalived-formula/commit/e01cd28115d1e0c282dd6d8f68cdf8c514abbe16))


### Continuous Integration

* **kitchen:** avoid using bootstrap for `master` instances [skip ci] ([05a0959](https://github.com/saltstack-formulas/keepalived-formula/commit/05a095954d5195d28af6c8b467ef28eb9e1b18d0))


### Features

* **vrrp_sync_group:** added option for vrrp_sync_group ([45e3261](https://github.com/saltstack-formulas/keepalived-formula/commit/45e3261e53b42e611d2d2ec92135bf554f6500f8))

## [0.4.5](https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.4...v0.4.5) (2020-01-27)


### Bug Fixes

* **keepalived.conf.tmpl.jinja:** fix `has no attribute` error ([4391459](https://github.com/saltstack-formulas/keepalived-formula/commit/4391459df8cabb4818e54f54b92d5ca067671956)), closes [/freenode.logbot.info/saltstack-formulas/20200122#c3126298-c3126299](https://github.com//freenode.logbot.info/saltstack-formulas/20200122/issues/c3126298-c3126299)
* **release.config.js:** use full commit hash in commit link [skip ci] ([e9f7b11](https://github.com/saltstack-formulas/keepalived-formula/commit/e9f7b11db30e370d37059e599f35130e1137dd0a))


### Continuous Integration

* **gemfile:** restrict `train` gem version until upstream fix [skip ci] ([a1a51d5](https://github.com/saltstack-formulas/keepalived-formula/commit/a1a51d58421ed65f56703a5b011178fc5122e26f))
* **kitchen:** use `debian-10-master-py3` instead of `develop` [skip ci] ([0bb4271](https://github.com/saltstack-formulas/keepalived-formula/commit/0bb4271c89b2a64ae536e08047eb835c121dac90))
* **kitchen:** use `develop` image until `master` is ready (`amazonlinux`) [skip ci] ([2758e8e](https://github.com/saltstack-formulas/keepalived-formula/commit/2758e8ebf360be54682ee09b59a5f2767f721bbd))
* **kitchen+travis:** upgrade matrix after `2019.2.2` release [skip ci] ([e638158](https://github.com/saltstack-formulas/keepalived-formula/commit/e6381581fad1568e7f21f34776ca46a6cd137d36))
* **travis:** apply changes from build config validation [skip ci] ([4f492da](https://github.com/saltstack-formulas/keepalived-formula/commit/4f492dafff1da17a180e63181ab5c509e65cb189))
* **travis:** opt-in to `dpl v2` to complete build config validation [skip ci] ([cc7542a](https://github.com/saltstack-formulas/keepalived-formula/commit/cc7542a93f03dc8bedb5bb7ac54c2bf17d30cd02))
* **travis:** quote pathspecs used with `git ls-files` [skip ci] ([5e42eaa](https://github.com/saltstack-formulas/keepalived-formula/commit/5e42eaaa56f45a1b4c2f60fa9087f7006c865bcc))
* **travis:** run `shellcheck` during lint job [skip ci] ([47b3bce](https://github.com/saltstack-formulas/keepalived-formula/commit/47b3bce96b50f5059db0c7011497ca0a0406bcf8))
* **travis:** update `salt-lint` config for `v0.0.10` [skip ci] ([4d40216](https://github.com/saltstack-formulas/keepalived-formula/commit/4d4021675480cb44e6084a5b91ec5c9963ce831f))
* **travis:** use `major.minor` for `semantic-release` version [skip ci] ([3e9bc91](https://github.com/saltstack-formulas/keepalived-formula/commit/3e9bc91558ade2614f8de256092bfad8179feb4e))
* **travis:** use build config validation (beta) [skip ci] ([2d42d93](https://github.com/saltstack-formulas/keepalived-formula/commit/2d42d932463df75931a721ab9c7f3dbe6a584767))


### Documentation

* **contributing:** remove to use org-level file instead [skip ci] ([603176e](https://github.com/saltstack-formulas/keepalived-formula/commit/603176eec75d8602944904e2c389d483d8d34a52))
* **readme:** update link to `CONTRIBUTING` [skip ci] ([01df0d0](https://github.com/saltstack-formulas/keepalived-formula/commit/01df0d0097457cc28fbde9fd5a542848c37804f2))


### Performance Improvements

* **travis:** improve `salt-lint` invocation [skip ci] ([45a87c6](https://github.com/saltstack-formulas/keepalived-formula/commit/45a87c67fd28e8f78a887a0a7453dd7d7c9b43d7))

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
