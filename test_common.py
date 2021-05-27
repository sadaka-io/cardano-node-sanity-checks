import os
def test_cabal_is_installed(host):
    output = host.check_output("cabal --version")
    assert output.startswith("cabal-install version 3.4.0.0")

def test_ghc_is_installed(host):
    output = host.check_output("ghc --version")
    assert output.startswith("The Glorious Glasgow Haskell Compilation System, version 8.10.2")

def test_cardano_node_is_installed(host):
    output = host.check_output("cardano-node version")
    assert output.startswith("cardano-node 1.26.2")

def test_cardano_cli_is_installed(host):
    output = host.check_output("cardano-cli version")
    assert output.startswith("cardano-cli 1.26.2")

def test_cnode_port_is_set(host):
    name = f"{os.environ['CNODE_HOME']}/scripts/env"
    env = host.file(name)
    assert env.contains('^CNODE_PORT=[0-9]\\+')

def test_cardano_node_is_enabled(host):
    service = host.service("cnode")
    assert service.is_enabled

def test_cardano_node_is_running(host):
    service = host.service("cnode")
    assert service.is_running
