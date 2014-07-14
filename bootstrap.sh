#!/usr/bin/env bash

sudo apt-get -q -y install git
python /vagrant/vendor/get-pip.py
pip install -r /vagrant/requirements.txt --find-links /vagrant/vendor/packages