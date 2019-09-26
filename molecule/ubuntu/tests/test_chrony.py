import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chrony_package(host):
    p = host.package('chrony')
    assert p.is_installed


def test_ntp_package(host):
    p = host.package('ntp')
    assert p.is_installed is False


@pytest.mark.parametrize('chronys', ['0', '1', '2', '3'])
def test_chrony_client(host, chronys):
    chronyconf = host.file('/etc/chrony/chrony.conf')
    assert chronyconf.exists
    assert chronyconf.user == 'root'
    assert chronyconf.group == 'root'
    assert chronyconf.contains("pool server%s.molecule" % chronys)


def test_chrony_service(host):
    assert host.service('chrony').is_enabled
    assert host.service('chrony').is_running


def test_ntp_service(host):
    assert host.service('ntp').is_enabled is False
    assert host.service('ntp').is_running is False
