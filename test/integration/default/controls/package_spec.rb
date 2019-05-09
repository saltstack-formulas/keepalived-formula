control 'Keepalived package' do
  title 'should be installed'

  describe package('keepalived') do
    it { should be_installed }
  end
end
