# -*- coding: utf-8 -*-
# vim: ft=sls

{#- Get the `tplroot` from `tpldir` #}
{%- set tplroot = tpldir.split('/')[0] %}
{%- set sls_package_install = tplroot ~ '.package.install' %}
{%- from tplroot ~ "/map.jinja" import keepalived with context %}
{%- from tplroot ~ "/libtofs.jinja" import files_switch with context %}

include:
  - {{ sls_package_install }}

keepalived-config-file-file-managed:
  file.managed:
    - name:     {{ keepalived.config_file }}
    - user:     root
    - group:    root
    - template: jinja
    - source: {{ files_switch(['keepalived.conf.tmpl', 'keepalived.conf.tmpl.jinja'],
                              lookup='keepalived-config-file-file-managed'
                 )
              }}
    - require:
      - sls: {{ sls_package_install }}
    - context:
        config: {{ keepalived.config | json }}
