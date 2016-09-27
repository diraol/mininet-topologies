"""SC16 topology for tests.

        host5     host6
          |         |        host7      host8  
       switch5   switch6       |          |
              \  /          switch7    switch8
               \/                 \   /
                \   host1          \ / 
                 \    |             /
                   switch1         / 
                 /         \      /
                /           \    /
               /             \  /
 host4 --- switch4        switch2 --- host2
               \             /
                \           /
                 \         /
                   switch3
                      |
                    host3

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        H1 = self.addHost('h1')
        H2 = self.addHost('h2')
        H3 = self.addHost('h3')
        H4 = self.addHost('h4')
        H5 = self.addHost('h5')
        H6 = self.addHost('h6')
        H7 = self.addHost('h7')
        H8 = self.addHost('h8')
        S1 = self.addSwitch('s1')
        S2 = self.addSwitch('s2')
        S3 = self.addSwitch('s3')
        S4 = self.addSwitch('s4')
        S5 = self.addSwitch('s5')
        S6 = self.addSwitch('s6')
        S7 = self.addSwitch('s7')
        S8 = self.addSwitch('s8')

	# Add links between switches
	self.addLink(S1, S2)
	self.addLink(S2, S3)
	self.addLink(S3, S4)
	self.addLink(S4, S1)
	self.addLink(S1, S5)
	self.addLink(S1, S6)
	self.addLink(S2, S7)
	self.addLink(S2, S8)

        # Add links between hosts and switches
        self.addLink(H1, S1)
        self.addLink(H2, S2)
        self.addLink(H3, S3)
        self.addLink(H4, S4)
        self.addLink(H5, S5)
        self.addLink(H6, S6)
        self.addLink(H7, S7)
        self.addLink(H8, S8)


topos = { 'mytopo': ( lambda: MyTopo() )}
