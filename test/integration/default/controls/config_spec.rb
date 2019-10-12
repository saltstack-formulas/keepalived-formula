# frozen_string_literal: true

control 'Keepalived configuration' do
  title 'should match desired lines'

  describe file('/etc/keepalived/keepalived.conf') do
    # Default config
    its('content') { should include 'smtp_server 192.168.200.1' }

    # Custom config from pillar
    its('content') { should include 'acassen@firewall.loc' }
  end
end
