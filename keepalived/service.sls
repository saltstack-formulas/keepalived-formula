# -*- coding: utf-8 -*-
# vim: ft=sls

{% from "keepalived/map.jinja" import keepalived with context %}

keepalived.service:
  service.{{ keepalived.service.state }}:
    - name: {{ keepalived.service.name }}
{% if keepalived.service.state in [ 'running', 'dead' ] %}
    - enable: {{ keepalived.service.enable }}
    - reload: True
{% endif %}

