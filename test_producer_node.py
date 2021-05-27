import os
def test_pool_name_is_set(host):
    name = f"{os.environ['CNODE_HOME']}/scripts/env"
    env = host.file(name)
    assert env.contains('^POOL_NAME=')
