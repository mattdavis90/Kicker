Kicker
======

A small script to help people using Cobbler and Puppet

Using Kicker
------------

Kicker requires Python v2.7+

It also requires that you have a common user on all of your hosts. This user's public SSH key should be in all of the host's authorized_keys file. The best way to achieve this is to add the key in your kickstart.

Create a config file called 'settings.conf'. An example config is given in 'example.conf'.

    [Settings]
    puppetUser = puppetagent
    hostsDir = /usr/kicker/hosts

If the hosts directory doesn't exist then you will need to create it.

    $ mkdir -p /usr/kicker/hosts

Run Kicker as follows.

    python kicker

or

    ./kicker

Kicker should give meaningful help when run without any arguments.