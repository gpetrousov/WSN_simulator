####Phase 1:####
(kick-off)
Motes self-organized or pre-programmed. Sinks are preselected depending on
geography (i.e. likelihood of node appearance), sensing parameters, storage
capacity or arbitrarily.

- Ποιά διαδικασία θα ακολουθείται σε αυτή τη φάση (πρώτη κίνηση);
> 

- Θα είναι προγραμματισμένες - καθορισμένες οι  συνδέσεις ή υπάρχει αλγόριθμος;
> 

- Αριθμός motes (Cloud A), nodes (Cloud B);
> 

- Αποστάσεις;
> 


--------
####Phase 2:####
(one node phase)
A node in proximity advertises its presence; being the only node it serves also
as the network coordinator and the gateway; if no B-C link exists information
is stored in this node temporarily.

Once Phase 1 is completed and Cloud A is set to normal operation, Cloud B nodes will associate themselves with that network as sinks (elsewhere in the literature referred also as cluster heads for a tree topology).

- Πως θα γίνει η σύνδεση, ποιό sink θα συνδεθεί που;
> 

- Μέχρι ποιά απόσταση θα γίνεται το advertisment των sink nodes;
> 


--------
####Phase 3:####
(structuring)
As other nodes enter, motes reorganize themselves depending on the identity information advertised by the node; nodes self-organize to decide on clusters, gateways and storage

- Πως γίνεται η οργάνωση;
> 

- identity information advertised;
> 

- nodes forming a mesh network using the OLPC PDM algorithm (Cloud B). 
Πρέπει να εκφραστεί στον κώδικα;
> 


--------
####Phase 4:####
(steady state)
As more nodes appear the conditions for the motes become more favorable.
Multihop link distances are reduced. The network reaches maturity
conditions. Preselected mote sinks are relaxed to accommodate power usage
and extend life time.

--------


###Αλγόριθμος

- Χρονικές μονάδες;
> 

Καθώς εμφανίζονται nodes στο δίκτυο:

Each node advertises itself as a sink to Cloud A. This is achieved by having each node
broadcast a Presence Entry. All motes that receive the Entry Presence information in the
Beacon and do not have a one-hop relation to another node set the advertising node as their
sink.

- Απόσταση των νέων nodes;
> 

Motes that already have a one-hop relation with a node listen to the Presence Entry,
but unless they are looking for another node for some reason (e.g. a node with increased
storage or processing capabilities), they ignore the invitation and store it in their lookup
table for possible future usage. In this case the network topology does not change in the
child tree branches of these motes; they only update their node availability look-up table.

The motes that decide to accept the node as a cluster head, become hop 0 motes for this
cluster. 

- Αλλαγή τοπολογίας δικτύου
> 

The first node that arrives in the proximity of Cloud A assumes the role of the
coordinator of Cloud A (figure 2). All subsequent nodes will form independent clusters.

- coordinator of Cloud A == gateway of clound A ?
>

- O coordinator μπορεί να αλλάξει;
> 

- Από που θα περνάει η κίνηση; Που θέλουμε να κάνουμε τη μέτρηση (coordinator of Cloud A, independent clusters nodes);
> 

- Τα independent clusters nodes προωθούν κίνηση στον coordinator of Cloud A;
> 

The coordinator could act as a Cloud C gateway as well; other nodes may also act as gateways,
that may act as cluster heads or not. The coordinator role may be transferred between
nodes.

####Clustering

In a simplified version of the protocol presented here all nodes are considered ”equal”.
Nodes broadcast Presence Entrys as they move.

- Κάθε πόσο χρόνο γίνεται το broadcast;
> 

When a mote establishes a direct connection with a node, it informs its neighbors; for this
purpose it transmits a Presence Entry itself. In case any of these motes has a 2 or higher hop
distance, they transverse their traffic to the mote in question.

- To mote θα συνδεθεί με το νέο node αν η απόσταση είναι μικρότερη από τον τρέχον συνδεδεμένο;
> 

- Ποιούς γείτονες ειδοποιεί (μέχρι πόσα hops);
> 

####Inter-cluster organization

A node before advertising its presence must consult the already participating nodes. For this
reason it broadcasts over the WMN (Cloud B) a cluster availability request. All nodes will
propagate the request to the whole network. When the request reach the coordinator node
it will reply by denoting the PHY channel that are used by the participating nodes and their
IDs. The coordination node will additionally denote its role. When this information is
available the node will choose one of the remaining channels and will send its Presence
Entry.

- Μέχρι πόσα κανάλια μπορούμε να έχουμε;
> 

If it does not receive an association request from at least one mote within some time,
then either there are no (interested) motes in its range or it is using an occupied channel.
The node will try again in another channel on a rotation cycle.

- Πόσο χρόνο;
>

####Broken Links

A node must inform all connected motes every τ seconds on its status. If a child hop 0 mote
does not receive a Presence Entry from the node at which it is connected for t>2 τ then it
transmits a Query Beacon to that node. If after 2τ the mote still has not received a Presence
Entry it concludes that the node is no longer available and tries to connect to other available
nodes stored in the look up table it maintains. If such nodes are not available or if the look
up table is empty the mote establishes its default Cloud A link and informs its default parent
mote.

- Χρονικές μονάδες για το τ και το t;
> 

Then it also informs all its (child status by definition of the protocol) neighbor nodes that had
transverse their relate links through it so that they link to another node or return their
default status following a similar procedure to the one described above for hop 0 motes.

- Ποιά πακέτα τελικά στέλνονται από ποιούς κόμβους;
> 

- Πότε στέλνονται πακέτα δεδομένων, σε ποιούς κόμβους και τι μέγεθος έχουν;
> 

####TRAFFIC AND POWER OVERHEAD

Whenever a node moves, every mote that changes status and associates with its cluster will
broadcast a Presence Entry. Motes on its children branches will ignore it, as well as all other
hop 0 motes, but the rest of the nodes will listen to it (including its parent) and if the
distance to Cloud B lowers, they will redirect their traffic through it.

###Δεν κατάλαβα το γράφημα

Figure 4 shows a spatiotemporal example of network formation in beacon and packets
graphical representation. The horizontal axis represents space, whereas the vertical one
time. t0 denotes the time that Node A after moving transmits it Presence Entry for the first
time in its new position. (t1-t0) and (t4-t2) is the superframe active portion; (t2-t1) and (t5-t4) is
the superframe inactive portion; (t2-t0) = (t5-t2) is the Beacon Interval (BI). As we know the
active portion can be divided to the CAP period (CSMA-CA competition slots) and the CFP
period (GTS assigned slots). In the figure CAP is (t6-t5) and (t3-t2), whereas the CFP is (t4-t3)
and (>t6). In terms of colours Greenish denotes Beacons, Purplish CAP packets and Bluish CFP
packets.