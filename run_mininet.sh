# This is intended to be used to run mininet.
#
# Before running mininet we will always clean prior mininet sessions.
#
# If any argument is passed when running the command on the shell, then we
# will look for a topology with that name (on the filenames) to be runned.
# The topology must be inside the topologies directory and the passed
# argument should not contain '.py' termination.
#
# Also we are considering here that the controller is running on the ip
# 192.168.56.1
#
# Finally, we are using, here, openflow 1.0
#

mn -c
if [ -z "$1" ]; then
  mn --topo single,2 --mac --controller=remote,ip=192.168.56.1 --switch ovsk,protocols=OpenFlow10
else
  mn --custom topologies/$1.py --topo mytopo -x --mac --controller=remote,ip=192.168.56.1 --switch ovsk,protocols=OpenFlow10
fi
