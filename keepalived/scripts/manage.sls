# -*- coding: utf-8 -*-
# vim: ft=sls

{#- Get the `tplroot` from `tpldir` #}
{%- set tplroot = tpldir.split('/')[0] %}
{%- set sls_package_install = tplroot ~ '.package.install' %}
{%- from tplroot ~ "/map.jinja" import keepalived with context %}
{%- from tplroot ~ "/libtofs.jinja" import files_switch with context %}

include:
  - {{ sls_package_install }}

{#- Don't create scripts_dir if no scripts defined #}
{%- if 'scripts' in keepalived and keepalived.scripts  %}
keepalived-scripts-manage-file-directory:
  file.directory:
    - name: {{ keepalived.scripts_dir }}
    - makedirs: true
    - require:
      - sls: {{ sls_package_install }}
{%- endif %}

{%- for script,data in keepalived.scripts|dictsort %}
  {%- set ensure = data.get('ensure', 'present') %}
  {%- if ensure == 'present' %}
keepalived-scripts-manage-file-managed-{{ script }}:
  file.managed:
    - name:     {{ data.get('dst_file', keepalived.scripts_dir ~ '/' ~ script) }}
    - user:     {{ data.get('user', 'root') }}
    - group:    {{ data.get('group', 'root') }}
    - mode:     {{ data.get('mode', '755') }}
    - template: {{ data.get('template_engine', 'jinja') }}
    {%- if 'contents' in data %}
    - contents: |
        {{ data.contents|indent(width=8) }}
    {%- elif 'template_file' in data %}
    - source: {{ files_switch([data.template_file]) }}
    - context:
        data: {{ data.context|tojson }}
    {%- endif %}
    - require:
      - sls: {{ sls_package_install }}
  {%- elif ensure == 'absent' %}
keepalived-scripts-manage-file-absent-{{ script }}:
  file.absent:
    - name: {{ data.get('dst_file', keepalived.scripts_dir ~ '/' ~ script) }}
  {%- endif %}
{%- endfor %}
