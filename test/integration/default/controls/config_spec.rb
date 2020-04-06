# frozen_string_literal: true

control 'Keepalived configuration' do
  title 'should match desired lines'

  describe file('/etc/keepalived/keepalived.conf') do
    # Default config
    its('content') { should include 'smtp_server 192.168.200.1' }

    # Custom config from pillar
    its('content') { should include 'acassen@firewall.loc' }

    # Check config from example pillar -- example vrrp sync group
    its('content') { should include 'EXAMPLE_GROUP' }

    # Check config from example pillar -- vrrp sync group item
    its('content') { should include 'VI_IPV6' }
  end
end
