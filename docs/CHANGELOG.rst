
Changelog
=========

`0.6.1 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.6.0...v0.6.1>`_ (2021-06-04)
------------------------------------------------------------------------------------------------------------

Bug Fixes
^^^^^^^^^


* **osfamilymap:** add package for Gentoo (\ `f07212d <https://github.com/saltstack-formulas/keepalived-formula/commit/f07212dfbb3256170f2982145b6bed31af42527a>`_\ )
* **service:** service restart handling with watch requisite (\ `1ae8918 <https://github.com/saltstack-formulas/keepalived-formula/commit/1ae8918f1efee2764fbfe5fd0ba69993d81fce58>`_\ )

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* add ``arch-master`` to matrix and update ``.travis.yml`` [skip ci] (\ `fbc97db <https://github.com/saltstack-formulas/keepalived-formula/commit/fbc97db9404b0b8d0397eb7e4e84d8465c30be22>`_\ )
* **commitlint:** ensure ``upstream/master`` uses main repo URL [skip ci] (\ `7bc7b0d <https://github.com/saltstack-formulas/keepalived-formula/commit/7bc7b0d002ae3932f9f8fc4b394ee9e8ab383129>`_\ )
* **gemfile+lock:** use ``ssf`` customised ``kitchen-docker`` repo [skip ci] (\ `5eb060c <https://github.com/saltstack-formulas/keepalived-formula/commit/5eb060cde7db66ec5f3ce8ab7f636f69e6cbdc30>`_\ )
* **gitlab-ci:** add ``rubocop`` linter (with ``allow_failure``\ ) [skip ci] (\ `b4ec26c <https://github.com/saltstack-formulas/keepalived-formula/commit/b4ec26cffb829c2dcea071105c8e2f722ff37aa9>`_\ )
* **kitchen+ci:** use latest pre-salted images (after CVE) [skip ci] (\ `d8bce5f <https://github.com/saltstack-formulas/keepalived-formula/commit/d8bce5ff94610fbcb4ee68e74eda49cbaf2cf534>`_\ )
* **kitchen+gitlab:** adjust matrix to add ``3003`` [skip ci] (\ `7732d92 <https://github.com/saltstack-formulas/keepalived-formula/commit/7732d9245776673ec7b193ebf92ef5b6a3e08b1c>`_\ )
* **kitchen+gitlab-ci:** use latest pre-salted images [skip ci] (\ `bbb13d1 <https://github.com/saltstack-formulas/keepalived-formula/commit/bbb13d1b18adf8991d67b84c418cece78db1eb0b>`_\ )
* **pre-commit:** update hook for ``rubocop`` [skip ci] (\ `afb12f1 <https://github.com/saltstack-formulas/keepalived-formula/commit/afb12f1fa82bf44ec723b34a5d8f22d2242af197>`_\ )

Tests
^^^^^


* standardise use of ``share`` suite & ``_mapdata`` state [skip ci] (\ `89986bf <https://github.com/saltstack-formulas/keepalived-formula/commit/89986bfe5ff40cebc69a1edc3e9ad1a4132543e6>`_\ )

`0.6.0 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.5.1...v0.6.0>`_ (2020-12-16)
------------------------------------------------------------------------------------------------------------

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* **gemfile.lock:** add to repo with updated ``Gemfile`` [skip ci] (\ `eebb7e0 <https://github.com/saltstack-formulas/keepalived-formula/commit/eebb7e0ea6b09bf2e9f4b53924842933f1c94fff>`_\ )
* **gitlab-ci:** use GitLab CI as Travis CI replacement (\ `15e3cdb <https://github.com/saltstack-formulas/keepalived-formula/commit/15e3cdb6a2318f5e9bcb47c885162079013dcaf6>`_\ )
* **kitchen:** use ``saltimages`` Docker Hub where available [skip ci] (\ `02347ad <https://github.com/saltstack-formulas/keepalived-formula/commit/02347adaac42522fb27bb50dc0211703abfcf7e5>`_\ )
* **kitchen+travis:** remove ``master-py2-arch-base-latest`` [skip ci] (\ `161c6a6 <https://github.com/saltstack-formulas/keepalived-formula/commit/161c6a615602ec14923e3bfaa05577de3a0adbac>`_\ )
* **pre-commit:** add to formula [skip ci] (\ `6d36686 <https://github.com/saltstack-formulas/keepalived-formula/commit/6d366861bf53960cb0a6adbee14a06232aaee67e>`_\ )
* **pre-commit:** enable/disable ``rstcheck`` as relevant [skip ci] (\ `ec4fa7b <https://github.com/saltstack-formulas/keepalived-formula/commit/ec4fa7bc11a1bf050a127cb43b59334d70e04902>`_\ )
* **pre-commit:** finalise ``rstcheck`` configuration [skip ci] (\ `635902d <https://github.com/saltstack-formulas/keepalived-formula/commit/635902dd4d2eb0e4e003a314520eca4ab9acd75e>`_\ )
* **travis:** add notifications => zulip [skip ci] (\ `3ae2959 <https://github.com/saltstack-formulas/keepalived-formula/commit/3ae2959f1305a6da1120f5c8e1cbcc7fd7422d70>`_\ )
* **workflows/commitlint:** add to repo [skip ci] (\ `80bdb6c <https://github.com/saltstack-formulas/keepalived-formula/commit/80bdb6cac4f381441975df7765dab6c0cb690975>`_\ )

Features
^^^^^^^^


* **config:** add support for switch type parameters (\ `20d67c1 <https://github.com/saltstack-formulas/keepalived-formula/commit/20d67c13a17377ef59df9fcd0970354d90aec772>`_\ )
* **scripts:** deploy helper scripts (\ `5fc37fa <https://github.com/saltstack-formulas/keepalived-formula/commit/5fc37fa6fb319ef8c718b1e8e4979bce77282021>`_\ )

Styles
^^^^^^


* **libtofs.jinja:** use Black-inspired Jinja formatting [skip ci] (\ `16d6742 <https://github.com/saltstack-formulas/keepalived-formula/commit/16d674294900317db54e8133a35a5871553d4afb>`_\ )

`0.5.1 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.5.0...v0.5.1>`_ (2020-04-07)
------------------------------------------------------------------------------------------------------------

Bug Fixes
^^^^^^^^^


* **service:** restart service if config changes (\ `0490489 <https://github.com/saltstack-formulas/keepalived-formula/commit/0490489614ef1374dadce88c734b8dadfe701f5f>`_\ ), closes `#37 <https://github.com/saltstack-formulas/keepalived-formula/issues/37>`_

`0.5.0 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.5...v0.5.0>`_ (2020-04-06)
------------------------------------------------------------------------------------------------------------

Bug Fixes
^^^^^^^^^


* **libtofs:** “files_switch” mess up the variable exported by “map.jinja” [skip ci] (\ `e01cd28 <https://github.com/saltstack-formulas/keepalived-formula/commit/e01cd28115d1e0c282dd6d8f68cdf8c514abbe16>`_\ )

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* **kitchen:** avoid using bootstrap for ``master`` instances [skip ci] (\ `05a0959 <https://github.com/saltstack-formulas/keepalived-formula/commit/05a095954d5195d28af6c8b467ef28eb9e1b18d0>`_\ )

Features
^^^^^^^^


* **vrrp_sync_group:** added option for vrrp_sync_group (\ `45e3261 <https://github.com/saltstack-formulas/keepalived-formula/commit/45e3261e53b42e611d2d2ec92135bf554f6500f8>`_\ )

`0.4.5 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.4...v0.4.5>`_ (2020-01-27)
------------------------------------------------------------------------------------------------------------

Bug Fixes
^^^^^^^^^


* **keepalived.conf.tmpl.jinja:** fix ``has no attribute`` error (\ `4391459 <https://github.com/saltstack-formulas/keepalived-formula/commit/4391459df8cabb4818e54f54b92d5ca067671956>`_\ ), closes `/freenode.logbot.info/saltstack-formulas/20200122#c3126298-c3126299 <https://github.com//freenode.logbot.info/saltstack-formulas/20200122/issues/c3126298-c3126299>`_
* **release.config.js:** use full commit hash in commit link [skip ci] (\ `e9f7b11 <https://github.com/saltstack-formulas/keepalived-formula/commit/e9f7b11db30e370d37059e599f35130e1137dd0a>`_\ )

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* **gemfile:** restrict ``train`` gem version until upstream fix [skip ci] (\ `a1a51d5 <https://github.com/saltstack-formulas/keepalived-formula/commit/a1a51d58421ed65f56703a5b011178fc5122e26f>`_\ )
* **kitchen:** use ``debian-10-master-py3`` instead of ``develop`` [skip ci] (\ `0bb4271 <https://github.com/saltstack-formulas/keepalived-formula/commit/0bb4271c89b2a64ae536e08047eb835c121dac90>`_\ )
* **kitchen:** use ``develop`` image until ``master`` is ready (\ ``amazonlinux``\ ) [skip ci] (\ `2758e8e <https://github.com/saltstack-formulas/keepalived-formula/commit/2758e8ebf360be54682ee09b59a5f2767f721bbd>`_\ )
* **kitchen+travis:** upgrade matrix after ``2019.2.2`` release [skip ci] (\ `e638158 <https://github.com/saltstack-formulas/keepalived-formula/commit/e6381581fad1568e7f21f34776ca46a6cd137d36>`_\ )
* **travis:** apply changes from build config validation [skip ci] (\ `4f492da <https://github.com/saltstack-formulas/keepalived-formula/commit/4f492dafff1da17a180e63181ab5c509e65cb189>`_\ )
* **travis:** opt-in to ``dpl v2`` to complete build config validation [skip ci] (\ `cc7542a <https://github.com/saltstack-formulas/keepalived-formula/commit/cc7542a93f03dc8bedb5bb7ac54c2bf17d30cd02>`_\ )
* **travis:** quote pathspecs used with ``git ls-files`` [skip ci] (\ `5e42eaa <https://github.com/saltstack-formulas/keepalived-formula/commit/5e42eaaa56f45a1b4c2f60fa9087f7006c865bcc>`_\ )
* **travis:** run ``shellcheck`` during lint job [skip ci] (\ `47b3bce <https://github.com/saltstack-formulas/keepalived-formula/commit/47b3bce96b50f5059db0c7011497ca0a0406bcf8>`_\ )
* **travis:** update ``salt-lint`` config for ``v0.0.10`` [skip ci] (\ `4d40216 <https://github.com/saltstack-formulas/keepalived-formula/commit/4d4021675480cb44e6084a5b91ec5c9963ce831f>`_\ )
* **travis:** use ``major.minor`` for ``semantic-release`` version [skip ci] (\ `3e9bc91 <https://github.com/saltstack-formulas/keepalived-formula/commit/3e9bc91558ade2614f8de256092bfad8179feb4e>`_\ )
* **travis:** use build config validation (beta) [skip ci] (\ `2d42d93 <https://github.com/saltstack-formulas/keepalived-formula/commit/2d42d932463df75931a721ab9c7f3dbe6a584767>`_\ )

Documentation
^^^^^^^^^^^^^


* **contributing:** remove to use org-level file instead [skip ci] (\ `603176e <https://github.com/saltstack-formulas/keepalived-formula/commit/603176eec75d8602944904e2c389d483d8d34a52>`_\ )
* **readme:** update link to ``CONTRIBUTING`` [skip ci] (\ `01df0d0 <https://github.com/saltstack-formulas/keepalived-formula/commit/01df0d0097457cc28fbde9fd5a542848c37804f2>`_\ )

Performance Improvements
^^^^^^^^^^^^^^^^^^^^^^^^


* **travis:** improve ``salt-lint`` invocation [skip ci] (\ `45a87c6 <https://github.com/saltstack-formulas/keepalived-formula/commit/45a87c67fd28e8f78a887a0a7453dd7d7c9b43d7>`_\ )

`0.4.4 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.3...v0.4.4>`_ (2019-10-12)
------------------------------------------------------------------------------------------------------------

Bug Fixes
^^^^^^^^^


* **rubocop:** add fixes using ``rubocop --safe-auto-correct`` (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/ce52e09>`_\ )

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* **kitchen:** change ``log_level`` to ``debug`` instead of ``info`` (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/676b623>`_\ )
* **kitchen:** install required packages to bootstrapped ``opensuse`` [skip ci] (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/eaaaf9e>`_\ )
* **kitchen:** use bootstrapped ``opensuse`` images until ``2019.2.2`` [skip ci] (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/3419a72>`_\ )
* **kitchen+travis:** replace EOL pre-salted images (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/2de0ca2>`_\ )
* **platform:** add ``arch-base-latest`` (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/39f1205>`_\ )
* merge travis matrix, add ``salt-lint`` & ``rubocop`` to ``lint`` job (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/ff62d0b>`_\ )
* merge travis matrix, add ``salt-lint`` & ``rubocop`` to ``lint`` job (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/0645ea6>`_\ )
* use ``dist: bionic`` & apply ``opensuse-leap-15`` SCP error workaround (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/2cb407f>`_\ )
* **travis:** merge ``rubocop`` linter into main ``lint`` job (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/49892c0>`_\ )
* **yamllint:** add rule ``empty-values`` & use new ``yaml-files`` setting (\ ` <https://github.com/saltstack-formulas/keepalived-formula/commit/0b782d6>`_\ )

`0.4.3 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.2...v0.4.3>`_ (2019-08-27)
------------------------------------------------------------------------------------------------------------

Code Refactoring
^^^^^^^^^^^^^^^^


* **pillar:** sync map.jinja with template-formula (\ `96fe445 <https://github.com/saltstack-formulas/keepalived-formula/commit/96fe445>`_\ )

`0.4.2 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.1...v0.4.2>`_ (2019-08-25)
------------------------------------------------------------------------------------------------------------

Documentation
^^^^^^^^^^^^^


* **readme:** fix indentation (\ `52c1359 <https://github.com/saltstack-formulas/keepalived-formula/commit/52c1359>`_\ )

`0.4.1 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.4.0...v0.4.1>`_ (2019-08-25)
------------------------------------------------------------------------------------------------------------

Documentation
^^^^^^^^^^^^^


* **readme:** add testing section (\ `bbc0f7b <https://github.com/saltstack-formulas/keepalived-formula/commit/bbc0f7b>`_\ )

`0.4.0 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.3.0...v0.4.0>`_ (2019-08-10)
------------------------------------------------------------------------------------------------------------

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^


* **kitchen+travis:** modify matrix to include ``develop`` platform (\ `a9cadb3 <https://github.com/saltstack-formulas/keepalived-formula/commit/a9cadb3>`_\ )

Features
^^^^^^^^


* **yamllint:** include for this repo and apply rules throughout (\ `9e29ffa <https://github.com/saltstack-formulas/keepalived-formula/commit/9e29ffa>`_\ )

`0.3.0 <https://github.com/saltstack-formulas/keepalived-formula/compare/v0.2.0...v0.3.0>`_ (2019-05-13)
------------------------------------------------------------------------------------------------------------

Features
^^^^^^^^


* **semantic-release:** implement an automated changelog (\ `51f872e <https://github.com/saltstack-formulas/keepalived-formula/commit/51f872e>`_\ )
