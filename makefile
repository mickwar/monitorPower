SHELL := /bin/bash

.PHONY : install clean

# Used for having this makefile call itself
THIS_FILE := $(lastword $(MAKEFILE_LIST))

PKG_NAME := monitorPower

# (Re)compile and (re)install based on version number in setup.py
# Tried having a rule for dist/$(PKG_NAME)-$(VERSION).tar.gz, but couldn't
# get `make` to recognize it when called through the `install` rule
install : setup.py
	python -B setup.py sdist
	$(eval VERSION := $(shell grep 'version' setup.py | cut -d\' -f2))
	pip install dist/$(PKG_NAME)-$(VERSION).tar.gz
	@$(MAKE) -f $(THIS_FILE) clean

# Update version number to today's date
#setup.py : monitorPower/*
#	sed -i -e "8s/.*/\ \ \ \ version='$(shell /bin/date +%y.%-m.%-d)'\,/" setup.py

clean :
	rm -rf $(PKG_NAME).egg-info
