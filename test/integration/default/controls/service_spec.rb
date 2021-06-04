# frozen_string_literal: true

control 'Keepalived service' do
  title 'should be installed'

  describe service('keepalived') do
    it { should be_installed }
    it { should be_enabled }
    it { should be_running }
  end
end
