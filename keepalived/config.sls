# -*- coding: utf-8 -*-
# vim: ft=sls

{% from "keepalived/map.jinja" import keepalived with context %}

keepalived.config:
  file.managed:
    - name: {{ keepalived.conffile }}
    - source: salt://keepalived/templates/keepalived.jinja
    - template: jinja
    - mode: 644
    - user: root
    - group: root


{%- for script, content in keepalived.get('scripts', {}).items() %}
keepalived.script_{{script}}:
 file.managed:
   - name: {{ script }}
   - contents: |
      {{content|indent(6)}}
   - user: root
   - group: root
   - mode: 755
   - makedirs: True
   - require_in: 
     - file: keepalived.config
{%- endfor %}
