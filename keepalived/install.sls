# -*- coding: utf-8 -*-
# vim: ft=sls

{% from "keepalived/map.jinja" import keepalived with context %}

keepalived.install:
  pkg.installed:
    - pkgs: {{ keepalived.pkgs | tojson }}
